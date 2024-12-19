from random import randint

def dynamic_xor_decrypt(enc, text_key="trudeau"):
    decoded_text = ""
    key_length = len(text_key)
    for i, char in enumerate(enc):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decoded_text += decrypted_char
    return decoded_text[::-1]

def decrypt(enc, key):
    val = []
    for num in enc:
        val.append(chr(int(num/(key*311))))

    return ''.join(val)


def generator(g, x, p):
    return pow(g, x) % p

def main(cipher,a,b):
    p = 97
    g = 31
    
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)

    shared_key = key
    semi_dec = decrypt(cipher, shared_key)
    val = dynamic_xor_decrypt(semi_dec)
    
    print(f'FLAG is: {val}')
  
cipher = [151146, 1158786, 1276344, 1360314, 1427490, 1377108, 1074816, 1074816, 386262, 705348, 0, 1393902, 352674, 83970, 1141992, 0, 369468, 1444284, 16794, 1041228, 403056, 453438, 100764, 100764, 285498, 100764, 436644, 856494, 537408, 822906, 436644, 117558, 201528, 285498]
main(cipher,97,22)

""" out file
a = 97
b = 22
cipher is: [151146, 1158786, 1276344, 1360314, 1427490, 1377108, 1074816, 1074816, 386262, 705348, 0, 1393902, 352674, 83970, 1141992, 0, 369468, 1444284, 16794, 1041228, 403056, 453438, 100764, 100764, 285498, 100764, 436644, 856494, 537408, 822906, 436644, 117558, 201528, 285498]
"""
