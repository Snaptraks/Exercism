import threading


class BankAccount:
    def __init__(self):
        self._is_open = False
        self._lock = threading.Lock()

    def get_balance(self):
        if self._is_open:
            return self._balance

        else:
            raise ValueError("Account is closed.")

    def open(self):
        if self._is_open:
            raise ValueError("Account is already opened.")
        self._is_open = True
        self._balance = 0

    def deposit(self, amount):
        if not self._is_open:
            raise ValueError("Account is not opened yet.")

        if amount < 0:
            raise ValueError(f"Cannot deposit negative amount ({amount}).")

        with self._lock:
            self._balance += amount

    def withdraw(self, amount):
        if not self._is_open:
            raise ValueError("Account is not opened yet.")

        if amount < 0:
            raise ValueError(f"Cannot withdraw negative amount ({amount}).")

        if amount > self._balance:
            raise ValueError(
                "Cannot withdraw more than current balance "
                f"({amount} > {self._balance})."
            )

        with self._lock:
            self._balance -= amount

    def close(self):
        if self._is_open:
            self._is_open = False

        else:
            raise ValueError("Account is closed.")
