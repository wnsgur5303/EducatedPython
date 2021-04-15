#1. 1~200까지의 5의 배수의 합

sum = 0;
for i in range(201):
    if i % 5 == 0:
        sum = sum+i
    
print("sum:",sum)