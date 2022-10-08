# 뽑기 당첨 확률

import random

cnt = 0   # 난수를 발생시킨 횟수를 저장하는 변수

while True:
    r = random.randint(1, 100)
    print(r)  # 생략 가능
    cnt = cnt + 1

    if r == 77:
        break

print(str(cnt) + "번째에 희귀 캐릭터 get!")  # str: 숫자를 문자열로 변환