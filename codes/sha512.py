import hashlib

api_key = "sk-..."
hash_key = hashlib.sha512(api_key.encode())
hex_dig = hash_key.hexdigest()

print(hex_dig)

with open("../config/hash_api_key", "w") as fw:
    fw.write(hex_dig)

with open("../config/hash_api_key", "r") as fr:
    str = fr.readline()

print(str)


