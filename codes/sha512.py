# import hashlib

# api_key = "sk-..."
# hash_key = hashlib.sha512(api_key.encode())
# hex_dig = hash_key.hexdigest()

# print(hex_dig)

# with open("../config/hash_api_key", "w") as fw:
#     fw.write(hex_dig)

# with open("../config/hash_api_key", "r") as fr:
#     str = fr.readline()

# print(str)

with open("../dataset/판례/광주지법 2000. 5. 19. 선고 2000노24 판결 _ 상고기각.pdf", "r", encoding="utf-8") as fr:
    print(fr.readlines())


