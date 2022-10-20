import os, binascii
from hashlib import pbkdf2_hmac

password = b"super secret password"
salt = binascii.unhexlify('aaef1654ac')
hashed = pbkdf2_hmac("sha256", password, salt, 1000)
print(binascii.hexlify(hashed))
print(hashed)