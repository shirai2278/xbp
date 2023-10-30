
score=0

print("PK対決! 全5回戦")
name=input("挑戦者の名前は？")
print(name, "さんはキッカーです。")

#----------------------------------------------------------- 
print("1回目")
print("1.左 2.中央 3.右")
selecta = int(input("コースを数字で入力してね。"))
import random
a = random.randint(1,3)
if selecta == a:
    print("goal!")
    scorea=score+1
else:
    print("miss...")
    scorea=score+0
#---------------------------------------------------------
print("2回目")
print("1.左 2.中央 3.右")
selectb = int(input("コースを数字で入力してね。"))
import random
b = random.randint(1,3)
if selectb == b:
    print("goal!")
    scoreb=score+1
else:
    print("miss...")
    scoreb=score+0
#----------------------------------------------------------
print("3回目")
print("1.左 2.中央 3.右")
selectc = int(input("コースを数字で入力してね。"))
import random
c = random.randint(1,3)
if selectc == c:
    print("goal!")
    scorec=score+1
else:
    print("miss...")
    scorec=score +0
#---------------------------------------------------------------------
print("4回目")
print("1.左 2.中央 3.右")
selectd = int(input("コースを数字で入力してね。"))
import random
d = random.randint(1,3)
if selectd == d:
    print("goal!")
    scored=score+1
else:
    print("miss...")
    scored=score+0
#--------------------------------------------------------------------------
print("5回目")
print("1.左 2.中央 3.右")
selecte = int(input("コースを数字で入力してね。"))
import random
e = random.randint(1,3)
if selecte == e:
    print("goal!")
    scoree=score+1
else:
    print("miss...")
    scoree=score+0
#----------------------------------------------------------------------------
print("試合終了")

if score==scorea+scoreb+scorec+scored+scoree>=3:
    print(name,"さんの勝利、おめでとう!")
else:
    print(name,"さんの敗北...お疲れ様でした。")
