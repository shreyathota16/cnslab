def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


a = 60
b = 48
gcd_value, x, y = extended_gcd(a, b)
print("GCD of", a, "and", b, "is:", gcd_value)
print("Coefficients x and y are:", x, "and", y)
print(f"Verification: {a} * ({x}) + {b} * ({y}) = {gcd_value}")
