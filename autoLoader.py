'''
By Alex
Python 3.8.2
Written on VS Code v1.45.0

Keep all files within the same directory (icon.ico, zbg.png etc, autoLoaderSave.txt.)

Program will create autoLoaderSave.txt that will store your selections.

Compiled using pyinstaller, working on Windows 10.
cmd: pyinstaller --noconsole --onefile --icon="path to icon" autoLoader.py

To clear your app list just delete "autoLoaderSave.txt".

Functionality that could be added: remove applications from list.
'''

import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
import subprocess, sys

HEIGHT = 700
WIDTH = 600

root = tk.Tk()
root.title("z0mbie Game Loader")
programs = []

def ClearList():
    for widgets in frame.winfo_children():
        widgets.destroy()

def CheckProgramAlreadyAdded(name):
    global programs
    if name in programs:
        messagebox.showerror("Ooops", "That is already in your apps list!")
        return True
    return False

def PrintProgramList():
    for i in programs:
        label = tk.Label(frame, text=i)
        label.pack()

def AddProgram():
    ClearList()
    #add "executables", "*.exe" to filetypes for exe files only (windows)
    name = filedialog.askopenfilename(initialdir="/", title="Select game platform to add", filetypes=([("all files", "*.*")]))
    if name == () or name == "":
        return PrintProgramList()
    else:
        if not CheckProgramAlreadyAdded(name):
            programs.append(name)
    return PrintProgramList()

def RunPrograms():
    #linux/mac (needs testing on mac)	
    #opener ="open" if sys.platform == "darwin" else "xdg-open"	
    
    for exe in programs:
        #windows
        os.startfile(exe)

        #linux/mac (needs testing on mac)
        #subprocess.call([opener, exe])

def save():
    saveFile = open('autoLoaderSave.txt', 'w')
    for exe in programs:
        saveFile.write(exe + ',')

def load():
    global programs
    if os.path.isfile('autoLoaderSave.txt'):
        savedPrograms = open('autoLoaderSave.txt', 'r').read()
        savedPrograms = savedPrograms.split(',')
        programs = [x for x in savedPrograms if x.strip()]
    PrintProgramList()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bgI = tk.PhotoImage(file='./zbg.png')
bgL = tk.Label(root, image=bgI)
bgL.place(x=0, y=0)

frame = tk.Frame(root, bg='#d9ff66', highlightbackground="black", highlightthickness=2)
frame.place(relx=0.12, rely=0.1, relwidth=0.75, relheight=0.7)

openFile = tk.Button(root, text="ADD", bd=2, highlightbackground="black", highlightthickness=2, bg='white', command=AddProgram)
openFile.place(relx=0.12, rely=0.87, relwidth=0.2, relheight=0.05)

loadPrograms = tk.Button(root, text="LOAD ALL", highlightbackground="black", highlightthickness=2, bg='white', command=RunPrograms)
loadPrograms.place(relx=0.67, rely=0.87, relwidth=0.2, relheight=0.05)

load()
root.iconbitmap('./icon.ico')
root.mainloop()
save()
