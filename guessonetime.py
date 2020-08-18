import random
num=random.randint(1,10)

ans=(input("請輸入數字:"))
if ans=='1' or ans=='2'or ans=='3'or ans=='4'or ans=='5'or ans=='6'or ans=='7'or ans=='8'or ans=='9'or ans=='10':
    
    if num==ans:
        print("恭喜答對")
    else:                   
        print("錯了")
else:
    print("error")
#if ans==str:                   
    #print("請輸入int")