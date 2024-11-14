def rail_fence_encrypt(plaintext, rails):
    plaintext = plaintext.replace(" ", "").upper()
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    row, down = 0, True
    for i in range(len(plaintext)):
        fence[row][i] = plaintext[i]
        if down:
            if row == rails - 1:
                down = False
                row -= 1
            else:
                row += 1
        else:
            if row == 0:
                down = True
                row += 1
            else:
                row -= 1
    ciphertext = ''.join([''.join(r) for r in fence])
    return ciphertext


def rail_fence_decrypt(ciphertext, rails):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    row, down = 0, True
    for i in range(len(ciphertext)):
        fence[row][i] = '*'
        if down:
            if row == rails - 1:
                down = False
                row -= 1
            else:
                row += 1
        else:
            if row == 0:
                down = True
                row += 1
            else:
                row -= 1
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*':
                fence[i][j] = ciphertext[index]
                index += 1
    decrypted_text = []
    row, down = 0, True
    for i in range(len(ciphertext)):
        decrypted_text.append(fence[row][i])
        if down:
            if row == rails - 1:
                down = False
                row -= 1
            else:
                row += 1
        else:
            if row == 0:
                down = True
                row += 1
            else:
                row -= 1
    return ''.join(decrypted_text)


plaintext = "HELLO WORLD"
rails = 3
ciphertext = rail_fence_encrypt(plaintext, rails)
print("Ciphertext:", ciphertext)
decrypted_text = rail_fence_decrypt(ciphertext, rails)
print("Decrypted text:", decrypted_text)
