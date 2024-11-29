#simple columnar

def simple_columnar_encrypt(plaintext, key):
    num_cols = len(key)
    padded_plaintext = plaintext.ljust(
        (len(plaintext) + num_cols - 1) // num_cols * num_cols)
    columns = ['' for _ in range(num_cols)]
    for index, char in enumerate(padded_plaintext):
        columns[index % num_cols] += char
    sorted_columns = ''.join(
        [columns[key.index(str(i + 1))] for i in range(num_cols)])

    return sorted_columns


plaintext = "HELLO WORLD"
key = "3214"
ciphertext = simple_columnar_encrypt(plaintext, key)
print("Encrypted (Simple Columnar):", ciphertext)


def simple_columnar_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    columns = ['' for _ in range(num_cols)]
    start = 0
    for i in key_order:
        columns[i] = ciphertext[start:start + num_rows]
        start += num_rows
    plaintext = ''.join(''.join(columns[j][i] for j in range(num_cols))
                        for i in range(num_rows)).strip()

    return plaintext


decrypted_text = simple_columnar_decrypt(ciphertext, key)
print("Decrypted (Simple Columnar):", decrypted_text)
