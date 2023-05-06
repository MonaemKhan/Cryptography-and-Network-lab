import numpy as np


def insert_key(key):
    key_array = ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@',
                 '@', '@', '@', '@', '@']
    index = 0
    for x in key:
        if x == 'j':
            x = 'i'

        flag = True
        for i in key_array:
            if x == i:
                flag = False
        if flag:
            key_array[index] = str(x)
            index = index + 1
    return key_array, index


def diagram(array, index):
    for x in range(97, 123):
        x = chr(x)
        flag = True
        for i in array:
            if x == i:
                flag = False
        if x == 'j':
            flag = False

        if flag:
            array[index] = str(x)
            index = index + 1
    return array


def split_text(arr):
    text = ''
    for i in range(0, len(arr), 2):
        try:
            if arr[i] == arr[i + 1]:
                text = text + arr[i] + 'x' + arr[i + 1]
            else:
                text = text + arr[i] + arr[i + 1]
        except:
            text = text + arr[i]
    if len(text) % 2 != 0:
        text = text + 'x'
    return text


def encryption(plain_text, diagrams):
    cipher = ''
    for i in range(0, len(plain_text), 2):
        ch1 = plain_text[i]
        ch2 = plain_text[i + 1]
        if ch1 == 'j':
            ch1 = 'i'
        if ch2 == 'j':
            ch2 = 'i'

        row1 = np.where(diagrams == ch1)[0][0]
        col1 = np.where(diagrams == ch1)[1][0]
        row2 = np.where(diagrams == ch2)[0][0]
        col2 = np.where(diagrams == ch2)[1][0]

        if row1 == row2:
            if col1 + 1 > 4:
                ch11 = diagrams[row1][0]
            else:
                ch11 = diagrams[row1][col1 + 1]

            if col2 + 1 > 4:
                ch22 = diagrams[row2][0]
            else:
                ch22 = diagrams[row2][col2 + 1]

            cipher = cipher + ch11 + ch22

        elif col1 == col2:
            if row1 + 1 > 4:
                ch11 = diagrams[0][col1]
            else:
                ch11 = diagrams[row1 + 1][col1]

            if row2 + 1 > 4:
                ch22 = diagrams[0][col2]
            else:
                ch22 = diagrams[row2 + 1][col2]

            cipher = cipher + ch11 + ch22

        else:
            ch11 = diagrams[row1][col2]
            ch22 = diagrams[row2][col1]
            cipher = cipher + ch11 + ch22
    return cipher


def decryption(cipher_text, diagrams):
    plain = ''
    for i in range(0, len(cipher_text), 2):
        ch1 = cipher_text[i]
        ch2 = cipher_text[i + 1]
        row1 = np.where(diagrams == ch1)[0][0]
        col1 = np.where(diagrams == ch1)[1][0]
        row2 = np.where(diagrams == ch2)[0][0]
        col2 = np.where(diagrams == ch2)[1][0]

        if row1 == row2:
            if col1 - 1 < 0:
                ch11 = diagrams[row1][4]
            else:
                ch11 = diagrams[row1][col1 - 1]

            if col2 - 1 < 0:
                ch22 = diagrams[row2][4]
            else:
                ch22 = diagrams[row2][col2 - 1]

            plain = plain + ch11 + ch22

        elif col1 == col2:
            if row1 - 1 < 0:
                ch11 = diagrams[4][col1]
            else:
                ch11 = diagrams[row1 - 1][col1]

            if row2 - 1 < 0:
                ch22 = diagrams[4][col2]
            else:
                ch22 = diagrams[row2 - 1][col2]

            plain = plain + ch11 + ch22

        else:
            ch11 = diagrams[row1][col2]
            ch22 = diagrams[row2][col1]
            plain = plain + ch11 + ch22
    return plain


def decrypt_edit(plain):
    if plain[-1] == 'x':
        plain = plain[:-1]
    text = ''
    for i in range(len(plain)):
        if plain[i] == 'x':
            if plain[i - 1] != plain[i + 1]:
                text = text + plain[i]
        else:
            text = text + plain[i]
    return text

print("Encryption ->  helloe")
msg = "helloe"
key = "Monarchy"

array_key, index = insert_key(key.lower())

update_diagram = diagram(array_key, index)
arr = np.array(update_diagram)
update_diagram = arr.reshape(5, 5)

split_msg = split_text(msg.lower())

cipher_text = encryption(split_msg, update_diagram)
print('Encrypted Message : ', cipher_text)

plain_text = decryption(cipher_text,update_diagram)
print(plain_text)
plain_text = decrypt_edit(plain_text)
print("Decrypted Message : ",plain_text)