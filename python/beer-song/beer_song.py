def _bottles(n):
    if n >= 1:
        return f"{n} bottle{'s' if n > 1 else ''}"

    elif n == 0:
        return "no more bottles"


def first_line(n):
    bottles = _bottles(n)
    return f"{bottles.capitalize()} of beer on the wall, {bottles} of beer."


def second_line(n):
    prefix = (
        f"Take {'one' if n!=1 else 'it'} down and pass it around"
        if n > 0
        else "Go to the store and buy some more"
    )
    return f"{prefix}, {_bottles((n-1) % 100)} of beer on the wall."


def recite(start, take=1):
    lyrics = []
    for n in range(start, start - take, -1):
        lyrics += [first_line(n), second_line(n)]
        if n != start - take + 1:
            lyrics.append("")

    return lyrics
