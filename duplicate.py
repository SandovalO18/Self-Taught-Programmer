def return_duplicates(a_list):
    dups = []
    a_set = set()
    for item in a_list:
        length_one = len(a_set)
        a_set.add(item)
        length_two = len(a_set)
        if length_one == length_two:
            dups.append(item)
    return dups

a_list = ['Susan Adams','Kwame Goodall','Jesus Sandoval','Jill Hampton','Susan Adams','Jesus Sandoval']
dups = return_duplicates(a_list)
print(dups)