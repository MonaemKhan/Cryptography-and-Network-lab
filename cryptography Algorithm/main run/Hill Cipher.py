import numpy as np

#for finding multiplicative inverse
def multiplicative_inverse(e):
    for i in range(1,e+1):
        mod = (i*e)%26
        if mod == 1:
            break
    return i

#find inverse matrix
def find_inverse(arr):
    det = np.linalg.det(arr)
    inv = multiplicative_inverse(int(det)%26)
    cof = np.linalg.inv(arr) * det
    cof  = np.rint(cof)
    cof = cof.astype(int)%26
    return (inv*cof)%26

#for encryption message
def encryption(msg,arr):
    cipher = ''
    for i in range(0,len(msg),3):
        c1 = ord(msg[i])-97
        c2 = ord(msg[i+1])-97
        c3 = ord(msg[i+2])-97
        msg_arr = [c1,c2,c3]
        ci = np.dot(msg_arr,arr)%26
        for j in ci:
            cipher = cipher+ chr(j+97)
    return cipher

#for decryption message
def decryption(msg,arr):
    plain = ''
    inv_arr = find_inverse(arr)
    for i in range(0,len(msg),3):
        p1 = ord(msg[i])-97
        p2 = ord(msg[i+1])-97
        p3 = ord(msg[i+2])-97
        msg_arr = [p1,p2,p3]
        pl = np.dot(msg_arr,inv_arr)%26
        for j in pl:
            plain = plain+ chr(j+97)
    return plain

##### __main__#####
# n  = int (input('Define your matrix size : '))
n=3
arr = np.zeros((n,n)).astype(int)

#message
# msg = input('Enter your message : ')
msg = 'paymoremoney'
if len(msg)%n !=0:
    for i in range(n-(len(msg)%n)):
        msg = msg+'x'

#key
# key = input('Enter Key (as text) : ')
key = 'rrfvsvcct'
while(len(key) != n*n):
    key = input('Enter Key again : ')

#update array value with key
k = 0
for i in range(n):
    for j in range(n):
        arr[i][j] = ord(key[k])-97
        k = k+1

cipher = encryption(msg,arr)
print("Cipher text : "+cipher)

plain = decryption(cipher,arr)
print('Plain msg : '+plain)