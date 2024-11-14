import hashlib

data = "Hello, world!"
md5_hash = hashlib.md5(data.encode())
hash_hex = md5_hash.hexdigest()
print("MD5 hash:", hash_hex)
