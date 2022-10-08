# 단계1: 이미지 표시하기

import tkinter
root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False)   # resizable: 윈도우 크기 변경 여부를 의미
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
pic = tkinter.PhotoImage(file="image/miko.png")
canvas.create_image(400, 300, image=pic)
root.mainloop()