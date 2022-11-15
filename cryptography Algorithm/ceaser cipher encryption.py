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
        if x == ' ':
            cipher = cipher + ' '
    return cipher


if __name__ ==  '__main__':
    msg =  input('Massage: ')
    key = (int) (input('Enter Key: '))
    print("Encrypted : ",end="")
    print(encryption(msg, key))
