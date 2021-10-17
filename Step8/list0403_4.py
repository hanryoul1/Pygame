# 태어난 시간부터 경과한 날짜 수 확인하기

import datetime
today = datetime.date.today()
birth = datetime.date(2001, 12, 28)
print(today - birth)