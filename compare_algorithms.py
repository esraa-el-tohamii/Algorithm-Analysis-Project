from utils.data_loader import load_tasks
from utils.performance import measure_performance

from algorithms.brute_force import brute_force_all_solutions
from algorithms.greedy import greedy_schedule
from algorithms.dynamic_programming import dynamic_programming_schedule
from algorithms.divide_and_conquer import divide_and_conquer_schedule


FILE_PATH = "data/smart_planner_1000_inputs.csv"
TOTAL_TIME = 8
TASK_LIMIT = 7   # مهم للـ Brute Force


def compare():
    tasks = load_tasks(FILE_PATH, limit=TASK_LIMIT)

    results = []

    # Brute Force
    (res, t, m) = measure_performance(brute_force_all_solutions, tasks, TOTAL_TIME)
    _, prod = res
    results.append(("Brute Force", prod, t, m))

    # Greedy
    (res, t, m) = measure_performance(greedy_schedule, tasks, TOTAL_TIME)
    _, prod = res
    results.append(("Greedy", prod, t, m))

    # Dynamic Programming
    (res, t, m) = measure_performance(dynamic_programming_schedule, tasks, TOTAL_TIME)
    _, prod = res
    results.append(("Dynamic Programming", prod, t, m))

    # Divide and Conquer
    (res, t, m) = measure_performance(divide_and_conquer_schedule, tasks, TOTAL_TIME)
    _, prod = res
    results.append(("Divide and Conquer", prod, t, m))

    print("\nAlgorithm Comparison")
    print("-" * 60)
    print(f"{'Algorithm':<22}{'Productivity':<15}{'Time(sec)':<12}{'Memory(KB)'}")
    print("-" * 60)

    for alg, prod, time_taken, memory in results:
        print(f"{alg:<22}{prod:<15}{time_taken:<12.6f}{memory:.2f}")


if __name__ == "__main__":
    compare()
