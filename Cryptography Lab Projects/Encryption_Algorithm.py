import numpy as np


def encryption_algorithm(char_list, update_diagram, massage, key):
    key = int(key[0])
    en_msg = ''
    rules = 0
    for i in list(massage):
        #     print(" ",i)
        try:
            index = char_list.index(i)
            new_index = index + key
            if new_index >= 90:
                new_index = new_index - 90
                ch = char_list[new_index]
            else:
                ch = char_list[new_index]
            #         print(ch)

            ll = np.where(update_diagram == ch)
            row = ll[0][0]
            col = ll[1][0]
            #         print(row," ",col)

            if rules == 0:
                col_pos = col + key
                if col_pos >= 9:
                    #                 print(row," ",col_pos-9)
                    #                 print(update_diagram[row][col_pos-9])
                    en_msg = en_msg + update_diagram[row][col_pos - 9]
                else:
                    #                 print(row," ",col+key_1)
                    #                 print(update_diagram[row][col_pos])
                    en_msg = en_msg + update_diagram[row][col_pos]
                rules = rules + 1

            elif rules == 1:
                col_pos = col - key
                if col_pos < 0:
                    #                 print(row," ",col_pos+9)
                    #                 print(update_diagram[row][col_pos+9])
                    en_msg = en_msg + update_diagram[row][col_pos + 9]
                else:
                    #                 print(row," ",col-key_1)
                    #                 print(update_diagram[row][col_pos])
                    en_msg = en_msg + update_diagram[row][col_pos]
                rules = rules + 1

            else:
                row_pos = row - key
                if row_pos < 0:
                    #                 print(row_pos+10," ",col)
                    #                 print(update_diagram[row_pos+10][col])
                    en_msg = en_msg + update_diagram[row_pos + 10][col]
                else:
                    #                 print(row_pos," ",col)
                    #                 print(update_diagram[row_pos][col])
                    en_msg = en_msg + update_diagram[row_pos][col]
                rules = 0
        except:
            #         print(i)
            en_msg = en_msg + i
    return en_msg
