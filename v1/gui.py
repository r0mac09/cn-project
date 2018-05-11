import tkinter
import credentials
import session
import mail
	
from tkinter import *
from credentials import *
from session import *
from mail import *

class SessionWindow():
    def __init__(self):
        self.window = Tk()
        self.window.title("Chat\'s Up v0.1")
        self.window.geometry('300x500')

        self.window.mainloop()


class SignUpWindow():
    def __init__(self):
        self.window = Tk()
        self.window.title("Sign Up v0.1")
        self.window.geometry('270x160')

        signup_label = Label(self.window, text="Sign Up", font=("Helvetica", 14))
        signup_label.grid(column=0, row=0)

        usr_label = Label(self.window, text="User:", font=("Helvetica", 12))
        usr_label.grid(column=0, row=1)

        self.usr = Entry(self.window, width=24)
        self.usr.grid(column=1, row=1)

        eml_label = Label(self.window, text="Email:", font=("Helvetica", 12))
        eml_label.grid(column=0, row=2)

        self.eml = Entry(self.window, width=24)
        self.eml.grid(column=1, row=2)

        psd_label = Label(self.window, text="Password:", font=("Helvetica", 12))
        psd_label.grid(column=0, row=3)

        self.psd = Entry(self.window, width=24)
        self.psd.grid(column=1, row=3)

        repsd_label = Label(self.window, text="Re-Password:", font=("Helvetica", 12))
        repsd_label.grid(column=0, row=4)

        self.repsd = Entry(self.window, width=24)
        self.repsd.grid(column=1, row=4)

        signup_button = Button(self.window, text="Sign Up", bg="light blue", fg="white", command=self.signup_action)
        signup_button.grid(column=1, row=6)

        cancel_button = Button(self.window, text="Cancel", bg="red", fg="white", command=self.cancel_action)
        cancel_button.grid(column=0, row=6)

        self.window.mainloop()

    def signup_action(self):
        user = self.usr.get()
        email = self.eml.get()
        password = self.psd.get()
        repassword = self.repsd.get()

        if check_user_exists(user):
            usr_exist_label = Label(self.window, text="user already taken", font=("Helvetica", 12))
            usr_exist_label.grid(column=3, row=1)
        elif check_email_exists(email):
            eml_exist_label = Label(self.window, text="email already used", font=("Helvetica", 12))
            eml_exist_label.grid(column=3, row=2)
        elif not password == repassword:
            psd_no_match_label = Label(self.window, text="passwords must match", font=("Helvetica", 12))
            psd_no_match_label.grid(column=3, row=4)
        elif not user == None and not email == None and not password == None:
            s = SignUp(user, email, password)
            s.add_db()
        
        

    def cancel_action(self):
        self.window.destroy()


class LoginWindow():
    def __init__(self):
        self.window = Tk()
        self.window.title("Chat's Up v0.1")
        self.window.geometry('350x200')

        login_label = Label(self.window, text="Login", font=("Helvetica", 14))
        login_label.grid(column=0, row=0)

        usr_label = Label(self.window, text="User:", font=("Helvetica", 12))
        usr_label.grid(column=0, row=1)

        self.usr = Entry(self.window, width=24)
        self.usr.grid(column=1, row=1)

        psd_label = Label(self.window, text="Password:", font=("Helvetica", 12))
        psd_label.grid(column=0, row=2)

        self.psd = Entry(self.window, width=24)
        self.psd.grid(column=1, row=2)

        login_button = Button(self.window, text="Login", bg="light blue", fg="white", command=self.login_action)
        login_button.grid(column=1, row=3)

        resetpsd_button = Button(self.window, text="Reset Password", bg="light blue", fg="white", command=self.resetpsd_action)
        resetpsd_button.grid(column=2, row=3)

        ots_button = Button(self.window, text ="One Time Session", bg="orange", fg="white")
        ots_button.grid(column=0, row=4)

        signup_button = Button(self.window, text ="Sign Up", bg="orange", fg="white", command=self.signup_action)
        signup_button.grid(column=1, row=4)

        self.window.mainloop()

    def login_action(self):
        user = self.usr.get()
        password = self.psd.get()

        nousr_label = Label(self.window, text='', font=("Helvetica", 12))
        nousr_label.grid(column=2, row=1)
        nopsd_label = Label(self.window, text='', font=("Helvetica", 12))
        nopsd_label.grid(column=2, row=2)

        if user == "":
            nousr_label.configure(text='                  ')
            nousr_label.configure(text='no user           ')
        elif not check_user_exists(user):
            nousr_label.configure(text='                  ')
            nousr_label.configure(text='inexistent')
        else:
            nousr_label.configure(text='                  ')

        if password == "":
            nopsd_label.configure(text='no password')          
        else :
            nopsd_label.configure(text='                       ')


        l = Login(user, password)
        if l.authenticate_user():
            SessionWindow()

    def signup_action(self):
        SignUpWindow()

    def resetpsd_action(self):
        m = Mail()
        m.send_mail('mihaescuac@gmail.com', 'It works!')

login_window = LoginWindow()



