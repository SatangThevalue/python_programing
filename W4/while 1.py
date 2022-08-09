import os
os.system('cls')
i=1
num=[]
while i<=5:
    n = int(input("Enter Num %d : "%i))
    num.append(n)
    i=i+1
print("Your Num : %s" %num)
print("Min Num : " ,min(num))
print("Max Num : " ,max(num))
print("Sum Num : " ,sum(num))
