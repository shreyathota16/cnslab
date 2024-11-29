#run
!pip install pycryptodome

#code
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
def pad(text):
 while len(text) % 8 != 0:
    text += ' '
 return text
def main():
 message = "This is a confidential message."
 message = pad(message)
 my_message = message.encode('utf-8')

 my_des_key = get_random_bytes(8)

 my_cipher = DES.new(my_des_key, DES.MODE_ECB)

 my_encrypted_bytes = my_cipher.encrypt(my_message)

 my_cipher = DES.new(my_des_key, DES.MODE_ECB)

 my_decrypted_bytes = my_cipher.decrypt(my_encrypted_bytes)

 encrypted_data = my_encrypted_bytes
 decrypted_data = my_decrypted_bytes.decode('utf-8').strip()

 print("Message: ", message.strip())
 print("Encrypted (in bytes): ", encrypted_data)
 print("Decrypted Message: ", decrypted_data)
if __name__ == "__main__":
 main()