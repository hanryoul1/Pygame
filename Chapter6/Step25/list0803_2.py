# keysym 값을 사용해 판정하기

import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym
    # keysym은 윈도우, 맥 공통으로 keycode보다 판정 편리

def main_proc():
    label["text"] = key
    root.after(100, main_proc)
    # 확실히 속도 1000<<<100

root = tkinter.Tk()
root.title("실시간 키입력")
root.bind("<KeyPress>", key_down)
label = tkinter.Label(font=("함초롱바탕", 80 ))
label.pack()
main_proc()
root.mainloop()
