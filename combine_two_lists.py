movies = ["Interstellar","The Dark Knight","Inception","The Prestige","Batman Begins"]
ratings = [1,10,10,8,6]
new_list = []
for tree in zip(movies,ratings):
    new_list.append(tree)
print(new_list)