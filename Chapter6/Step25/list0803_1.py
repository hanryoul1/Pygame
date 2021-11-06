# 실시간 키 입력

import tkinter

key = 0
def key_down(e):
    global key
    key = e.keycode

def main_proc():
    label["text"] = key
    root.after(100, main_proc)  
    # 0.1초 후 실행할 함수 지정(main_proc)
    # 1000 = 1초, 100 = 0.1초

root = tkinter.Tk()
root.title("실시간 키입력")
root.bind("<KeyPress>", key_down)
label = tkinter.Label(font=("한컴산뜻돋움", 80))
label.pack()
main_proc()

root.mainloop()