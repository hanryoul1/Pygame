# bind() 명령 사용하기

import tkinter
key = 0
def key_down(e):
    global key
    key = e.keycode
    print("KEY:" + str(key))

root = tkinter.Tk()
root.title("키 코드 얻기")
root.bind("<KeyPress>", key_down)
# blind("<이벤트>", 이벤트 발생 시 실행할 함수명)

root.mainloop()
