from cProfile import label
import tkinter


import tkinter
import random
root = tkinter.Tk()

def click_btn():
    label["text"]=random.choice(["大吉", "中吉", "小吉", "凶"])
    label.update()

root.title("おみくじソフト")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="eriya_omikuzi.png")
canvas.create_image(200,400,image=gazou)
label = tkinter.Label(root, text="？？", font=("Times New Roman", 120), bg="white", fg="black")
label.place(x=380, y=60)
button = tkinter.Button(root, text="おみくじを引く", font=("Times New Roman", 36), command=click_btn, fg="skyblue")
button.place(x=360,y=400)
root.mainloop()