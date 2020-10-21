from enum import Enum

b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012346789+/"

def enum(**enums):
    return type('Enum', (), enums)

def hex_to_base64(hexdata):

    base64Final = []

    #Enumerate all possibilitys of bits padding
    take = enum(ZERO=0, TWO=2, FOUR=4)

    #Convert from hexadecimal to decimal
    decs = [ int(h, 16) for h in hexdata ]

    sextets = 0
    padding = take.ZERO

    for dec in decs:

        if padding == take.ZERO:
            sextets = dec
            padding = take.TWO

        elif padding == take.TWO:
            sextets = (sextets << 2) | (dec >> 2)
            base64Final.append( b64_table[sextets] )
            sextets = (dec & 0x03)
            padding = take.FOUR

        elif padding == take.FOUR:
            sextets = (sextets << 4) | dec
            base64Final.append( b64_table[sextets] )
            padding = take.ZERO

    if padding == take.TWO or padding == take.FOUR:

        base64Final.append( {
            take.TWO: lambda: f"{ b64_table[( sextets << 2) ]}="  ,
            take.FOUR: lambda: f"{ b64_table[ ( sextets << 4) ]}=="
        } [padding] ()
    )

    return "".join(base64Final)

def main_test():

    assert hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") ==\
    "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    print("Hex to base64  Cypotpals Accept")

if __name__ == '__main__':
    main_test()
