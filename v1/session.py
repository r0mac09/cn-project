import tkinter

from tkinter import *


class Session():
    def __init__(self, usr):
        self.window = Tk()
        self.window.title("Session " + usr)