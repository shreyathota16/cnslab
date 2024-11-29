def rc4(key, text):
    # Key-Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    result = []
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        result.append(char ^ K) # XOR with keystream byte
    return bytes(result)
# Usage example:
key = b'secretkey'
plaintext = b'This is shivani'
ciphertext = rc4(key, plaintext)
decrypted = rc4(key, ciphertext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted.decode('utf-8'))