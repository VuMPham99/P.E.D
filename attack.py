# /usr/bin/env python3

# CS 642 University of Wisconsin
#
# usage: python3 attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys
import hashlib
# Grab ciphertext from first argument
ciphertextWithTag = bytes.fromhex(sys.argv[1])

if len(ciphertextWithTag) < 16+16+32:
  print("Ciphertext is too short!")
  sys.exit(0)


new_message = \
"""AMOUNT: $1037.98
Originating Acct Holder: Alexa
Orgininating Acct #98166-20633

I authorized the above amount to be transferred to the account #51779-31226 
held by a Wisc student at the National Bank of the Cayman Islands.
"""


iv = ciphertextWithTag[:16]
iv = iv.hex()

iv1 = iv[:-14]
iv2 = iv[22:]

# TODO: Modify the input so the transfer amount is more lucrative to the recipient

#initial message
d ="414d4f554e543a2024202033372e39380a4f726967696e6174696e67204163637420486f6c6465723a20416c6578610a4f7267696e696e6174696e672041636374202339383136362d32303633330a0a4920617574686f72697a6564207468652061626f766520616d6f756e7420746f206265207472616e7366657272656420746f20746865206163636f756e74202335313737392d3331323236200a68656c64206279206120576973632073747564656e7420617420746865204e6174696f6e616c2042616e6b206f6620746865204361796d616e2049736c616e64732e0a" 

new = "414d4f554e543a2024313033372e3938" #first line of new message in hex
ini = d[:-(len(d)-32)] #first line of initial message

ciphertext = ciphertextWithTag.hex()[32:len(ciphertextWithTag.hex())-64] #ciphertext without iv

#XORing and storing iv bytes corespoding to the changes message 
iv_c1 = hex(int(ini[18:20],16)^int(new[18:20],16)^int(iv[18:20],16))
iv_c1 = iv_c1[2:]
iv_c2 = hex(int(ini[20:22],16)^int(new[20:22],16)^int(iv[20:22],16))
iv_c2 = iv_c2[2:]

#puting old iv and new changes to make new iv
iv_new = iv1 + iv_c1+iv_c2+iv2

#put new iv to rest of ciphertext to complete ciphertext
ciphertext = iv_new + ciphertext
ciphertext = bytes.fromhex(ciphertext)

#creating fake tag corespoding to new message
fake_tag = bytes.fromhex(hashlib.sha256(new_message.encode()).hexdigest())

# TODO: Print the new encrypted message
# you can change the print content if necessary

print(ciphertext.hex() + fake_tag.hex())
