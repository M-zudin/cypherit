import secrets
import sys
try:
    file=open('keygen-encoding.config')
    encoding=file.read()
except:
    encoding='utf-8'
while True:
    atts=0
    while True:
        try:
            print('Input key length (bits):')
            bits=int(sys.stdin.readline())
            if bits%8!=0:
                raise ValueError
        except ValueError:
            print('''Not a number or can't divide by 8''')
        else:
            break
    print('Generating key...')
    while True:
        atts+=1
        key=[]
        for x in range(0,int(bits/8)):
            key.append(secrets.randbits(8))
        try:
            key=bytes(key).decode(encoding)
            print('Key:',key,'Attempts',atts)
        except UnicodeDecodeError:
            pass
        except LookupError:
            encoding='utf-8'
        else:
            break
        
