
#run
!pip install pycryptodome

#code
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
import base64
def main():
 message = "This is a confidential message"

 secret_key = get_random_bytes(16)

 cipher = Blowfish.new(secret_key, Blowfish.MODE_ECB)

 while len(message) % 8 != 0:
    message += ' '
 encrypted_message = cipher.encrypt(message.encode('utf-8'))

 encrypted_base64 = base64.b64encode(encrypted_message).decode('utf-8')
 print("Encrypted Message:", encrypted_base64)

 cipher = Blowfish.new(secret_key, Blowfish.MODE_ECB)

 decrypted_message = cipher.decrypt(base64.b64decode(encrypted_base64)).decode('utf-8').strip()
 print("Decrypted Message:", decrypted_message)
if __name__ == "__main__":
 main()