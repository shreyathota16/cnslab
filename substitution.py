class SubCipher:
 @staticmethod
 def encrypt(plaintext, key):
    encrypted_text = []
    for i in range(len(plaintext)):
        shifted_char = chr(ord(plaintext[i]) + key[i])
        encrypted_text.append(shifted_char)
    return ''.join(encrypted_text)
 @staticmethod
 def decrypt(encrypted_text, key):
    decrypted_text = []
    for i in range(len(encrypted_text)):
        shifted_char = chr(ord(encrypted_text[i]) - key[i])
        decrypted_text.append(shifted_char)
    return ''.join(decrypted_text)
if __name__ == "__main__":
 plaintext = "ABC"
 key = [1, 3, 5]
 encrypted_text = SubCipher.encrypt(plaintext, key)
 print("Encrypted Text:", encrypted_text)
 decrypted_text = SubCipher.decrypt(encrypted_text, key)
 print("Decrypted Text:", decrypted_text)