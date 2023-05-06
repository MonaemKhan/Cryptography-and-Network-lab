import random

#random key generator
def random_key_generator(length):
    key = ""
    for i in range(len(msg)):
        key = key+ chr(random.randint(0,25)+97)
    return key

#xor operation
def xor_operation(msg,key):
    xor_str = ''
    for i in range(len(msg)):
        xor_num = (ord(msg[i]))^(ord(key[i]))
        xor_str = xor_str + chr(xor_num)
    return xor_str

#main program start

# msg = 'monaem'
msg = input('Enter your plain text : ')

key  =  random_key_generator(len(msg))

# #in case of manual key
# key = input('Enter key : ')
# while len(msg) != len(key):
#     if len(msg) > len(key):
#         key = key+key
#     else:
#         key = key[:len(msg)]

print('Key : '+key)

cipher =  xor_operation(msg,key)
print("Cipher Text : "+cipher)

plain =  xor_operation(cipher,key)
print('Plain Text : '+plain)