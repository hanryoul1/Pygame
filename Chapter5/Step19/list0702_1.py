# 여러 행 텍스트 입력 필드

import tkinter

def click_btn():
    text.insert(tkinter.END, "지수 바보!")

root = tkinter.Tk()
root.title("여러 행 텍스트 입력")
root.geometry("400x200")
button = tkinter.Button(text="message", command=click_btn)
button.pack()
text = tkinter.Text()
text.pack()
root.mainloop()