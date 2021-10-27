# Entry 내 문자열 조작하기

import tkinter

def click_btn():   
    # 버튼 클릭 시 실행되는 함수 정의

    txt = entry.get()   
    # 입력 필드의 문자열을 변수 txt에 대입

    button["text"] = txt   
    # 버튼의 문자열에 txt의 값을 대입   


root = tkinter.Tk()
root.title("첫번째 텍스트 입력 필드")
root.geometry("400x200")
entry = tkinter.Entry(width=20)
entry.place(x=20, y=20)
button = tkinter.Button(text="문자열 얻기", command=click_btn) 
# command=로 실행할 함수 지정

button.place(x=20, y=100)
root.mainloop()