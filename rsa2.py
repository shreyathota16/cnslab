import math 
p = 3
q = 7
n = p*q
print("n =", n)
phi = (p-1)*(q-1)
print("phi = ",phi)
e = 2
while(e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1
print("e =", e)
j = 0
while(j<phi):
    if (j*e%phi == 1):
        d = j
        break 
    j+=1
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
msg = 11
print(f'Original message:{msg}')
C =(msg**e)%n
print(f'Encrypted message: {C}')
M = (C**d)%n
print(f'Decrypted message: {M}')
