from collections import defaultdict
import json


def json_wrapper(f):
    def wrapper(self, url, payload=None):
        if isinstance(payload, str):
            payload = json.loads(payload)

        return json.dumps(f(self, url, payload))

    return wrapper


class User:
    def __init__(self, name, owes=None, owed_by=None, **kwargs):
        self.name = name
        self.records = defaultdict(lambda: 0)

        owes = owes or {}
        for lender, amount in owes.items():
            self.borrow_from(lender, amount)

        owed_by = owed_by or {}
        for borrower, amount in owed_by.items():
            self.loan_to(borrower, amount)

    def borrow_from(self, name, amount):
        self.records[name] -= amount

    def loan_to(self, name, amount):
        self.records[name] += amount

    def owes(self):
        return {name: -amount for name, amount in self.records.items()
                if amount < 0}

    def owed_by(self):
        return {name: amount for name, amount in self.records.items()
                if amount > 0}

    def balance(self):
        return sum(self.records.values())

    def to_dict(self):
        return {
            "name": self.name,
            "owes": self.owes(),
            "owed_by": self.owed_by(),
            "balance": self.balance(),
        }


class RestAPI:
    def __init__(self, database=None):
        database = database or {"users": []}
        self.users = {
            user["name"]: User(**user)
            for user in database["users"]
        }

    @json_wrapper
    def get(self, url, payload=None):
        if url == "/users":
            payload = payload or {"users": []}
            return self._get_users(**payload)

    @json_wrapper
    def post(self, url, payload=None):
        if url == "/add":
            return self._post_add(**payload)

        if url == "/iou":
            return self._post_iou(**payload)

    def _get_users(self, users):
        return {"users": [user.to_dict()
                          for user in self.users.values()
                          if len(users) == 0 or user.name in users]}

    def _post_add(self, user):
        user = User(user)
        if user.name in self.users:
            raise ValueError("User already in database.")
        return user.to_dict()

    def _post_iou(self, borrower, lender, amount):
        self.users[borrower].borrow_from(lender, amount)
        self.users[lender].loan_to(borrower, amount)

        return {"users": sorted([
            self.users[borrower].to_dict(),
            self.users[lender].to_dict(),
        ], key=lambda u: u["name"])}
