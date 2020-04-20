'''a simple GUI attempt for ged project
Fangji Liang 04/19/2020
'''

from ssw555Prj_Hogwarts import Repository
from error_list import pretty_error
from special_list import pretty_special
from tkinter import *
from tkinter import messagebox


repo = Repository()


def display_Repository():
    pt = Tk()
    pt.iconbitmap("hogwarts.ico")
    pt.title("Repository")
    pt.geometry("900x600")
    s1 = Scrollbar(pt)
    s1.pack(side=RIGHT, fill=Y)
    s2 = Scrollbar(pt, orient=HORIZONTAL)
    s2.pack(side=BOTTOM, fill=X)
    t = Text(pt, yscrollcommand=s1.set, xscrollcommand=s2.set, wrap='none')
    t.pack(expand=YES, fill=BOTH)
    s1.config(command=t.yview)
    s2.config(command=t.xview)
    t.insert(INSERT, repo)
    t.configure(state='disabled')
    t.pack()


def display_error():
    pt = Tk()
    pt.iconbitmap("hogwarts.ico")
    pt.title("Error List")
    pt.geometry("900x600")
    s1 = Scrollbar(pt)
    s1.pack(side=RIGHT, fill=Y)
    s2 = Scrollbar(pt, orient=HORIZONTAL)
    s2.pack(side=BOTTOM, fill=X)
    t = Text(pt, yscrollcommand=s1.set, xscrollcommand=s2.set, wrap='none')
    t.pack(expand=YES, fill=BOTH)
    s1.config(command=t.yview)
    s2.config(command=t.xview)
    t.insert(INSERT, pretty_error(repo))
    t.configure(state='disabled')
    t.pack()


def display_unique():
    pt = Tk()
    pt.iconbitmap("hogwarts.ico")
    pt.title("Special List")
    pt.geometry("900x300")
    s1 = Scrollbar(pt)
    s1.pack(side=RIGHT, fill=Y)
    s2 = Scrollbar(pt, orient=HORIZONTAL)
    s2.pack(side=BOTTOM, fill=X)
    t = Text(pt, yscrollcommand=s1.set, xscrollcommand=s2.set, wrap='none')
    t.pack(expand=YES, fill=BOTH)
    s1.config(command=t.yview)
    s2.config(command=t.xview)
    t.insert(INSERT, pretty_special(repo))
    t.configure(state='disabled')
    t.pack()


def main_window():
    prime = Tk()
    prime.iconbitmap("hogwarts.ico")
    prime.title("ssw555Prj_Hogwarts")
    prime.geometry("200x150")
    B1 = Button(prime, text="Repository", command=display_Repository)
    B2 = Button(prime, text="Error List", command=display_error)
    B3 = Button(prime, text="Special List", command=display_unique)
    B1.pack()
    B2.pack()
    B3.pack()
    prime.mainloop()


if __name__ == "__main__":
    main_window()
