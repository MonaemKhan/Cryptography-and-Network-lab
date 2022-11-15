def decryption(cipher_text, key):
    plain = ''
    for x in cipher_text:
        if x.isupper():
            char = ord(x) - ord('A')
            newChar = (char - key) % 26
            plain = plain + chr(newChar + ord('A'))

        if x.islower():
            char = ord(x) - ord('a')
            newChar = (char - key) % 26
            plain = plain + chr(newChar + ord('a'))
        if x == ' ':
            plain = plain + ' '
    return plain

if __name__ ==  '__main__':
    msg =  input('Encrypted Message : ')
    key = (int) (input('Enter Key: '))
    print("Decrypted : ",end="")
    print(decryption(msg, key))