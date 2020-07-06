def summer_69_s(arr):
    
    total = 0
    add = True

    for i in arr:
        flip_case = i==6 or (not add and i==9)
        if flip_case:
            add = not add
            continue
        if add:
            total += i
        
    return total

def summer_69(arr):
    
    total = 0
    add = True

    for i in arr:
        while add:
            if i != 6:
                total = total + i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total

summer_69_s([1, 3, 5])
summer_69([1, 3, 5])
summer_69_s([4, 5, 6, 7, 8, 9])
summer_69([4, 5, 6, 7, 8, 9])
summer_69_s([2, 1, 6, 9, 11])
summer_69([2, 1, 6, 9, 11])