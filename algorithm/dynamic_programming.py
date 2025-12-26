def dynamic_programming_schedule(tasks, total_time):
    """
    Dynamic Programming (0/1 Knapsack)
    Time Complexity: O(n * T)
    """
    n = len(tasks)
    T = int(total_time)

    dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for t in range(T + 1):
            duration = int(tasks[i - 1]["duration"])
            priority = tasks[i - 1]["priority"]

            if duration <= t:
                dp[i][t] = max(
                    dp[i - 1][t],
                    priority + dp[i - 1][t - duration]
                )
            else:
                dp[i][t] = dp[i - 1][t]

    # Backtracking to find selected tasks
    selected_tasks = []
    t = T

    for i in range(n, 0, -1):
        if dp[i][t] != dp[i - 1][t]:
            selected_tasks.append(tasks[i - 1]["name"])
            t -= int(tasks[i - 1]["duration"])

    selected_tasks.reverse()
    return selected_tasks, dp[n][T]
