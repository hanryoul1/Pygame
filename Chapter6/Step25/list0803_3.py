# 실시간으로 캐릭터 움직이기

import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

cx = 400
cy = 300

def main_proc():
    global cx, cy
    if key == "Up":
        cy = cy - 20
    if key == "Down":
        cy = cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20
    canvas.coords("MYCHR", cx, cy)
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("캐릭터 이동")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
# 둘 다 KeyPress로 설정하면 작동하지 않음

canvas = tkinter.Canvas(width=800, height=600, bg='lightgreen')
canvas.pack()
img = tkinter.PhotoImage(file= "image/mimi.png")
# PhotoImage 명령으로 이미지 로딩

canvas.create_image(cx, cy, image=img, tag="MYCHR")
# create_image() 명령으로 캔버스에 이미지 표시
# tag= 뒤에 입력한 문자열이 태그명/ex) MYCHR == free, but easy

main_proc()
root.mainloop()
