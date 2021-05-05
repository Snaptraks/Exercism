N = 12

VERSES = [
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
    "and a Partridge in a Pear Tree",
]

DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


def recite_verse(verse):
    prefix = f"On the {DAYS[verse-1]} day of Christmas my true love gave to me"

    if verse == 1:
        # special case to remove the prefix
        # if on Python 3.9, use .removeprefix() instead
        suffix = VERSES[N - 1][len("and "):]

    else:
        suffix = ", ".join(VERSES[N - verse:])

    return f"{prefix}: {suffix}."


def recite(start_verse, end_verse):
    song = []

    for verse in range(start_verse, end_verse + 1):
        song.append(recite_verse(verse))
        print(song[-1])

    return song
