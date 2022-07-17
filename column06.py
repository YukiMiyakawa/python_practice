import tkinter
root = tkinter.Tk()
root.title("キャンパスに図形を描く")
root.geometry("500x400")
cvs = tkinter.Canvas(root, width=500, height=400, bg="white")
cvs.pack()
cvs.create_oval(250-40, 100-40, 250+40, 100+40, fill="silver", outline="purple")
cvs.mainloop()
