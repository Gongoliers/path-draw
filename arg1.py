def count(string, character='-'):
    if not string:
        return 0
    elif string[0] == character:
        return 1 + count(string[1:], character)
    else:
        return 0


def options(argv):
    for arg in argv[1:]:
        depth = count(arg)
        if depth <= 0 or depth > 2:

            # Parse value
            option_value(arg)

        elif depth == 1:

            # Parse GNU / single '-'
            option_short(arg)

        elif depth == 2:

            # Parse long / two '-'
            option_long(arg)



if __name__ == "__main__":
    string = "--test"
    print(count(string, "-"), string)
