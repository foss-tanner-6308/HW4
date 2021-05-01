# helper function taken from stack overflow because I could not get, for example,
# first.isalpha(), first.isdigit(), and first.isalnum() to work properly. These
# alone would cause all tests to fail so I looked for an alternative, which used
# isdigit() in a loop

# https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
def hasNumbers(s):
    return any(i.isdigit() for i in s)


def full_name(first, last):
    if hasNumbers(first):
        raise ValueError("Name can only be made of letters.")
    if hasNumbers(last):
        raise ValueError("Name can only be made of letters.")
    return first + " " + last