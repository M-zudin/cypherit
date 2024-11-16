import os
import sys
import pyAesCrypt
direct=input('Input path to encrypted directory: ')
password=input('Input key: ')
def decrypt(file):
    global password
    print('-'*80)
    password=str(password)
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)
    print("[Decrypt] '" + str(os.path.splitext(file)[0]) + "'")
    os.remove(file)
 
def walk(directory):
    try:
        for name in os.listdir(directory):
            path = os.path.join(directory, name)
            if os.path.isfile(path):
                try:
                    decrypt(path)
                except:
                    print('Incorrect password')
                    break
            else:
                walk(path)
    except:
        print('Directory not found')
 
walk(str(direct))
print('-' * 80)
input('Press enter...')
