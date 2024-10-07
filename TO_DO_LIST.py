# todo_list.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def create_task(self, new_task, due_date, priority):
        task = {
            'description': new_task,
            'due_date': due_date,
            'priority': priority,
            'completed': False
        }
        self.tasks.append(task)

    def update_task(self, task_id, **kwargs):
        task = self.tasks[task_id]
        for key, value in kwargs.items():
            task[key] = value

    def track_tasks(self):
        for i, task in enumerate(self.tasks):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{i+1}. {task['description']} - {status}")

    def delete_task(self, task_id):
        del self.tasks[task_id]

todo_list = TodoList()

while True:
    print("1. Create Task")
    print("2. Update Task")
    print("3. Track Tasks")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        new_task = input("Enter task Name: ")
        due_date = input("Enter due date: ")
        priority = input("Enter priority (High/Medium/Low): ")
        todo_list.create_task(new_task, due_date, priority)
    elif choice == '2':
        task_id = int(input("Enter task ID: "))
        new_task = input("Enter new description: ")
        due_date = input("Enter new due date: ")
        priority = input("Enter new priority: ")
        todo_list.update_task(task_id-1, description=new_task, due_date=due_date, priority=priority)
    elif choice == '3':
        todo_list.track_tasks()
    elif choice == '4':
        task_id = int(input("Enter task ID: "))
        todo_list.delete_task(task_id-1)
    elif choice == '5':
        break
    else:
        print("Invalid option. Please try again.")