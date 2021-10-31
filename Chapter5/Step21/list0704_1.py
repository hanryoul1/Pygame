# 메세지 박스 사용 방법

import tkinter
import tkinter.messagebox

def click_btn():
    tkinter.messagebox.showinfo("Information", "You click the button")

    # 메세지 박스 표시 명령어
    # showinfo: 정보를 표시하는 메세지 박스
    # showwarning: 경고를 표시하는 메세지 박스
    # showerror: 에러를 표시하는 메세지 박스
    # askyesno: '네', '아니오' 버튼이 있는 메세지 박스
    # askokcancel: 'OK', '취소' 버튼이 있는 메세지 박스
    
root = tkinter.Tk()
root.title("First message box")
root.geometry("400x200")
btn = tkinter.Button(text="Test", command=click_btn)
btn.pack()
root.mainloop()