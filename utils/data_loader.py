import csv

def load_tasks(file_path, limit=7):
    tasks = []
    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= limit:
                break
            tasks.append({
                "name": f"Task_{row['task_id']}",
                "duration": float(row["task_duration"]),
                "priority": float(row["task_priority"])
            })
    return tasks
