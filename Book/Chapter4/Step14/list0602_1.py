# 라벨 배치

import tkinter
root = tkinter.Tk()
root.title("첫 번째 라벨")
root.geometry("800x600")

label = tkinter.Label(root, text = "라벨 문자열", font = ("한컴산뜻돋움", 24)) 
# 라벨 변수명 = tkinter.Label(윈도우 객체, text = "라벨 문자열", font = ("폰트 명", 폰트 크기))

label.place(x=300, y=100)
# {라벨 변수명}.place(x=X좌표, y=Y좌표)

root.mainloop()