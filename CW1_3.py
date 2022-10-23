import math
from itertools import count, permutations
from pip import main
from collections import Counter
from tools import *

# function is obtained and modified from https://www.geeksforgeeks.org/columnar-transposition-cipher/
def decrypt(cipher, key):
    message = ""
    key_index = 0
    msg_index = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    #column
    col = len(key)
    #row
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
  
    # Arrange the matrix column wise according 
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[key_index])
  
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_index]
            msg_index += 1
        key_index += 1
  
    # convert decrypted msg matrix into a string
    try:
        message = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
  
    null_count = message.count('_')
  
    if null_count > 0:
        return message[: -null_count]
  
    return message
  
def main():
    cipher_text = "ekatebrteigDegslnbsneoimsnormuidifatoraolfonpnenoeuapndanmiyoueantltismutflthsikohlehsns"
    key = "bfgcdahe"
    decrypted_message = []
    # using list comprehension
    msg = decrypt(cipher_text, key)
    decrypted_message.append(msg)
    print(decrypted_message)

if __name__ == "__main__":
    main()