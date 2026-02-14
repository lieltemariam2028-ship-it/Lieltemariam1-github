todo = []

todo_list = int(input(
    "What would you like to do?\n"
    "1. Add item "
    "2. Remove item "
    "3. Clear list "
    "Enter choice: "
))

if todo_list == 1:
    choice = input("What would you like to add: ")
    todo.append(choice)
    print(todo)

elif todo_list == 2:
    remove = input("What do you want to remove: ")
    if remove in todo:
        todo.remove(remove)
        print("Successfully removed")
    else:
        print("Item not found")
    print(todo)

elif todo_list == 3:
    todo.clear()
    print("Successfully cleared")

else:
    print(todo)
