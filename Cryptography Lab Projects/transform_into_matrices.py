import numpy as np


def transform_into_matrices(char_list, key):
    key_2 = key[1:]
    fair = list(key_2)
    for i in char_list:
        if i not in fair:
            fair.append(i)
    arr = np.array(fair)
    update_diagram = arr.reshape(10, 9)

    return update_diagram
