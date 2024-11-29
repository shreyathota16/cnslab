#triple des

#execute in colab

#run
!pip install pycryptodome

#code
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
def generate_3des_key():
    return get_random_bytes(24)
def triple_des_encrypt(plaintext, key):
    cipher = DES3.new(key, DES3.MODE_CBC)
    iv = cipher.iv  
    padded_text = pad(plaintext.encode(), DES3.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return iv + ciphertext  
def triple_des_decrypt(ciphertext, key):
    iv = ciphertext[:DES3.block_size]
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext[DES3.block_size:])
    plaintext = unpad(padded_plaintext, DES3.block_size)  
    return plaintext.decode()  
plaintext = "Hello, Triple DES with pycryptodome!"
key = generate_3des_key()  
ciphertext = triple_des_encrypt(plaintext, key)
print("Ciphertext (hex):", ciphertext.hex())
decrypted_text = triple_des_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)