# 메세지 박스 사용 방법

import tkinter
import tkinter.messagebox

def click_btn():
    tkinter.messagebox.showinfo("Information", "You click the button")
    
root = tkinter.Tk()
root.title("First message box")
root.geometry("400x200")
btn = tkinter.Button(text="Test", command=click_btn)
btn.pack()
root.mainloop()