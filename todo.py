while True:
 print("1. Add tasks")
 print("2. View tasks")
 print("3. Exit")

 tasks=["Wash clothes","Code","Write one chapter","Read novel","Cook lunch","Go for a walk"]
 for task in tasks:
    print(task)

 choice= input("Choose an option: ")

 if choice =="1":
     task=input("Enter a new task:")
     tasks.append(task)
     print("task added!")

     if choice=="2":
       task=input("View all the task:")
       print("menu")

       if choice=="3":
         print("Exit")
         