numbers = [2,2,3,3,5,7,7,9,11,11]

count = {}

for number in numbers:
    if number not in count:
        count[number] = 1
    else:
        count[number] += 1

for key,value in count.items():
    if value == 1:
        print(key)

print(count)

'''for i in num:
    if num.count(i) == 1:
        print("Number with single occurance is {}".format(i))'''