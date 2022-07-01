# เคลียร์ Output ที่ไม่เกี่ยวข้องออกไป
import os
os.system("cls")

print("--------------------")
print("--- Big Data 65  ---")
print("--- Poly Pyramid ---")
print("--------------------")


n = int(input("กรุณาป้อนจำนวนแถว : ")) #รับค่าจำนวนแถว
for row in range(0, n):
    for col in range(n - row - 1): #สมการหาช่องว่างคือ n-row-1
        print(" ",end="")
    for col in range(row + 1): #สมการใส่ดอกจันทร์คือ row+1
        print("*",end=" ")
    print()
