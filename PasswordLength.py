def PasswordLen(string):
    if len(string) < 8:
        return 0
    elif len(string) >= 8 and len(string) <=11:
        return 1
    else:
        return 2
        