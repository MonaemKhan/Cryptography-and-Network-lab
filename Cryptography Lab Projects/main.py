import Encryption
import Decryption
import os

if __name__ == '__main__':
    i = 1;

    while i == 1:
        print("1. File Encryption\n2. File Decryption")
        try:
            choise = int(input("Enter Your Preference : "))
        except:
            break
        if choise == 1:
            Encryption.encryption()
        else:
            Decryption.decryption()
        try:
            i = int(input('Do You Want to Continue[yes(1)/no(0)/any key to quite] : '))
        except:
            break
    print()
    print("Thank You")



