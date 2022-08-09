import os
import random
os.system('cls')

print("----------------")
random_num = random.randint(0,9)
num = int(input("กรุณากรอกตัวเลข 0 - 9 : "))
while random_num != num:
    print("ตัวเลขที่สุ่ม : " ,random_num)
    print("ตัวเลขที่คุณป้อน : " ,num)
    print("!!! ตัวเลขไม่เท่ากัน !!!")
    print("----------------")
    random_num = random.randint(0,9)
    num = int(input("กรุณากรอกตัวเลข 0 - 9 : "))
    print("----------------")
    if random_num == num:
        print("ตัวเลขที่สุ่ม : " ,random_num)
        print("ตัวเลขที่คุณป้อน : " ,random_num)
        print(">>> ตัวเลขเท่ากัน <<<")
        break
