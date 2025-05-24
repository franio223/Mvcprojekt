class Task:
    def __init__(self, description, due_date, status="Nieukończone"):
        self.description = description
        self.due_date = due_date
        self.status = status
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
