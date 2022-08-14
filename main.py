#imports
from prints import *
from aesC import aes
from affineC import affine
from base64C import b64
from binaryC import binary
from caesarC import caesar
from desC import des
from desC import des3
from reverseC import reverse
from transpositionC import transposition
from viginereC import viginere

def runCiphers(message):
	affine(message)
	caesar(message)
	reverse(message)
	transposition(message)
	viginere(message)

def runKeys(message):
	aes(message)
	b64(message)
	binary(message)
	des(message)
	des3(message)
	
#Prints the early part of the code from prints.py
beginning()

#Takes input and creates 2 space lines after, space in prints.py
encrypted = input()
space()

#Prints optiontext from prints.py, sets option as user input, and space from prints.py
optiontext()
option = input()
space()

if option == "1":
	#All ciphers and keys to file
	quit

elif option == "2":
	#All ciphers
	quit

elif option == "3":
	#All keys
	quit

else:
	print("An unacceptable input was given. Please restart the program and give a proper option")
	quit
