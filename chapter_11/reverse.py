def reverse(string):
    if not string:
        return ""

    return reverse(string[1:]) + string[0]
