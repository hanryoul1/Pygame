# 캔버스 배치

import tkinter
root = tkinter.Tk()
root.title("첫 번째 캔버스")
canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue")   # 캔버스 컴포넌트 생성
canvas.pack()   # 윈도우에 캔버스 배치
root.mainloop()

# 캔버스 생성
# 캔버스 변수명 = tkinter.Canvas(윈도우 객체, width=폭, height=높이, bg=배경색)