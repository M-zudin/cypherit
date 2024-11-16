import os
import sys
import pyAesCrypt
direct = input("Input directory: ")
password = input("Input key: ")
def crypt(file):
    global password
    print('-' * 80)
    password = str(password)
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
    print("[Encrypt] '"+str(file)+".crp'")
    os.remove(file)
 
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path)
 
walk(str(direct))
print('-' * 80)
input('Press enter...')
