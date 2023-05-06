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


decision = True
while decision:
    print('What Do You Want?\n1. Encrypt a msg \n2. Decrypt a msg')
    choice = int(input())

    while choice > 2:
        print('........Warning!!!!!!')
        print("Please!!! Enter number between 1 and 2")
        choice = int(input())

    msg = input("Message : ")
    key = int(input("Key : "))

    if choice == 1:
        print("Encryption ->")
        print(encryption(msg, key))
    else:
        print("Decryption ->")
        print(decryption(msg, key))

    popup = input("Do you want to continue?(y/n): ")
    popup = popup.lower()
    while popup != 'y' and popup != 'n':
        popup = input("Do you want to continue?(y/n)")
        popup = popup.lower()

    if popup == 'y':
        decision = True
    else:
        decision = False

print("Thank You")