import string

main = string.ascii_lowercase


def generate_key():
    key = [[0 for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            x = int(input())
            key[i][j] = x
    return key

def message_matrix(s, n):
    s = s.replace(" ", "")
    s = s.lower()
    final_matrix = []
    if (len(s) % n != 0):
        while (len(s) % n != 0):
            s = s + 'x'
    for k in range(len(s) // n):
        message_matrix = []
        for i in range(n):
            sub = []
            for j in range(1):
                sub.append(ord(s[i + (n * k)]) - ord('a'))
            message_matrix.append(sub)
        final_matrix.append(message_matrix)
    return (final_matrix)

def getCofactor(mat, temp, p, q, n):
    i = 0
    j = 0
    for row in range(n):
        for col in range(n):
            if (row != p and col != q):
                temp[i][j] = mat[row][col]
                j += 1
                if (j == n - 1):
                    j = 0
                    i += 1

def determinantOfMatrix(mat, n):
    D = 0
    if (n == 1):
        return mat[0][0]
    temp = [[0 for x in range(n)]
            for y in range(n)]

    sign = 1

    for f in range(n):
        getCofactor(mat, temp, 0, f, n)
        D += (sign * mat[0][f] *
              determinantOfMatrix(temp, n - 1))
        sign = -sign
    return D


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
key = generate_key()

plain_text = input("Enter the message: ")
message = message_matrix(plain_text, n)
final_message = ''
for i in message:
    sub = multiply_and_convert(key, i)
    for j in sub:
        for k in j:
            final_message += k
print("encrypted message: ", final_message)