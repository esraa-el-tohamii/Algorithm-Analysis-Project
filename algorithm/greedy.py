def greedy_schedule(tasks, total_time):
    """
    Greedy Algorithm
    Sorts tasks by priority (highest first)
    Time Complexity: O(n log n)
    """
    tasks_sorted = sorted(tasks, key=lambda x: x["priority"], reverse=True)

    current_time = 0
    productivity = 0
    schedule = []

    for task in tasks_sorted:
        if current_time + task["duration"] <= total_time:
            current_time += task["duration"]
            productivity += task["priority"]
            schedule.append(task["name"])

    return schedule, productivity
