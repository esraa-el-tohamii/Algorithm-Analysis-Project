import itertools

def brute_force_all_solutions(tasks, total_time):
    """
    Brute Force Algorithm
    Tries all possible permutations of tasks
    Time Complexity: O(n!)
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
            best_schedules = [schedule]
        elif productivity == max_productivity:
            best_schedules.append(schedule)

    return best_schedules, max_productivity
