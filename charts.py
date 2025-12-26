import matplotlib.pyplot as plt


def plot_results(results):
    algorithms = [r[0] for r in results]
    productivity = [r[1] for r in results]
    time_taken = [r[2] for r in results]
    memory_used = [r[3] for r in results]

    # نافذة واحدة + مسافات أكبر
    fig, axs = plt.subplots(3, 1, figsize=(10, 13))

    # =========================
    # 1️⃣ Productivity
    # =========================
    axs[0].plot(algorithms, productivity, marker='o', linestyle='-')
    axs[0].set_title("Productivity Comparison", pad=15)
    axs[0].set_ylabel("Productivity")

    # =========================
    # 2️⃣ Execution Time
    # =========================
    axs[1].plot(algorithms, time_taken, marker='o', linestyle='-', color='orange')
    axs[1].set_title("Execution Time Comparison", pad=15)
    axs[1].set_ylabel("Time (seconds)")

    # =========================
    # 3️⃣ Memory Usage
    # =========================
    axs[2].plot(algorithms, memory_used, marker='o', linestyle='-', color='green')
    axs[2].set_title("Memory Usage Comparison", pad=15)
    axs[2].set_ylabel("Memory (KB)")
    axs[2].set_xlabel("Algorithm")

    # زيادة المسافات بين الرسومات
    plt.subplots_adjust(hspace=0.6)

    plt.show()
