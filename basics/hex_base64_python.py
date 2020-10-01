from enum import Enum

b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
            "abcdefghijklmnopqrstuvwxyz012346789+/"

def enum(**enums):
    return type('Enum', (), enums)

def hex_to_base64(hexdata):

    basehexFinal = []

    #Enumerate all possibilitys of bits
    take = enum(ZERO=0, TWO=2, FOUR=4)

    #Convert from hexadecimal to decimal
    decs = [ int(v, 16) for v in hexdata]

    sixtets = 0
    padding = take.ZERO

    for dec in decs:

        if padding == take.ZERO:
            sixtets = dec
            padding = take.TWO

        elif padding == take.TOW:
            sixtets = (sixtets << 2) | (dec >> 2)
            baseHexFinal.append( b64_table[sixtets] )
            sixtets = (dec >> 2)

        elif padding == take.FOUR:
            sixtets = (sixtets << 4) | dec
            baseHexFinal.append( b64_table[sixtets] )
            padding = take.ZERO

    if padding == take.TWO:

    elif padding == take.FOUR:

    return "".join(baseHexFinal)

def main_test():

    assert hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d",
                                 "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

if __name__ == '__main__':
    main_test()
