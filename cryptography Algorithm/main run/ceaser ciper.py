def encryption(plain_text, key):
    cipher = ''
    for x in plain_text:
        if x.isupper():
            char = ord(x) - ord('A')
            newChar = (char + key) % 26
            cipher = cipher + chr(newChar + ord('A'))

        if x.islower():
            char = ord(x) - ord('a')
            newChar = (char + key) % 26
            cipher = cipher + chr(newChar + ord('a'))

    return cipher


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

    return plain



msg = 'helloe'
key = 3
print("Encryption ->")
print(encryption(msg, key))
msg = 'khoorh'
key = 3
print("Encryption ->")
print(decryption(msg, key))