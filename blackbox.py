
import sys
import random


# Create key based on randomized positions

def get_key(msg):
	K=[i for i in range(50)]
	random.shuffle(K)
	key=''
	msg = msg.replace(' ','')
	for i in range(len(msg)):
		key += '.'+str(K[i])
	return key

# Encode a message

def scramble(msg, key):
	X = []
	result = ''
	msg = msg.upper().replace(' ','')
	
	K= key.split('.')
	K.pop(0)

	for i in range(50):
		X.append('#')

	for i in range(len(msg)):
		X[K[i]]=msg[i]

	for i in range(50):
		result += X[i]

	return result

# Decode a message

def unscramble(msg, key):
	K= key.split('.')
	K.pop(0)
	result=''
	for i in range(len(K)):
		result += msg[int(K[i])]
	return result
