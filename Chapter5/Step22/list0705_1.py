# 단계1: GUI 배치하기

import tkinter

root = tkinter.Tk()
root.title("고양이 지수 진단 게임")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
pic = tkinter.PhotoImage(file="image/melody.png")
canvas.create_image(400, 300, image=pic)

button = tkinter.Button(text="진단하기", font=("한컴산뜻돋움", 32), bg="pink")
button.place(x=400, y=480)
text = tkinter.Text(width=40, height=5, font=("한컴산뜻돋움", 16))
text.place(x=320, y=30)
root.mainloop()