def trim(string, delim, num):
    start = string.find(delim)
    while start >= 0 and num > 1:
        start = string.find(delim, start+len(delim))
        num -= 1

    # Fixes removal of last character
    if start < 0:
        start = len(string)
    return string[0:start]


def delim_parse(blob, delim):
    if type(blob) != list:
        blob = [blob]
    blob_str = '\n'.join(blob)
    blob_str = blob_str.replace('\n', delim)
    path = []
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


def tsv_parse(blob):
    return delim_parse(blob, '\t')


def csv_parse(blob):
    return delim_parse(blob, ',')


def space_parse(blob):
    return delim_parse(blob, ' ')


if __name__ == "__main__":
    print(delim_parse("This\tis\ta\ntest\tof\nthe\nparser\n.\tAnother\tstring\there", '\t'))
    print(delim_parse(["This\tis\ta\ntest\tof\nthe\nparser\n.\tAnother\tstring\there"], '\t'))
    print(delim_parse(["This\tis\ta", "test\tof", "the", "parser", ".\tAnother\tstring\there"], '\t'))

    print(tsv_parse("This\tis\ta\ntest\tof\nthe\nparser\n.\tAnother\tstring\there"))
    print(tsv_parse(["This\tis\ta\ntest\tof\nthe\nparser\n.\tAnother\tstring\there"]))
    print(tsv_parse(["This\tis\ta", "test\tof", "the", "parser", ".\tAnother\tstring\there"]))

    print(csv_parse("This,is,a\ntest,of\nthe\nparser\n.,Another,string,here"))
    print(csv_parse(["This,is,a\ntest,of\nthe\nparser\n.,Another,string,here"]))
    print(csv_parse(["This,is,a", "test,of", "the", "parser", ".,Another,string,here"]))

    print(space_parse("This is a\ntest of\nthe\nparser\n. Another string here"))
    print(space_parse(["This is a\ntest of\nthe\nparser\n. Another string here"]))
    print(space_parse(["This is a", "test of", "the", "parser", ". Another string here"]))
