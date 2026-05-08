#Question 1
playlist = []

for i in range(1, 6, 1):
    playlist.append(input(f"Enter song #{i}: "))
print(f"Your playlist:\n{playlist}")

playlist.append(input(f"Add one more song: "))
print(f"Updated list\n{playlist}")

#Question 2
students = []

for i in range(1, 5, 1):
    students.append(input("Enter student: "))
print(f"Current students:\n{students}")

students.insert (1, input("Enter new student to insert at position 1: "))
print(f"Update students list:\n{students}")

#Question 3
habits = []

for i in range(1, 7, 1):
    habits.append(input(f"Enter habit #{i}: "))
print(f"Your habits list:\n{habits}")

habits.remove(input("Which habits do oyu want to remove? "))
print(f"Update list:\n{habits}")

#Question 4
groceries = []

for i in range(1, 6, 1):
    groceries.append(input(f"Enter grocery item #{i}: "))
print(f"Your groceries:\n{groceries}")

remove_item = groceries.pop(int(input(f"Enter the index of the item to remove: ")))
print(f"You remove {remove_item}\nRemaining items: {groceries}")

#Question 5
numbers = []

for i in range(1, 6, 1):
    inputing = input("Enter number: ")
    numbers.append(inputing)
print(f"Original list:\n{numbers}")

numbers.sort()
print(f"Sorted list:\n{numbers}")

numbers.reverse()
print(f"Reverse list:\n{numbers}")