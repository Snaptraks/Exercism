import re


class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num
        # cache validity
        self._valid = None

    def valid(self):
        # use cached result
        if self._valid is not None:
            return self._valid
        else:
            self._valid = self.check_validity()
            return self._valid

    def check_validity(self):
        pattern = "^ *[0-9][0-9 ]*$"

        if re.match(pattern, self.card_num):
            return self.luhn_algorithm()
        else:
            return False

    def luhn_algorithm(self):
        """Assume a card_num with only numbers and spaces."""

        stripped_card_num = self.card_num.replace(" ", "")
        if len(stripped_card_num) <= 1:
            return False

        digits = [int(x) for x in stripped_card_num]
        every_second_digit_from_right = digits[-2::-2]
        other_digits = digits[::-2]
        every_second_digit_doubled = [
            self.substract_9_if_bigger(2 * x)
            for x in every_second_digit_from_right]

        sum_all_digits = sum(other_digits) + sum(every_second_digit_doubled)
        return sum_all_digits % 10 == 0

    def substract_9_if_bigger(self, x):
        if x <= 9:
            return x
        else:
            return self.substract_9_if_bigger(x - 9)
