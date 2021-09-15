BELOW_TWENTY = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

TENS = {
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

THOUSANDS = {
    0: "",
    1: "thousand",
    2: "million",
    3: "billion",
}


def split_in_thousands(number: int) -> list[int]:
    splits = []
    while number:
        splits.append(number % 1000)
        number //= 1000

    return splits[::-1]


def say_below_hundred(number: int) -> str:
    if number == 0:
        return ""

    if number < 20:
        return BELOW_TWENTY[number]

    tens = number // 10
    units = number % 10
    if units == 0:
        return TENS[tens]

    return f"{TENS[tens]}-{BELOW_TWENTY[number % 10]}"


def say_below_thousand(number: int) -> str:
    hundreds = number // 100
    if hundreds:
        hundred_word = f"{BELOW_TWENTY[hundreds]} hundred "

    else:
        hundred_word = ""

    return f"{hundred_word}{say_below_hundred(number % 100)}"


def say(number: int):
    if not (0 <= number <= 999_999_999_999):
        raise ValueError(f"Number {number} is out of range.")

    # special case of zero
    if number == 0:
        return BELOW_TWENTY[number]

    split_number = split_in_thousands(number)
    print(split_number)

    magnitude = len(split_number)
    for n, block in enumerate(split_number):
        print(say_below_thousand(block), THOUSANDS[magnitude - n - 1])

    return " ".join([
        f"{say_below_thousand(block)} {THOUSANDS[magnitude -n -1]}"
        for n, block in enumerate(split_number)
        if block != 0
    ]).strip()
