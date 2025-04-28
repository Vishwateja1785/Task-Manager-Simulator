# Task-Manager-Simulator

A simple console-based Task Manager Simulator that helps users manage their daily tasks efficiently. This project was developed as part of a hackathon challenge.

---

**Features**

- **Add a Task:**  
  Add a new task with a title, priority (1 = high, 2 = medium, 3 = low), and time estimate (in minutes).
- **View All Tasks:**  
  Display all tasks sorted by priority (high to low). Tasks with the same priority are sorted by shortest time estimate first.
- **Complete a Task:**  
  Mark a task as complete, removing it from the task list.
- **Undo Last Action:**  
  Undo the last action (add, complete, or view).
- **Exit:**  
  End the program.

---

## How It Works

1. **Data Structures**
   - **Task:** Each task has a title, priority, and time estimate.
   - **Linked List:** Manages the list of tasks for efficient insertion and removal.
   - **Stack:** Stores user actions to enable the undo feature.

2. **Menu System**
   - Users interact via a menu:
     1. Add a Task
     2. View All Tasks
     3. Complete a Task
     4. Undo Last Action
     5. Exit

3. **Input Validation**
   - The program validates all user inputs and handles invalid entries gracefully.

---

## Sample Usage

```
Welcome to Task Manager Simulator!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: 1

Enter task title: Finish report
Enter priority (1 = high, 2 = medium, 3 = low): 1
Enter time estimate (minutes): 60
Task added successfully!

Choose an option: 2
Tasks:
1. Finish report (Priority: High, Time: 60 mins)

Choose an option: 3
Enter the title of the task to complete: Finish report
Task "Finish report" completed successfully!

Choose an option: 4
Last action undone successfully!

Choose an option: 5
Goodbye!
```

---

## Implementation Breakdown

- **Task Data Structure:**  
  `Task` class with attributes for title, priority, and time estimate.
- **Linked List:**  
  For managing and sorting tasks.
- **Stack:**  
  For undo functionality.
- **Menu Loop:**  
  Handles user input and calls the appropriate functions.
- **Testing:**  
  All features tested for correctness and user experience.

---

## Constraints

- Uses a stack for undo.
- Modular code with separate functions for each operation.
- Handles input validation and errors.
- Menu-driven user interface.

---
