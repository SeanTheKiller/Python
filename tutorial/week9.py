#Question 1
food = []

for i in range(1, 6, 1):
     food.append(input(f"Enter favourite food #{i}: "))

print(f"Your favourite food:\n{food}\n")
food.remove(input("Which food you want to remove: "))
print(f"{food}")

#Question 2
movie = []

for i in range(1, 5, 1):
    movie.append(input(f"Enter movie #{1}: "))

print(f"Your movie list so far:\n{movie}")

movie.insert(0, input("Add one more movie: "))
print(f"Update list (with your VIP movie in front):\n{movie}")

remove = movie.pop(int(input("Enter the index of the movie to remove: ")))
print(f"You remove '{remove}'. Here's what's left:\n{movie}")


