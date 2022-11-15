def unhide(msg):
    length = int((len(msg)-16)/2)

    key_last_part = msg[:6]

    extended_length = 6 + length
    msg_part_1 = msg[6:extended_length]

    key_first_part = msg[extended_length:(extended_length + 6)]
    extended_length= extended_length + 6

    last_length = ((len(msg) - 4))
    key_mid_part = msg[last_length:]

    msg_part_2 = msg[extended_length:last_length]

    message = msg_part_1+msg_part_2
    key = key_first_part+key_mid_part+key_last_part

    return message,key
