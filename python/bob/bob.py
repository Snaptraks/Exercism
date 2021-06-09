import string


def response(hey_bob):
    hey_bob = hey_bob.strip()

    is_question = hey_bob.endswith("?")
    has_ascii = any([c in string.ascii_letters for c in hey_bob])
    is_all_caps = (hey_bob == hey_bob.upper()) and has_ascii

    if len(hey_bob) == 0:
        return "Fine. Be that way!"

    elif is_question and is_all_caps:
        return "Calm down, I know what I'm doing!"

    elif is_question:
        return "Sure."

    elif is_all_caps:
        return "Whoa, chill out!"

    return "Whatever."
