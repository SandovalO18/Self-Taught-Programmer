'''input_string = "Buy 1 get 2 free"
new_list = [c for c in input_string if c.isdigit()][-1]
print(new_list)'''

#List Comprehension --> [expression(i) for i in input_list if filter(i)]

input_list = [1,7,5,3,2]
new_list = [number*7 for number in input_list]
print(new_list)