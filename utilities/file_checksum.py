""" 校验下载文件 """


import hashlib


BLOCK = 1024
hash_sum = ""
path = ""
m = hashlib.sha256()
with open(path, 'rb') as f:
    while True:
        segment = f.read(BLOCK)
        if not segment:
            break

        m.update(segment)

print(m.hexdigest() == hash_sum)
