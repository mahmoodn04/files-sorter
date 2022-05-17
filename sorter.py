# Python3
# Author -- Mahmood
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os, shutil, time
import pyinputplus as py

# from pathlib import Path
def browse():
    p = filedialog.askdirectory()


top = Tk()
top.title("Sorter")

Name = py.inputStr(
    "Name for the folder of the things the would moved"
)  # namen of the new folders
p = filedialog.askdirectory()  #'C:\\Users\\Mahmood\\Desktop'
b = Button(text="Browse", command=browse)
Newpath = p + Name
options = py.inputMenu(
    [".pdf", ".txt", ".docx"], blank=False, numbered=True, default=".pdf"
)
if not os.path.exists(Newpath):  # Checking if it's exist and create a new one if not
    os.mkdir(Newpath, 775)
for folders, subforlders, filenames in os.walk(p):  # looking for the files in the path
    for files in filenames:
        if files.endswith(".pdf"):  # for the folders that ends with pdf
            filepath = os.path.join(p, files)  # join the path with the file names
            shutil.move(filepath, Newpath)  # moving them
