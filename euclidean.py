def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = 60
b = 48
print("GCD of", a, "and", b, "is:", gcd(a, b))
