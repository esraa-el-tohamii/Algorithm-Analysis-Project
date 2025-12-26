from utils.data_loader import load_tasks
from utils.performance import measure_performance
from charts import plot_results


from algorithms.brute_force import brute_force_all_solutions
from algorithms.greedy import greedy_schedule
from algorithms.dynamic_programming import dynamic_programming_schedule
from algorithms.divide_and_conquer import divide_and_conquer_schedule


FILE_PATH = "data/smart_planner_1000_inputs.csv"
TOTAL_TIME = 8
TASK_LIMIT = 7   # مهم جدًا للـ Brute Force


def print_result(name, schedule, productivity, time_taken, memory_used):
    print(f"\n{name} Algorithm Results")
    print("-" * 40)
    print("Schedule:", schedule)
    print("Productivity:", productivity)
    print(f"Execution Time: {time_taken:.6f} sec")
    print(f"Memory Usage: {memory_used:.2f} KB")


if __name__ == "__main__":
    
    results = []
    tasks = load_tasks(FILE_PATH, limit=TASK_LIMIT)

    # 1️⃣ Brute Force
    (bf_result, bf_time, bf_memory) = measure_performance(
        brute_force_all_solutions, tasks, TOTAL_TIME
    )
    bf_schedules, bf_productivity = bf_result
    results.append(("Brute Force", bf_productivity, bf_time, bf_memory))

    print_result(
        "Brute Force",
        bf_schedules[0],
        bf_productivity,
        bf_time,
        bf_memory
    )

    # 2️⃣ Greedy
    (greedy_result, g_time, g_memory) = measure_performance(
        greedy_schedule, tasks, TOTAL_TIME
    )
    greedy_schedule_result, greedy_productivity = greedy_result
    results.append(("Greedy", greedy_productivity, g_time, g_memory))

    print_result(
        "Greedy",
        greedy_schedule_result,
        greedy_productivity,
        g_time,
        g_memory
    )

    # 3️⃣ Dynamic Programming
    (dp_result, dp_time, dp_memory) = measure_performance(
        dynamic_programming_schedule, tasks, TOTAL_TIME
    )
    dp_schedule, dp_productivity = dp_result
    results.append(("Dynamic Programming", dp_productivity, dp_time, dp_memory))

    print_result(
        "Dynamic Programming",
        dp_schedule,
        dp_productivity,
        dp_time,
        dp_memory
    )

    # 4️⃣ Divide and Conquer
    (dc_result, dc_time, dc_memory) = measure_performance(
        divide_and_conquer_schedule, tasks, TOTAL_TIME
    )
    dc_schedule, dc_productivity = dc_result
    results.append(("Divide and Conquer", dc_productivity, dc_time, dc_memory))

    print_result(
        "Divide and Conquer",
        dc_schedule,
        dc_productivity,
        dc_time,
        dc_memory
    )
    plot_results(results)

