import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    for line in lines:
        # Match titles first
        match = re.match("(#+) (.*)", line)
        if match is not None:
            title_level = len(match.group(1))
            line = f"<h{title_level}>{match.group(2)}</h{title_level}>"

        # Match list items
        match = re.match(r'\* (.*)', line)
        if match is not None:
            list_item = match.group(1)

            line = f'<li>{list_item}</li>'
            # If we were not in a list before, we are now and lets start one
            if not in_list:
                in_list = True
                line = f"<ul>{line}"

        else:  # not in a list item
            if in_list:
                in_list_append = True
                in_list = False

        match = re.match('<h|<ul|<p|<li', line)
        if match is None:
            line = f'<p>{line}</p>'

        match = re.match('(.*)__(.*)__(.*)', line)
        if match is not None:
            parts = [match.group(i) for i in (1, 2, 3)]
            line = f"{parts[0]}<strong>{parts[1]}</strong>{parts[2]}"

        match = re.match('(.*)_(.*)_(.*)', line)
        if match is not None:
            parts = [match.group(i) for i in (1, 2, 3)]
            line = f"{parts[0]}<em>{parts[1]}</em>{parts[2]}"

        if in_list_append:
            line = f"</ul>{line}"
            in_list_append = False

        res += line
    if in_list:
        res += '</ul>'
    return res
