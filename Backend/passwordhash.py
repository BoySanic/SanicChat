#! /usr/bin/python3
import hashlib
import secrets
import string
import binascii

def pbkdf2_hmac(message, salt):
	iterations = 1000000
	hashed = hashlib.pbkdf2_hmac('sha512', str.encode(message), str.encode(salt), iterations)
	return hashed
def getSalt(size):
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	return ''.join(secrets.choice(chars) for _ in range(size))

pw = "test"
salt = getSalt(64)
#saltedpw = pw + salt
#m = sha256(saltedpw)
#print(m.hexdigest())
#print(salt)
hashed = pbkdf2_hmac(pw, salt)
print(binascii.hexlify(hashed))