import Decryption_Algorithm
import transform_into_matrices
import unhide_key
import custom_char_list
import os

def decryption():
    char_list = custom_char_list.char_list
    print()
    file_path = input('Enter a file path: ')

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            cipher_text = f.read()

            print()
            print('Cipher Text : ', cipher_text)
            print()

            en_text, key = unhide_key.unhide(cipher_text)
            diagram = transform_into_matrices.transform_into_matrices(char_list, key)
            de_cipher_text = Decryption_Algorithm.decryption_algorithm(char_list, diagram, en_text, key)
            print("Plain Text",de_cipher_text)

            last_pos = 0
            for i in range(len(file_path)):
                if file_path[i] == '/':
                    last_pos = i

            print()
            path = file_path[:last_pos + 1]
            name = file_path[last_pos + 1:]
            name = 'de_' + name
            with open(path + name, 'w') as f:
                f.write(de_cipher_text)
                print('Decrypted File Saved Succesfull')

        f.close()
    else:
        print('The specified file does NOT exist')