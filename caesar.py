class CaesarCipher:
 @staticmethod
 def encrypt(plaintext, key):
    encrypted_text = []
    for c in plaintext:
        shifted_char = chr(ord(c) + key)
        encrypted_text.append(shifted_char)
    return ''.join(encrypted_text)
 @staticmethod
 def decrypt(encrypted_text, key):
    decrypted_text = []
    for c in encrypted_text:
        shifted_char = chr(ord(c) - key)
        decrypted_text.append(shifted_char)
    return ''.join(decrypted_text)
if __name__ == "__main__":
 plaintext = "ABC"
 key = 3
 encrypted_text = CaesarCipher.encrypt(plaintext, key)
 print("Encrypted Text:", encrypted_text)
 decrypted_text = CaesarCipher.decrypt(encrypted_text, key)
 print("Decrypted Text:", decrypted_text)