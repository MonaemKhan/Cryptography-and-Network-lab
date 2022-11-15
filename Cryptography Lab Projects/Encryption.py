import key_generator
import transform_into_matrices
import Encryption_Algorithm
import hide_key
import custom_char_list
import os

def encryption():
    char_list = custom_char_list.char_list
    
    key = key_generator.key_generator()
    print()
    print('Key : ',key)
    print()

    diagram = transform_into_matrices.transform_into_matrices(char_list,key)

    file_path = input('Enter a file path: ')

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            plain_text = f.read()

            print()
            print('Plain Text :\n',plain_text)
            print()

            en_plain_text = Encryption_Algorithm.encryption_algorithm(char_list, diagram, plain_text, key)
            print("Encrypted Text :\n", en_plain_text)
            print()

            hiden_msg = hide_key.hide(en_plain_text, key)
            print("Main Cipher Text :\n", hiden_msg)

            last_pos = 0
            for i in range(len(file_path)):
                if file_path[i] == '/':
                    last_pos = i

            print()
            path = file_path[:last_pos + 1]
            name = file_path[last_pos + 1:]
            name = 'en_' + name
            with open(path + name, 'w') as f:
                f.write(hiden_msg)
                print('Encrypted File Saved Succesfull')
                print()
        f.close()
    else:
        print('The specified file does NOT exist')