import tkinter
import login
import session
	
from tkinter import *
from login import *
from session import *

class LoginWindow():
    def __init__(self):
        self.window = Tk()
        self.window.title("CNizator v0.1")
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

        self.test_label = Label(self.window, text="Nada", font=("Helvetica", 12))
        self.test_label.grid(column=0, row=5)

        login_button = Button(self.window, text="Login", bg="light blue", fg="white", command=self.login_action)
        login_button.grid(column=1, row=3)

        ots_button = Button(self.window, text ="One Time Session", bg="orange", fg="white")
        ots_button.grid(column=0, row=4)

        signup_button = Button(self.window, text ="Sign Up", bg="orange", fg="white")
        signup_button.grid(column=1, row=4)

        self.window.mainloop()

    def login_action(self):
        user = self.usr.get()
        password = self.psd.get()
        self.test_label.configure(text=user + password)

        l = Login(user, password)
        if l.authenticate_user():
            session_window = Session(user)
            self.usr = Entry(self.window, width=24, state='disabled')
            self.psd = Entry(self.window, width=24, state='disabled')



login_window = LoginWindow()
