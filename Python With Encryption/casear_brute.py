msg = input('Enter Encrypt Text:')
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(LETTERS)):
	translated = ''
	for symbol in msg:
		if symbol in LETTERS:
			num = LETTERS.find(symbol)
			num = num - key
			if num < 0:
				num = num + len(LETTERS)
			translated = translated + LETTERS[num]
		else:
			translated = translated + symbol
	print ('key ',key,':',translated)
	
