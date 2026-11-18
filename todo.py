tasks = ["Wash clothes", "Code", "Write one chapter", "Read novel", "Cook lunch", "Go for a walk"]

while True:
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("Your tasks:")
        for task in tasks:
            print(task)

    elif choice == "3":
        print("Exit")
        break

    else:
        print("Invalid option!")