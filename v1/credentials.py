import hashlib

def check_email_exists(mail):
    f = open('C:\\Users\\Mihaescu\\Desktop\\cn-project\\v1\\db.txt', "r")
    for line in f:
        user = line.split()
        if mail == user[1]:
            f.close()
            return True

    f.close()
    return False

def check_user_exists(usr): 
    f = open('C:\\Users\\Mihaescu\\Desktop\\cn-project\\v1\\db.txt', "r")

    for line in f:
        user = line.split()
        if usr == user[0]:
            f.close()
            return True

    f.close()    
    return False



def check_password_exists(psd_hash):
    f = open('C:\\Users\\Mihaescu\\Desktop\\cn-project\\v1\\db.txt', "r")

    for line in f:
        user = line.split()
        if psd_hash == user[2].decode("hex"):
            f.close()
            return True
    
    f.close()
    return False

class Login():
    def __init__(self, usr, psd):
        self.u = usr
        self.p = psd
        self.h = hashlib.sha256(psd.encode()).hexdigest()

    def check_credentials(self):
        if check_user_exists(self.u):
            print("Login")
        else:
            print("No way you'll be")
        if check_password_exists(self.h):
            print("Successful!")
        else:
            print("Failed")

    def authenticate_user(self):
        f = open('v1\\db.txt', "r")
        for line in f:
            user = line.split()
            if self.u == user[0] and str(hashlib.sha256(self.p.encode()).hexdigest()) == user[2]: #check on this
                f.close()
                return True
        f.close()
        return False



class SignUp():
    def __init__(self, user, email, password):
        self.u = user
        self.e = email
        self.p = password
        self.h = hashlib.sha256(password.encode()).hexdigest()
    
    def add_db(self):
        f = open('C:\\Users\\Mihaescu\\Desktop\\cn-project\\v1\\db.txt', 'a')
        f.write(self.u + ' ' + self.e + ' ' + self.h)
        f.close()