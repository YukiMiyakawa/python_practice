import tkinter

from setuptools import Command

def click_btn():
    txt = entry.get()
    button["text"] = txt

root = tkinter.Tk()
root.title("初めてのテキスト入力")
root.geometry("400x200")
entry = tkinter.Entry(width=20)
entry.place(x=10, y=10)
button = tkinter.Button(text="文字列の取得", command=click_btn)
button.place(x=20, y=100)
root.mainloop()