import itertools

def brute_force_all_solutions(tasks, total_time):
    """
    Returns all task orders that achieve the maximum productivity
    """
    max_productivity = 0
    best_schedules = []

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
            best_schedules = [schedule]  # start a new list
        elif productivity == max_productivity:
            best_schedules.append(schedule)  # add to existing list

    return best_schedules, max_productivity


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
    best_schedules, max_productivity = brute_force_all_solutions(tasks, total_time)
    
    print(f"\nMaximum productivity achievable: {max_productivity}")
    print(f"Number of optimal schedules: {len(best_schedules)}\n")
    
    for idx, schedule in enumerate(best_schedules, 1):
        print(f"Optimal Schedule {idx}:")
        for task in schedule:
            print(f"- {task}")
        print()
