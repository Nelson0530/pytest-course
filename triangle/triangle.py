# validity of triangle given sides

# function defintion to check validity
def is_valid_triangle(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False

def type_of_triangle(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "不是三角形"
    elif (a == b) and (b == c):
        return "正三角形"
    elif (a == b) or (b == c) or (c == a):
        return "等腰三角形"
    elif (a * a + b * b == c * c) or (b * b + c * c == a * a) or (c * c + a * a == b * b):
        return "直角三角形"
    else:
        return "一般三角形"

