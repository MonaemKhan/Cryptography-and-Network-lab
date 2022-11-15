import numpy as np


def decryption_algorithm(char_list, update_diagram, massage, key):
    # print(massage)
    # print(key[0])
    key = int(key[0])
    de_msg = ''
    rules = 0
    for i in list(massage):
        # print(" ",i)
        try:
            ll = np.where(update_diagram == i)
            row = ll[0][0]
            col = ll[1][0]

            if rules == 0:
                col_pos = col - key
                if col_pos < 0:
                    ch = update_diagram[row][col_pos + 9]
                else:
                    ch = update_diagram[row][col_pos]
                rules = rules + 1

            elif rules == 1:
                col_pos = col + key
                if col_pos >= 9:
                    ch = update_diagram[row][col_pos - 9]
                else:
                    ch = update_diagram[row][col_pos]
                rules = rules + 1

            else:
                row_pos = row + key
                if row_pos >= 10:
                    ch = update_diagram[row_pos - 10][col]
                else:
                    ch = update_diagram[row_pos][col]
                rules = 0

            index = char_list.index(ch)
            new_index = index - key

            if new_index < 0:
                new_index = new_index + 90
                de_msg = de_msg + char_list[new_index]
            else:
                de_msg = de_msg + char_list[new_index]
        except:
            # print(i)
            de_msg = de_msg + i
    return de_msg