# 단계1: 주사위 게임 보드 표시하기2

pl_pos = 6
com_pos = 3

def board():
    print("•" * (pl_pos-1) + "P" + "•" * (30-pl_pos))
    print("•" * (com_pos-1) + "C" + "•" * (30-com_pos))
    
board()