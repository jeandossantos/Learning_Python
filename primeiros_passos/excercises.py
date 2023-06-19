import math
def square_sum(numbers):
    rs = 0
    
    for v in numbers:
        rs += v ** 2
    return rs

rs = square_sum([1, 2, 2])

print(rs)
