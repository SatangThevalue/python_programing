import os
os.system('cls')
print("----------------")
print("โปรแกรมวางแผนบริการลูกค้า")
print("----------------")
gender = str(input("กรุณากรอกเพศ : "))
print("----------------")
weight = float(input("กรุณากรอกน้ำหนัก : "))
print("----------------")
height = int(input("กรุณากรอกส่วนสูง : "))
if gender == 'm' or gender == 'M' or gender == 'man' or gender == 'MAN' or gender == 'Man' or gender == 'ชาย' or gender == 'ช':
    if weight >= (height-100):
        print("----------------")
        print(">>> คุณควรออกกำลังกาย <<<")
        print("----------------")
    elif weight < (height-100):
        print("----------------")
        print("+++ คุณผู้ชายหุ่นดีแล้ว +++")
        print("----------------")  
elif gender == 'w' or gender == 'W' or gender == 'woman' or gender == 'WOMAN' or gender == 'Woman' or gender == 'หญิง' or gender == 'ญ':
    if weight >= (height-110):
        print("----------------")
        print(">>> คุณควรออกกำลังกาย <<<")
        print("----------------")
    elif weight < (height-110):
        print("----------------")
        print("+++ คุณผู้หญิงหุ่นดีแล้ว +++")
        print("----------------")  