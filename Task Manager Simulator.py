class Task:
    def __init__(self, title, priority, timeEstimate):
        self.title = title
        self.priority = priority
        self.timeEstimate = timeEstimate
        self.next_task = None

    # Getters
    def get_title(self): return self.title
    def get_priority(self): return self.priority
    def get_time_estimate(self): return self.timeEstimate

    # Setters
    def set_next_task(self, next_task): self.next_task = next_task
    def get_next_task(self): return self.next_task


class TaskManager:
    def __init__(self):
        self.head = None

    def add_task(self, title, priority, timeEstimate):
        # Check for duplicate titles
        current = self.head
        while current:
            if current.get_title() == title:
                print("Error: Task with this title already exists.")
                return False
            current = current.get_next_task()

        new_task = Task(title, priority, timeEstimate)
        if not self.head or (priority < self.head.get_priority() or 
                             (priority == self.head.get_priority() and 
                              timeEstimate < self.head.get_time_estimate())):
            new_task.set_next_task(self.head)
            self.head = new_task
        else:
            current = self.head
            while current.get_next_task() and (current.get_next_task().get_priority() < priority or 
                                             (current.get_next_task().get_priority() == priority and 
                                              current.get_next_task().get_time_estimate() < timeEstimate)):
                current = current.get_next_task()
            new_task.set_next_task(current.get_next_task())
            current.set_next_task(new_task)
        return True

    def view_tasks(self):
        tasks = []
        current = self.head
        while current:
            tasks.append((current.get_title(), current.get_priority(), current.get_time_estimate()))
            current = current.get_next_task()
        return tasks

    def remove_task(self, title):
        if not self.head: return False
        if self.head.get_title() == title:
            self.head = self.head.get_next_task()
            return True
        current = self.head
        while current.get_next_task() and current.get_next_task().get_title() != title:
            current = current.get_next_task()
        if current.get_next_task():
            current.set_next_task(current.get_next_task().get_next_task())
            return True
        return False


class Stack:
    def __init__(self): self.stack = []
    def push(self, action): self.stack.append(action)
    def pop(self): return self.stack.pop() if self.stack else None


class UndoManager:
    def __init__(self): self.action_stack = Stack()

    def add_action_to_stack(self, action_type, task):
        # Store full task object for undo functionality
        self.action_stack.push((action_type, task))

    def undo_last_action(self, task_manager):
        last_action = self.action_stack.pop()
        if last_action:
            action_type, task = last_action
            if action_type == 'add':
                task_manager.remove_task(task.get_title())
            elif action_type == 'remove':
                task_manager.add_task(task.get_title(), task.get_priority(), task.get_time_estimate())


def show_menu():
    print("\n1. Add a Task")
    print("2. View All Tasks")
    print("3. Complete a Task")
    print("4. Undo Last Action")
    print("5. Exit")


def main():
    task_manager = TaskManager()
    undo_manager = UndoManager()
    print("Welcome to Task Manager Simulator!")
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            title = input("Enter task title: ").strip()
            priority = get_valid_input("Enter priority (1 = high, 2 = medium, 3 = low): ", [1, 2, 3])
            time_estimate = get_valid_input("Enter time estimate (minutes): ", int)
            
            if task_manager.add_task(title, priority, time_estimate):
                undo_manager.add_action_to_stack('add', Task(title, priority, time_estimate))
                print("Task added successfully!")

        elif choice == '2':
            tasks = task_manager.view_tasks()
            print("Tasks:")
            if tasks:
                for i, (title, priority, time) in enumerate(tasks, 1):
                    print(f"{i}. {title} (Priority: {['High', 'Medium', 'Low'][priority-1]}, Time: {time} mins)")
            else:
                print("(No tasks to display)")

        elif choice == '3':
            tasks = task_manager.view_tasks()
            if tasks:
                title = input("Enter the title of the task to complete: ").strip()
                # Find the task object before removing it for undo purposes
                tasks_before_removal = task_manager.view_tasks()
                task_to_remove = next((t for t in tasks_before_removal if t[0] == title), None)

                if task_to_remove and task_manager.remove_task(title):
                    undo_manager.add_action_to_stack('remove', Task(*task_to_remove))
                    print("Task \"{}\" completed successfully!" .format(title))
            else:
                print("No tasks to complete.")

        elif choice == '4':
            undo_manager.undo_last_action(task_manager)
            print("Last action undone successfully!")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


def get_valid_input(prompt, valid_type):
    while True:
        try:
            value = input(prompt).strip()
            
            if valid_type == int: 
                return int(value)
            
            if isinstance(valid_type, list): 
                value_int = int(value)
                if value_int in valid_type: 
                    return value_int
            
            raise ValueError
            
        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()