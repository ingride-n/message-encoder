
import sys
import random


# Create key based on randomized positions (max 50 characters)

def create_key(msg):
	K=[i for i in range(50)]
	random.shuffle(K)
	key=''
	msg = msg.replace(' ','')
	for i in range(len(msg)):
		key += '.'+str(K[i])
	return key

# Encode a message

def encode(msg, key):
	X = []  # Array for chars of the encoded message
	result = ''
	msg = msg.upper().replace(' ','')
	K= key.split('.')
	K.pop(0)
	for i in range(50):
		X.append('#')
	for i in range(len(msg)):
		X[int(K[i])]=msg[i]  # Encode to a new position
	for i in range(50):
		result += X[i] # Create string
	return result

# Decode a message

def decode(msg, key):
	K= key.split('.')
	K.pop(0)
	result=''
	for i in range(len(K)):
		result += msg[int(K[i])]
	return result

