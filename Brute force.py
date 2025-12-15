import itertools

def brute_force_planner(tasks, total_time):
    """
    tasks: list of dictionaries
    total_time: available hours
    """
    best_schedule = None
    max_productivity = 0

    for perm in itertools.permutations(tasks):
        current_time = 0
        productivity = 0
        schedule = []

        for task in perm:
            if current_time + task["duration"] <= total_time:
                current_time += task["duration"]
                productivity += task["priority"]
                schedule.append(task["name"])

        if productivity > max_productivity:
            max_productivity = productivity
            best_schedule = schedule

    return best_schedule, max_productivity


def get_user_input():
    tasks = []
    n = int(input("Enter the number of tasks: "))
    for i in range(n):
        name = input(f"Task {i+1} name: ")
        duration = float(input(f"Task {i+1} duration (hours): "))
        priority = float(input(f"Task {i+1} priority (e.g., 1-10): "))
        tasks.append({"name": name, "duration": duration, "priority": priority})
    
    total_time = float(input("Enter total available time (hours): "))
    return tasks, total_time


if __name__ == "__main__":
    tasks, total_time = get_user_input()
    best_schedule, max_productivity = brute_force_planner(tasks, total_time)
    
    print("\nBest task schedule:")
    for task in best_schedule:
        print(f"- {task}")
    print(f"Total productivity achieved: {max_productivity}")
