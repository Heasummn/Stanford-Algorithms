def karatsuba(x1, x2):
    if x1 < 10 or x2 < 10:
        return x1 * x2

    length = max(len(str(x1)), len(str(x2)))
    half_l = length // 2

    a = x1 // pow(10, half_l)
    b = x1 % pow(10, half_l)
    c = x2 // pow(10, half_l)
    d = x2 % pow(10, half_l)

    product1 = karatsuba(a, c)
    product3 = karatsuba(b, d)
    expanded_p = karatsuba(a + b, c + d)
    product2 = expanded_p - product1 - product3

    return pow(10, half_l*2) * product1 + pow(10, half_l) * product2 + product3

def alg(file):
    with open(file) as f:
        x1 = int(f.readline())
        x2 = int(f.readline())
        return karatsuba(x1, x2)
