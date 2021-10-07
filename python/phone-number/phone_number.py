import re


class PhoneNumber:
    def __init__(self, number):
        _number = self._clean_number(number)
        self._verify_number(_number)
        self.number = _number[-10:]
        self.area_code = _number[-10:-7]
        self.exchange_code = _number[-7:-4]
        self.subscriber_number = number[-4:]

    def pretty(self):
        return (f"({self.area_code})"
                f"-{self.exchange_code}"
                f"-{self.subscriber_number}")

    def _clean_number(self, number):
        cleaned_number = "".join(re.findall("[0-9]+", number))

        return cleaned_number

    def _verify_number(self, number):
        if len(number) < 10:
            raise ValueError("Number not long enough")

        if int(number[-10]) < 2 or int(number[-7]) < 2:
            raise ValueError("Invalid area or exchange code")

        if len(number) > 10 and number[0] != "1":
            raise ValueError("Invalid country code")
