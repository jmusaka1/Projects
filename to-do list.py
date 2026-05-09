print("Welcome to your TO-DO list!! Let's crush this! 💪")

#Creating original list
task_list = []
tasks = input("What are your tasks? ")

for task in tasks.split(","):
    task_list.append(task.strip())

#Adding or deleting a task
list_edit = input("Would you like to add a task, delete a task, or quit (a for add, d for delete, q for quit)? ")

while list_edit == 'a' or list_edit == 'd':
#Adding a task
    if list_edit == 'a':
        add_task = input("What is your new task? ")
        task_list.append(add_task)

#Deleting a task
    if list_edit == 'd':
        delete_task = int(input("Which task would you like to delete (type the respective number of the task starting from 0)?"))

        for i, task in enumerate(task_list):
            if delete_task == i:
                task_list.remove(task)

    list_edit = input("Would you like to add a task, delete a task, or quit (a for add, d for delete, q for quit)? ")

#Quit
if list_edit == 'q':
    print("Here's your list: ")
    for task in task_list:
        print(f"-{task}")