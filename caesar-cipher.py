#A basic implementation of caesar's cipher

def cipher(content, shift):
	encrypted = ''
	for char in content:
		if (char != ' '):
			encrypted += str(unichr(ord(char) + shift))
		else:
			encrypted += ' '
	return encrypted

content = str(raw_input("Enter a phrase that you'd like to encrypt: "))
shift = int(raw_input("Enter the shift you'd like to use: "))

print cipher(content, shift)