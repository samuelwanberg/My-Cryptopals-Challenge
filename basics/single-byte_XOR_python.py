from collections import Counter

english_freq = {
    'a': 8.2389258, 'b': 1.5051398, 'c': 2.8065007, 'd': 4.2904556,
    'e': 12.813865, 'f': 2.2476217, 'g': 2.0327458, 'h': 6.1476691,
    'i': 6.1476691, 'j': 0.1543474, 'k': 0.7787989, 'l': 4.0604477,
    'm': 2.4271893, 'n': 6.8084376, 'o': 7.5731132, 'p': 1.9459884,
    'q': 0.0958366, 'v': 0.9866131, 'w': 2.3807842, 'x': 0.1513210,
    'y': 1.9913847, 'z': 0.0746517
}

def calc_freq_quotient(cipher: bytes):

    c =  Counter(cipher)

    cipher_freq = { letter : ( c.get(ord(letter), 0) * 100 ) / len(cipher)
               for letter in english_freq.keys() }

    all_letters = english_freq.keys()
    fq_calc = lambda fa,fb: abs(fa - fb)

    return sum([ fq_calc( english_freq[letter], cipher_freq[letter] )
                 for letter in all_letters ]) / len(all_letters)


def single_byte_xor(text: bytes, key: int) -> bytes:
    return bytes([ b ^ key  for b in text])

def single_bruteforce_decrypt(chipher: bytes) -> float:
    all_decrypt = []

    for key in range(256):
        #print(f"{key} -> {single_byte_xor(chipher, key).decode()}\n\n" )
        all_decrypt.append( single_byte_xor(chipher, key) )

    return all_decrypt

def decrypt_message(cipher: bytes) -> bytes:

    messages = single_bruteforce_decrypt(cipher)
    frequencies = [ calc_freq_quotient(msg) for msg in messages ]

    index = frequencies.index(min(frequencies))

    return messages[index]

def main_test():

    chipher = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    print(f"{decrypt_message(chipher)}\n\n" )


if __name__ == '__main__':
    main_test()
