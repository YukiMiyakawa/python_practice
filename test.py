i = 0
while i < 5:
    print(i)
    i += 1

import datetime
print(datetime.date.today())
print(datetime.datetime.now())

d = datetime.datetime.now()
print(d.hour)
print(d.minute)
print(d.second)

today = datetime.date.today()
birth = datetime.date(1993,7,13)
print(today-birth)

# 乱数
import random
#r = random.random()
#print(r)

cnt = 0
while True:
    r = random.randint(1, 100)
    print(r)
    cnt = cnt + 1
    if r == 77:
        break
print(str(cnt) + " 回目でレアキャラをゲット")
