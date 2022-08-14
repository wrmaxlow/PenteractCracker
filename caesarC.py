#Caesar Cipher brute force crack
def caesar(message):
	for key in range(len(message)):
		translated = ''
		for symbol in message:
			if symbol in message:
				num = message.find(symbol)
				num = num - key
				if num < 0:
					num = num + len(message)
					translated = translated + message[num]
				else:
					translated = translated + symbol
	print('Key #%s: %s' % (key, translated))