import random

#generate key
def key_gerator(phi_n):
    while(True):
        e = random.randint(1,phi_n)
        if isPrime(e):
            d = multiplicative_inverse(e,phi_n)
            if d!=e:
                break
    return e,d

#check for prime number
def isPrime(n):
    if(n==1 or n==0):
        return False
    for i in range(2,int(n**(1/2))+1):
        if(n%i==0):
            return False
    return True

#do multiplicative inverse
def multiplicative_inverse(e,phi_n):
    for i in range(1,e+1):
        mod = (i*e)%phi_n
        if mod == 1:
            break
    return i

#encryption process
def encrypt(msg,key,n):
    up_msg = msg**key%n
    return up_msg

#decryption process
def decrypt(msg,key,n):
    up_msg = msg**key%n
    return up_msg

#take input from user and calculate value
print('Enter two prime number p & q such that their product will grater than your total alphabet size')
size = int(input('Enter Total Alphabate Size : '))

while (True):
    while (True):
        p = int(input('Enter a prime number p : '))
        if isPrime(p):
            break
        else:
            print('Not a prime Number')

    while (True):
        q = int(input('Enter a prime number q : '))
        if p == q:
            print('Both can not be same')
        elif isPrime(q):
            break
        else:
            print('Not a prime Number')
    n = p * q
    if n > size:
        break
    else:
        print('your input prime numbers are less than your alphabet size')

phi_n = (p - 1) * (q - 1)

public_key, private_key = key_gerator(phi_n)
print('Public key is : '+str (public_key))
print('Private key is : '+str (private_key))

#input plain text and convert to cipher
plain_text = input('Message for encryption : ')
plain_text = plain_text.lower()
chipher = ''
for char in plain_text:
    msg = ord(char)-97
    chipher_char = encrypt(msg,public_key,n)
    chipher = chipher + chr(chipher_char+97)
print("Cipher Text : "+chipher)

#covert to plain
plain = ''
for char in chipher:
    msg = ord(char)-97
    plain_char = decrypt(msg,private_key,n)
    plain = plain + chr(plain_char+97)
print("Plain Text : "+plain)