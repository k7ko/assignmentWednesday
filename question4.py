list1 = []
x = input().split(",")

for number in x:
    try:
        y = int(number, 2)
    except ValueError:
        print("Binary numbers only!!!")
    else: 
        if y%5 == 0:
            list1.append(number)
print(','.join(list1))

