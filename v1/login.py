#!/bin/python

import hashlib

class Login():
    def __init__(self, usr, psd):
        self.u = usr
        self.p = psd
        self.h = hashlib.sha256(psd.encode()).hexdigest()

    def check_credentials(self):
        if self.check_usr(True):
            print("Login")
        else:
            print("No way you'll be")
        if self.check_psd(True):
            print("Successful!")
        else:
            print("Failed")

    def authenticate_user(self):
        return True


    #ret is a boolean value specified at function call, used for prototyping
    def check_usr(self, ret): 
        return ret

    def check_psd(self, ret):
        return ret


