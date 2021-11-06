# after() 명령 사용하기

import tkinter
tmr = 0 
#type: int 
#전역 변수

def count_up():
    global tmr  # 함수 안에서 전역 변수 값을 변경할 때 global 선언
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000, count_up)  # 1초 후에 다시 count_up 함수 실행

root = tkinter.Tk()
label = tkinter.Label(font=("한컴산뜻돋움", 80))
label.pack()
root.after(1000, count_up)
root.mainloop()