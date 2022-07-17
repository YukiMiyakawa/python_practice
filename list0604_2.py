import tkinter
root = tkinter.Tk()
root.title("初めての画像表示")
canvas = tkinter.Canvas(root, width=800, height=800)
canvas.pack()
gazou = tkinter.PhotoImage(file="noene.png")
canvas.create_image(400, 500, image=gazou)
root.mainloop()