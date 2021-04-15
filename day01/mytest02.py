#200포함 100~200까지의 합

sum = 0;
for i in range(201):
    if i >= 100:
        sum = sum+i
    
print(sum)

sum = 0
for i in range (101):
    sum += (i+100)
print("sum:",sum)