def commands(binary_str):
    reverse, jump, close, double, wink = [int(_) for _ in list(binary_str)]

    _commands = []
    if wink:
        _commands.append("wink")

    if double:
        _commands.append("double blink")

    if close:
        _commands.append("close your eyes")

    if jump:
        _commands.append("jump")

    if reverse:
        _commands.reverse()

    return _commands
