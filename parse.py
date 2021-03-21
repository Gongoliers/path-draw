def trim(string, delim, num):
    start = string.find(delim)
    while start >= 0 and num > 1:
        start = string.find(delim, start+len(delim))
        num -= 1
    return string[0:start]


def delim_parse(blob, delim):
    if type(blob) != list:
        blob = [blob]
    blob_str = '\n'.join(blob)
    blob_str = blob_str.replace('\n', delim)
    path = []
    # TODO: Fix mangling of the final element(s)
    while blob_str:

        # Break off the first distance-angle pair
        s = trim(blob_str, delim, 2)
        pair = s.split(delim)

        # Add the pair to the path
        if len(pair) == 2:
            path.append(pair)
        else:

            # Assumes that None will be processed correctly
            path.append([pair[0], None])


        # Remove parsed substring from string
        blob_str = blob_str[len(s)+len(delim):]
    return path


if __name__ == "__main__":
    print(delim_parse("This\tis\ta\ntest\tof\nthe\nparser\n.\tAnother\tstring\there", '\t'))
    print(delim_parse(["This\tis\ta\ntest\tof\nthe\nparser\n.\tAnother\tstring\there"], '\t'))
    print(delim_parse(["This\tis\ta", "test\tof", "the", "parser", ".\tAnother\tstring\there"], '\t'))
