def Complexity(string):
    point = 0
    low = False
    high = False
    num = False
    special = False
    for char in string:
        isnum = False
        ischar = False
        if 'A'<= char <='Z' or 'a' <= char <='z':
            ischar = True
        if '0' <= char <= '9':
            isnum = True
        if not high and 'A' <= char <= 'Z':
            high = True
            point += 1
            continue
        if not low and 'a' <= char <= 'z':
            low = True
            point += 1
            continue
        if not num and '0' <= char <= '9':
            num = True
            point += 1
            continue
        if not special and (not isnum and not ischar):
            special = True
            point += 1
            continue
        if point == 4:
            break
    return point
        
        


        