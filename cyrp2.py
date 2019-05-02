from Crypto.Cipher import Salsa20
import uuid
import json
import random
import hashlib
import string



def randomString(stringLength=60):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def passwordHash(salt1, salt2, username, pwd):
  s1 = hashlib.sha256(b'another awesome password').digest()  
  s2 = hashlib.sha256(b'another awesome password').digest()  

pwd = "sushant@12345"
salt1 = randomString()
salt2 = randomString()
username = "sushant87@gmail.com"

# passwordHash(salt1, salt2, username, pwd)

dict = {
    "username": username, 
    "password": pwd,
    "salt1": salt1,
    "salt2": salt2
}

data = json.dumps(dict)
print(data, type(data))

test = hashlib.sha256(username.encode()).digest()
print(test)

# secret = hashlib.sha256(b'another awesome password').digest()

secret = b'mDG9RaBeR3GSFn4GLZmhdhIQy7vEwROZ'
print(secret)

plaintext = b'Attack at dawn'
cipher = Salsa20.new(key=secret)
msg = cipher.nonce + cipher.encrypt(plaintext)

print(msg)

msg_nonce = msg[:8]
ciphertext = msg[8:]
cipher = Salsa20.new(key=secret, nonce=msg_nonce)
plaintext = cipher.decrypt(ciphertext)

print(plaintext.decode())



