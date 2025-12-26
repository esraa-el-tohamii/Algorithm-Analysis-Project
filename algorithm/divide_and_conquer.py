def divide_and_conquer_schedule(tasks, total_time):
    """
    Divide and Conquer Approach
    Divides tasks into two halves and solves independently
    """

    if not tasks or total_time <= 0:
        return [], 0

    if len(tasks) == 1:
        if tasks[0]["duration"] <= total_time:
            return [tasks[0]["name"]], tasks[0]["priority"]
        else:
            return [], 0

    mid = len(tasks) // 2
    left_tasks = tasks[:mid]
    right_tasks = tasks[mid:]

    left_schedule, left_prod = divide_and_conquer_schedule(
        left_tasks, total_time / 2
    )

    right_schedule, right_prod = divide_and_conquer_schedule(
        right_tasks, total_time / 2
    )

    return left_schedule + right_schedule, left_prod + right_prod
