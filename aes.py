
#run
!pip install pycryptodome

#code
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
def main():
 message = "This is a confidential message"
 
 secret_key = get_random_bytes(16) # AES key size of 128 bits (16 bytes)
 
 cipher = AES.new(secret_key, AES.MODE_ECB)
 
 while len(message) % 16 != 0:
  message += ' '
 
 encrypted_message = cipher.encrypt(message.encode('utf-8'))
 
 encrypted_base64 = base64.b64encode(encrypted_message).decode('utf-8')
 
 print("Encrypted Message:", encrypted_base64)
 
 cipher = AES.new(secret_key, AES.MODE_ECB)
 
 decrypted_message = cipher.decrypt(base64.b64decode(encrypted_base64)).decode('utf-8').strip()
 print("Decrypted Message:", decrypted_message)
if __name__ == "__main__":
 main()