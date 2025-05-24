from models.task import Task

tasks = []  

# Dodanie nowego zadania
def add_task(description, due_date):
    new_task = Task(description, due_date)
    tasks.append(new_task)
    return new_task

# Lista zadań
def get_tasks():
    return tasks

# Usuwanie zadania
def delete_task(index):
    if index < len(tasks):
        del tasks[index]
