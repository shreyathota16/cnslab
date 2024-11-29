#des

from Crypto.Cipher import DES 
from secrets import token_bytes 
def pad(text): 
	while len(text) % 8 != 0: 
 	text += ' ' 
 	return text 
def generate_key(): 
 	return token_bytes(8) 
def des_encrypt(plaintext, key): 
 	des = DES.new(key, DES.MODE_ECB)
	padded_text = pad(plaintext) 
	ciphertext = des.encrypt(padded_text.encode('utf-8')) 
	return ciphertext 
def des_decrypt(ciphertext, key): 
	des = DES.new(key, DES.MODE_ECB) 
	decrypted_text = des.decrypt(ciphertext).decode('utf-8').strip() 
	return decrypted_text 
key = generate_key() 
plaintext =input(" enter the plain text : ") 
ciphertext = des_encrypt(plaintext, key) 
print("Encrypted Text:", ciphertext) 
decrypted_text = des_decrypt(ciphertext, key) 
print("Decrypted Text:", decrypted_text)  

#blowfish

from Crypto.Cipher import Blowfish 
from Crypto.Util.Padding import pad, unpad 
from secrets import token_bytes 
def generate_key(): 
	return token_bytes(32) 
def blowfish_encrypt(plaintext, key): 
	cipher = Blowfish.new(key, Blowfish.MODE_CBC) 
	padded_text = pad(plaintext.encode('utf-8'), Blowfish.block_size) 
	ciphertext = cipher.encrypt(padded_text) 
	return cipher.iv, ciphertext 
def blowfish_decrypt(ciphertext, key, iv): 
	cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv) 
	decrypted_text = unpad(cipher.decrypt(ciphertext), 	Blowfish.block_size).decode('utf-8') 
	return decrypted_text 
key = generate_key() 
plaintext =input("enter plain text: ") 
iv, ciphertext = blowfish_encrypt(plaintext, key) 
print("Encrypted Text:", ciphertext) 
decrypted_text = blowfish_decrypt(ciphertext, key, iv) 
print("Decrypted Text:", decrypted_text)


#aes

from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad 
from secrets import token_bytes 
def generate_key(): 
	return token_bytes(32) 
def rijndael_encrypt(plaintext, key): 
	cipher = AES.new(key, AES.MODE_CBC) 
	padded_text = pad(plaintext.encode('utf-8'), AES.block_size) 
	ciphertext = cipher.encrypt(padded_text) 
	return cipher.iv, ciphertext 
def rijndael_decrypt(ciphertext, key, iv): 
	cipher = AES.new(key, AES.MODE_CBC, iv) 
	decrypted_text = unpad(cipher.decrypt(ciphertext), 	AES.block_size).decode('utf-8') 
	return decrypted_text 
key = generate_key() 
plaintext =input("enter plain text: ") 
iv, ciphertext = rijndael_encrypt(plaintext, key) 
print("Encrypted Text:", ciphertext) 
decrypted_text = rijndael_decrypt(ciphertext, key, iv) 
print("Decrypted Text:", decrypted_text) 
