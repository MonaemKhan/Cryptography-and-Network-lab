def hide(message,key):
    length = int(len(message)/2)
    part_1 =  message[:length]
    part_2 = message[length:]
    hiden_msg = key[10:] + part_1 + key[:6] + part_2 + key[6:10]
    return hiden_msg