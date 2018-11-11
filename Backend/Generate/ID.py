#! /usr/bin/python3
import random
import binascii
import time
import math
import hashlib
import binascii
import string
#def generate_id(count):
#	
#	unixtime = time.time()
#	truncated = math.floor(unixtime)
#	fullid = "" + str(bin(truncated)[2:]) + str(bin(random.randrange(6, 8))[2:]) + str(bin(count)[2:])
#	fullid2 = fullid[::-1]
#	intid = int(fullid2, 2)
#	return intid	
def generate_id():
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	thing = ''.join(random.choice(chars) for _ in range(64))
	m = hashlib.md5()
	m.update(thing.encode())
	m.digest()
	return m.hexdigest()

print(generate_id())