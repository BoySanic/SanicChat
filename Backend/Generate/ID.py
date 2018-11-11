#! /usr/bin/python3
import random
import binascii
import time
import math
import hashlib
import binascii
import string

def generate_id():
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	thing = ''.join(random.choice(chars) for _ in range(64))
	m = hashlib.md5()
	m.update(thing.encode())
	m.digest()
	return m.hexdigest()

print(generate_id())