import tkinter

KEKKA = [
    "のらってます",
    "のらのらってます",
    "コズミックを感じます",
    "頭のらです",
    "カピピです",
    "キャティです",
    "いますぐコズミックバトル",
    "のらのらのらぁ！"

]

def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    noenedo = int(100*pts/7)
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "＜診断結果＞\nあなたのノエネ度は" + str(noenedo) + "%です\n" + KEKKA[pts])

root = tkinter.Tk()
root.title("ネズミ診断アプリ")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="noene.png")
canvas.create_image(200, 400, image=gazou)
button = tkinter.Button(text="診断する", font=("Times New Roman", 32), bg="lightgreen", command=click_btn)
button.place(x=400, y=480)
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

bvar = [None]*7
cbtn = [None]*7
ITEM = [
    "語尾がのら",
    "コズミックパワーを感じる",
    "地下アイドルタイプ",
    "押しは自分",
    "メガホンマイク",
    "カピピのピ",
    "アルクP"
]
for i in range(7):
    # bvar[i] = tkinter.BooleanVar()
    # bvar[i].set(False)
    # cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=bvar[i], bg="#dfe")
    # cbtn[i].place(x=400, y=160+40*i)
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=bvar[i], bg="#dfe", fg="black")
    cbtn[i].place(x=400, y=160+40*i)
    
root.mainloop()