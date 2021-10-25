# 캔버스에 이미지 표시하기

import tkinter
root = tkinter.Tk()
root.title("첫 번째 캔버스")
canvas = tkinter.Canvas(root, width=400, height=600)  
canvas.pack()   
khu = tkinter.PhotoImage(file="image/khu.png")
canvas.create_image(200, 300, image=khu)
root.mainloop()