#! /usr/bin/python3
import hashlib
import secrets
import string
def sha256(message):
	m = hashlib.sha256()
	m.update(str.encode(message))
	return m
def getSalt(size):
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	return ''.join(secrets.choice(chars) for _ in range(size))

pw = "test"
salt = getSalt(14)
saltedpw = pw + salt
m = sha256(saltedpw)