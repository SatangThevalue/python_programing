import os
os.system('cls')

num = int(input("Enter Num : "))
if num > 0:
    if num % 2 == 0 :
        print("จำนวนเป็นเลขคู่")
    else:
        print("จำนวนเป็นเลขคี่")
elif num < 0:
        if num % 2 == 0 :
            print("จำนวนเป็นเลขคู่")
        else:
            print("จำนวนเป็นเลขคี่")
elif num == 0 :
    print("จำนวนเป็นศูนย์")