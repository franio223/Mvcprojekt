from models.task import Task

def test_task_creation():
    task = Task("Umyć naczynia", "2025-05-25")
    assert task.description == "Umyć naczynia"
    assert task.due_date == "2025-05-25"
    assert task.status == "Nieukończone"

test_task_creation()
print(" Test przeszedł pomyślnie!")
