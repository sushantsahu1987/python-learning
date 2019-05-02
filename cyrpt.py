import binascii
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter
import base64

def int_of_string(s):
    return int(binascii.hexlify(s), 16)

def encrypt_message(key, plaintext):
    iv = os.urandom(16)
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return iv + aes.encrypt(plaintext)

def decrypt_message(key, ciphertext):
    iv = ciphertext[:16]
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext[16:])

import random
import string
key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
print(string.ascii_letters)
print(string.punctuation)
print(string.digits)
print(key)
print(len(key))

key = '622822B3B85B269D'+'F41583A32E495888'

print(len(key))

enctxt = encrypt_message(key, 'Hello how are you people')
encodedtext = base64.encodestring(enctxt)
print(encodedtext)
print(enctxt)
decrypt = decrypt_message(key, enctxt)
print(decrypt.decode())

