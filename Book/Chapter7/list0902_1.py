# 파이썬에서의 마우스 입력

import tkinter

mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def mouse_release(e):
    global mouse_c
    mouse_c = 0

def game_main():
    fnt = ("한컴산뜻돋움", 30)
    txt = "mouse({},{}){}".format(mouse_x, mouse_y, mouse_c) 
    # {} 안에 순서대로 <mouse_x, mouse_y, mouse_c> 대입

    cvs.delete("TEST")
    cvs.create_text(456, 384, text=txt, fill="black", font=fnt, tag="TEST")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("마우스 입력")
root.resizable(False, False)
root.bind("<Motion>", mouse_move) 
# 마우스 포인터 이동 시 mouse_move 함수 실행

root.bind("<ButtonPress>", mouse_press)
# 마우스 버튼 클릭 시 mouse_press 함수 실행

root.bind("<ButtonRelease>", mouse_release)
# 마우스 버튼 클릭 후 해체 시 mouse_release 함수 실행
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
game_main()
root.mainloop()