import string
import numpy as np

main = string.ascii_lowercase


def generate_key():
    key = [[0 for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            x = int(input())
            key[i][j] = x
    return key

def modInverse(a, m):
    a = a % m;
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1


def method(a, m):
    if (a > 0):
        return (a % m)
    else:
        k = (abs(a) // m) + 1
    return method(a + k * m, m)


def message_matrix(s, n):
    s = s.replace(" ", "")
    s = s.lower()
    final_matrix = []
    if (len(s) % n != 0):
        for i in range(abs(len(s) % n)):
            s = s + 'z'
    for k in range(len(s) // n):
        message_matrix = []
        for i in range(n):
            sub = []
            for j in range(1):
                sub.append(ord(s[i + (n * k)]) - ord('a'))
            message_matrix.append(sub)
        final_matrix.append(message_matrix)
    return (final_matrix)


def multiply_and_convert(key, message):
    res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]

    for i in range(len(key)):
        for j in range(len(message[0])):
            for k in range(len(message)):
                res_num[i][j] += key[i][k] * message[k][j]

    res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
    for i in range(len(key)):
        for j in range(len(message[0])):
            res_alpha[i][j] += chr((res_num[i][j] % 26) + 97)

    return (res_alpha)

print("Enter 3x3 matrix for key (It should be inversible):")
n = 3
key_matrix = generate_key()
A = np.array(key_matrix)
det = np.linalg.det(A)
adjoint = det * np.linalg.inv(A)

if (det != 0):
    convert_det = modInverse(int(det), 26)
    adjoint = adjoint.tolist()

    for i in range(len(adjoint)):
        for j in range(len(adjoint[i])):
            adjoint[i][j] = round(adjoint[i][j])
            adjoint[i][j] = method(adjoint[i][j], 26)

    adjoint = np.array(adjoint)
    inverse = convert_det * adjoint

    inverse = inverse.tolist()
    for i in range(len(inverse)):
        for j in range(len(inverse[i])):
            inverse[i][j] = inverse[i][j] % 26

    print("Inverse matrix: ")
    for i in inverse:
        print(i)

    cipher_text = input("Enter the cipher text: ")
    message = message_matrix(cipher_text, n)
    plain_text = ''
    for i in message:
        sub = multiply_and_convert(inverse, i)
        for j in sub:
            for k in j:
                plain_text += k

    print("plain message: ", plain_text)
else:
    print("Matrix cannot be inverted")