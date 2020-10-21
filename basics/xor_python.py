def hex_xor(buffer1, buffer2):

    assert len(buffer1) == len(buffer2)
    return hex( int(buffer1, 16) ^ int(buffer2, 16))[2:]

def main_test():
    assert hex_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965') ==\
            '746865206b696420646f6e277420706c6179'

    print("Xor Cypotpals Accept")

if __name__ == '__main__':
    main_test()
