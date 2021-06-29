def is_armstrong_number(number):
    str_number = str(number)
    number_of_digits = len(str_number)

    new_number = sum([int(d)**number_of_digits for d in str_number])
    return new_number == number
