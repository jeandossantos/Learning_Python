def grow(arr):
    arr.sort()
    rs = 1

    for i in arr:
        rs *= i

    return rs


print(grow([6, 2, 1, 8, 10]))
