###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''
for char in plain_text:
    # read the character's code (use ord())
    code = ord(char)
    # add one to the character's code
    if 'a' <= char <= 'z':
        if char == 'z':
            code = ord('a')
        else:
            code += 1

    # uppercase letters
    elif 'A' <= char <= 'Z':
        if char == 'Z':
            code = ord('A')
        else:
            code += 1

    encrypted_char = chr(code)

    # add encrypted character to encrypted text
    encrypted_text += encrypted_char

print(plain_text)
print(encrypted_text)