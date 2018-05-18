from ftplib import FTP

ftp = FTP('192.168.0.105') 
ftp.login(user = 'Alexandru Mihaescu', passwd = 'Parola123')
ftp.cwd('/')

def upload(file_name):
    ftp.storbinary('STOR ' + file_name, open(file_name, 'rb'))
    ftp.quit()

def download(file_name):
    f = open(file_name, "wb")
    ftp.retrbinaty('RETR ' + file_name, f.write, 1024)
    ftp.quit()
    f.close()

upload('db.txt')
