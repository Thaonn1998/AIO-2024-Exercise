# 4 functions sin(x), cos(x), sinh(x), và cosh(x)

def approx_sin(x, n): #functions sin(x)
    result = 0
    for i in range(n):
        term = 1
        for j in range(2 * i + 1):
            term *= x / (j + 1)
        term *= (-1) ** i
        result += term
    return result

def approx_cos(x, n): #functions cos(x)
    result = 0
    for i in range(n):
        term = 1
        for j in range(2 * i):
            term *= x / (j + 1)
        term *= (-1) ** i
        result += term
    return result

def approx_sinh(x, n): #functions sinh(x)
    result = 0
    for i in range(n):
        term = 1
        for j in range(2 * i + 1):
            term *= x / (j + 1)
        result += term
    return result

def approx_cosh(x, n): #functions cosh(x)
    result = 0
    for i in range(n):
        term = 1
        for j in range(2 * i):
            term *= x / (j + 1)
        result += term
    return result

if __name__ == "__main__":
    print(approx_sin(x=3.14, n=10))
    print(approx_cos(x=3.14, n=10))
    print(approx_sinh(x=3.14, n=10))
    print(approx_cosh(x=3.14, n=10))