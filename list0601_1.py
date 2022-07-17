import tkinter
# import tkinter.font
root = tkinter.Tk()
# root.geometry("800x600")
# root.title("初めてのウィンドウ")
# root.title("初めてのラベル")
# root.geometry("800x600")
# label = tkinter.Label(root, text="ラベルの文字列", font=("System", 24))
# label.place(x=200, y=100)
# root.mainloop()

# print(tkinter.font.families())

# def click_btn():
#     button["text"] = "クリックしました"

# root.title("初めてのボタン")
# button = tkinter.Button(root, text="クリックしてください", font=("Times New Roman", 24), command=click_btn)
# button.place(x=200, y=100)
# root.mainloop()

root.title("初めてのキャンパス")
canvas = tkinter.Canvas(root, width=400, height=600,bg="skyblue")
canvas.pack()
root.mainloop()