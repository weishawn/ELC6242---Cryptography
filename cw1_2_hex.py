from tkinter import N
from tools import *
import binascii
from operator import xor

xor_cipher_text = []

def read_hex(filename):
    with open(filename, 'rb') as f:
        hexdata = binascii.hexlify(f.read())
        return hexdata

def bytes_to_char(hex_data):
    char_array=[]
    for i in range(0,len(hex_data),2):
        num = int(hex_data[i:i+2],16)
        char_array.append(chr(num))
    return char_array

hex_encrypted_msg=read_hex("57.hex")
cipher_text = bytes_to_char(hex_encrypted_msg)
print(cipher_text)
print(len(cipher_text))

# for i in range(len(cipher_text)):
#     xor_cipher_text.append(chr(xor(ord(cipher_text[i]),0x2B)))

# print("key: 0x2B")
# print("Deciphered text using key length 1:")
# print(''.join(xor_cipher_text))
# xor_cipher_text = []

# for i in range(len(cipher_text)):
#     if (i % 2 == 0):
#         xor_cipher_text.append(chr(xor(ord(cipher_text[i]),0x2B)))
#     else:
#         xor_cipher_text.append('X')

# print("key: 0x2B")
# print("Deciphered text using key length 2:")
# print(''.join(xor_cipher_text))
# xor_cipher_text = []


# for i in range(len(cipher_text)):
#     if (i % 3 == 0):
#         xor_cipher_text.append(chr(xor(ord(cipher_text[i]),0x2B)))
#     else:
#         xor_cipher_text.append('X')
# print("key: 0x2B")
# print("Deciphered text using key length 3:")
# print(''.join(xor_cipher_text))
# print('')
# xor_cipher_text = []

# for i in range(len(cipher_text)):
#     if (i % 4 == 0):
#         xor_cipher_text.append(chr(xor(ord(cipher_text[i]),0x2B)))
#     else:
#         xor_cipher_text.append('X')
# print("key: 0x2B")
# print("Deciphered text using key length 4:")
# print(''.join(xor_cipher_text))


# two possible keys to decipher using XOR
for i in range(len(cipher_text)):
    if (i % 2 == 0):
        xor_cipher_text.append(chr(xor(ord(cipher_text[i]),0x2B)))
    else:
        xor_cipher_text.append(chr(xor(ord(cipher_text[i]),0x3A)))
print("key: 0x2B, 0x3A")
print("Deciphered text using key length 2:")
print(''.join(xor_cipher_text))
xor_cipher_text = []

for i in range(len(cipher_text)):
    if (i % 2 == 0):
        xor_cipher_text.append(chr(xor(ord(cipher_text[i]),0x2B)))
    else:
        xor_cipher_text.append(chr(xor(ord(cipher_text[i]),0x20)))
print("key: 0x2B, 0x20")
print("Deciphered text using key length 2:")
print(''.join(xor_cipher_text))
xor_cipher_text = []




