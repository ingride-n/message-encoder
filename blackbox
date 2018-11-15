
import sys
import random

# List position values in random order (max 50)

def random_gen():
	K=[i for i in range(50)]
	random.shuffle(K)
	return K

# Create message key based on randomized positions

def key_gen(K, msg):
	key=''
	msg = msg.upper().replace(' ','')
	for i in range(len(msg)):
		key += '.'+str(K[i])
	return key

# Encode a message

def scramble(K, msg):
	X = []
	result = ''
	msg = msg.upper().replace(' ','')

	for i in range(50):
		X.append('#')

	for i in range(len(msg)):
		X[K[i]]=msg[i]

	for i in range(50):
		result += X[i]

	return result

# Decode a message

def unscramble(msg, key):
	K = key.split('.')
	K.pop(0)
	result=''
	for i in range(len(K)):
		result += msg[int(K[i])]
	return result
