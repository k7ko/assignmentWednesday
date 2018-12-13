
studentsMarks = [23, 4, 5, 6, 64, 90, 67, 98, 45, 23, 67, 78, 89]
list1=[]
list2 =[]
for mark in studentsMarks:
    if mark < 50:
        list1.append(mark)
    else:
        list2.append(mark)
for mark in studentsMarks:
    if mark > 90:
        print ("Excellent")
    elif 70 <= mark <= 89:
        print ("Very Good")
    elif 60 <= mark <= 69:
        print ("Good")
    elif 40 <= mark <= 59:
        print ("Poor")
    elif 20 <= mark <= 39:
        print ("Very Poor")
    else:
        print ("Repeat")
        

print(list1)
print(list2)


