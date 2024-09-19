task = input("Kindly provide task description: ")
priority = input("Kindly provide the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        msg = f"Reminder: '{task}' is a high priority task"
    case "medium":
        msg = f"Reminder: '{task} is a medium priority task"
    case "low":
        msg = f"Note: '{task}' is a low priority task"
    case _:
        error = "Not a valid priority"
if time_bound == "yes":
    msg += " that requires immediate attention today!"
elif time_bound == "no":
    msg += ". Consider completing it when you have free time."
print(msg)