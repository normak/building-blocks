def cipher (content, shift):
  encrypted = ""
  for char in content:
    if (ord(char) >= 65 and ord(char) <= 90):
      if ((ord(char) + shift) > 90):
        encrypted += chr(64 + ((ord(char) + shift) % 90))
      else:
        encrypted += chr(ord(char) + shift)
    elif (ord(char) >= 97 and ord(char) <= 122):
      if ((ord(char) + shift) > 122):
        encrypted += chr(96 + ((ord(char) + shift) % 122))
      else:
        encrypted += chr(ord(char) + shift)
    else:
      encrypted += char

  return encrypted


content = str(input("Enter a phrase that you'd like to encrypt: "))
shift = int(input("Enter the shift you'd like to use: "))

print(cipher(content,shift))