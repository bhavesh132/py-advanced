def average(a,b):
    print("The average is" + (a+b)/2)


def average (*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is ",  round(sum/len(numbers), 2))

average(1,2,3,4,5,6,7,89,0,245,234,14,346,312,4213,345,12,312,4346,12,323456,1234,346,213,24,51234,24,51,34123,346,12,324,61234,46,1234,24,6123,4234,5)


def name(**name):
    print ("Hello " + name["first"] + " " + name["last"])

name(first = "Rahul", last = "Sharma")


custom_list = [1,2,3,4,5,6,7,8,9,10]

for index, val in enumerate(custom_list):
    print(index, val+20)