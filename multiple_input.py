todos = []

while(True):
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()        
        todos.append(todo)
    if user_action.startswith("show"):
        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter the updated todo: ")
            todos[number] = new_todo
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)
            print(f"Todo {todo_to_remove} is removed from the list")
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break