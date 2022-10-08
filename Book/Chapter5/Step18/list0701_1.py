# 1행 텍스트 입력 필드

import tkinter
root = tkinter.Tk()
root.title("첫번째 텍스트 입력 필드")
root.geometry("400x200")

entry = tkinter.Entry(width=20)  # 20 문자 크기 입력 필드 컴포넌트 생성
entry.place(x=10, y=10)  # 윈도우에 입력 필드 컴포넌트 배치
root.mainloop()