import re


def grep(pattern, flags, files):
    flags = flags.split()
    re_flags = 0

    if "-i" in flags:
        re_flags |= re.I
    pattern = re.compile(pattern, re_flags)

    result = ""
    files_result = ""

    for file in files:
        with open(file) as f:
            for line_number, line in enumerate(f.readlines()):
                prefix = ""
                if "-n" in flags:
                    line_number += 1
                    prefix = f"{line_number}:{prefix}"

                if len(files) > 1:
                    prefix = f"{file}:{prefix}"

                if "-x" in flags:
                    match = pattern.fullmatch(line.strip())
                else:
                    match = pattern.search(line)

                if bool(match) != ("-v" in flags):
                    if file not in files_result:
                        files_result += f"{file}\n"
                    result += f"{prefix}{line}"

    if "-l" in flags:
        return "".join(list(files_result))

    return result
