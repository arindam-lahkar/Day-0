tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    tasks.remove(task)

def show_tasks():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

while True:
    cmd = input("add / remove / list / quit: ")
    if cmd == "add":
        add_task(input("Task: "))
    elif cmd == "remove":
        remove_task(input("Task to remove: "))
    elif cmd == "list":
        show_tasks()
    elif cmd == "quit":
        break