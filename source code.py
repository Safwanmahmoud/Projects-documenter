from collections import deque
from tkinter import *
from tkinter import ttk
import os
from tkinter import filedialog
import zipfile
import glob
from pathlib import Path



fils_list = []
dir_list = []

def add_dir():
    global Directories
    dir = filedialog.askdirectory(parent=root, title='Please select a directory')

    if len(dir) != 0:
        dir_list.append(dir)
        Directories.insert(END, "\n " + dir)

def add_file():
    global Directories
    dir = filedialog.filename = filedialog.askopenfilename()
    
    if len(dir) != 0:
        fils_list.append(dir)
        Directories.insert(END, "\n " + dir)

def zip_all():
    global fils_list,dir_list


    with zipfile.ZipFile('Projects/' + title.get(1.0, "end-1c") + '.zip', 'w') as f:
        # zipping files 
        for i in fils_list:
            print(i)
            f.write(i,arcname=Path(i).name)
        
        for u in dir_list:
            for file in glob.glob(u + '/*'):
                f.write(file,arcname=Path(file).name)

        with open('readme.txt', 'w') as l:
            l.write(description.get(1.0, "end-1c"))
        
        f.write('readme.txt')
        os.remove('readme.txt')

def clear():
    fils_list = []                 # clear files list
    dir_list = []                  # clear directories list
    title.delete(1.0, 'end')       # clearing title box
    Directories.delete(1.0, 'end') # clearing directories box
    description.delete(1.0, 'end') # clearing description box


root = Tk()
root.title("Projects Documenter")


# labels:
ttk.Label(root, text="Project Title").grid(row=0, column=4, padx=10, pady=10, columnspan=1)
ttk.Label(root, text="Directories").grid(row=3, column=4, padx=10, pady=10, columnspan=1)
ttk.Label(root, text="Descritption").grid(row=9, column=4, padx=10, pady=10, columnspan=1)

# Texts
title = Text(root, width=60, height=2, font=('Arial', 16))
title.grid(row=2, column=1, columnspan=7, padx=20, pady=10)

Directories = Text(root, width=103, height=8, font=('Arial', 10))
Directories.grid(row=4, column=1, columnspan=7, padx=20, pady=10)

description = Text(root, width=80, height=4, font=('Arial', 12))
description.grid(row=10, column=1, columnspan=7, padx=20, pady=10)

#buttons
save_projects = ttk.Button(root, text="Save Project", command = zip_all).grid(row=11, column=6, columnspan=2, rowspan = 1, padx=10, pady=20)
clear_ = ttk.Button(root, text="Clear", command = clear).grid(row=11, column=3, columnspan=2, rowspan = 1, padx=10, pady=20)
Add_file = ttk.Button(root, text="Add File", command=add_file).grid(row=8, column=5, columnspan=2, padx=10, pady=20)
Add_directory = ttk.Button(root, text="Add directory", command = add_dir).grid(row=8, column=2, columnspan=2, padx=10, pady=20)

root.mainloop()