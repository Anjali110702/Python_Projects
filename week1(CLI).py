class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def display_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            print(f"{i}. {task.description} (Due: {task.due_date}, Priority: {task.priority}, Status: {status})")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, description, due_date, priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = description
            task.due_date = due_date
            task.priority = priority
            print("Task updated.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task removed.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Task Description: ")
            due_date = input("Due Date: ")
            priority = input("Priority: ")
            todo_list.add_task(description, due_date, priority)
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == "4":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to update: "))
            description = input("New Description: ")
            due_date = input("New Due Date: ")
            priority = input("New Priority: ")
            todo_list.update_task(task_index, description, due_date, priority)
        elif choice == "5":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
