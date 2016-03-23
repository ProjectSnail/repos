import os, pickle, getpass

USER_LOCAL_PATH = os.path.join(os.environ["HOME"], ".repos")
USER_AUTH_PATH = os.path.join(USER_LOCAL_PATH, 'auth')

def writeStr(str, f, encode='ascii'):
    pickle.dump(len(str), f)
    f.write(str.encode(encode))

def readStr(f, encode='ascii'):
    l = pickle.load(f)
    return f.read(l)

def checkFolder():
    if not os.path.exists(USER_LOCAL_PATH):
        os.makedirs(USER_LOCAL_PATH)
        return False
    return True

def getAuth():
    if checkFolder():
        if os.path.isfile(USER_AUTH_PATH):
            with open(USER_AUTH_PATH, 'rb') as f:
                pickle.load(f)
                l = pickle.load(f)
                usr = f.read(l)
                l = pickle.load(f)
                pwd = f.read(l)
                return (usr, pwd)
        return None
    return None

def writeAuth(usr, pwd):
    checkFolder()
    with open(USER_AUTH_PATH, 'wb') as f:
        pickle.dump(0, f)
        pickle.dump( len(usr), f)
        f.write(usr.encode('ascii'))
        pickle.dump( len(pwd), f)
        f.write(pwd.encode('ascii'))

def askAuth():
    username = raw_input("Auth required.\n  username: ")
    password = getpass.getpass("  password: ")
    return (username, password)

if __name__ == "__main__" :
    pass
