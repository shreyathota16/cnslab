import numpy as np
def encrypt(key, pt):
    pt_matrix = [ord(char) - ord('A') for char in pt]
    key_mat = [[0 for _ in range(3)]for _ in range(3)]
    char = 0
    for i in range(3):
        for j in range(3):
            x = ord(key[char])-ord('A')
            key_mat[i][j] = x
            char+=1
    en_mat = np.dot(key_mat,pt_matrix)%26
    en_msg = ''
    for char in en_mat:
        en_msg+=chr(char+ord('A'))
    return en_msg,en_mat
def decrypt(inverse_key_matrix, en_mat):
    de_mat = np.dot(inverse_key_matrix, en_mat) % 26
    de_mat = [int(num) for num in de_mat]  
    de_msg = ''
    for num in de_mat:
        x = chr(int(num) + ord('A'))
        de_msg+=x 
    return de_msg

key = "GYBNQKURP"
pt = "ACT"
encrypted_message, encrypted_matrix = encrypt(key, pt)
print("Encrypted Message:", encrypted_message)
inverse_key_matrix = np.array([
        [8, 5, 10],
        [21, 8, 21],
        [21, 12, 8]
    ])
decrypted_message = decrypt(inverse_key_matrix, encrypted_matrix)
print("Decrypted Message:", decrypted_message)