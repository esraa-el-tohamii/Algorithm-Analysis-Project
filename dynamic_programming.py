def dynamic_programming_planner(tasks, total_time):
    n = len(tasks)
    # Initialize DP table
    dp = [[0 for _ in range(total_time + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for t in range(total_time + 1):
            if tasks[i - 1]["duration"] <= t:
                dp[i][t] = max(
                    dp[i - 1][t],
                    dp[i - 1][t - tasks[i - 1]["duration"]] + tasks[i - 1]["priority"]
                )
            else:
                dp[i][t] = dp[i - 1][t]

    # Traceback to find selected tasks
    t = total_time
    selected_tasks = []
    for i in range(n, 0, -1):
        if dp[i][t] != dp[i - 1][t]:
            selected_tasks.append(tasks[i - 1]["name"])
            t -= tasks[i - 1]["duration"]

    return selected_tasks[::-1], dp[n][total_time]


def get_user_input():
    tasks = []
    n = int(input("Enter the number of tasks: "))
    for i in range(n):
        name = input(f"Task {i+1} name: ")
        duration = int(input(f"Task {i+1} duration (hours): "))
        priority = int(input(f"Task {i+1} priority (e.g., 1-10): "))
        tasks.append({"name": name, "duration": duration, "priority": priority})
    
    total_time = int(input("Enter total available time (hours): "))
    return tasks, total_time


if __name__ == "__main__":
    tasks, total_time = get_user_input()
    best_schedule, max_productivity = dynamic_programming_planner(tasks, total_time)
    
    print("\nBest task schedule using Dynamic Programming:")
    for task in best_schedule:
        print(f"- {task}")
    print(f"Total productivity achieved: {max_productivity}")
