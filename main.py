import datetime
import json
import sys
import os
from tabulate import tabulate

# 定义任务列表
tasks = []

def add_task(task_type, status):
    task = {
        "type": task_type,
        "status": status,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks()

def save_tasks():
    folder_path = "tasks/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = folder_path + datetime.datetime.now().strftime("%Y-%m-%d") + "_tasks.json"
    with open(file_path, "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        folder_path = "tasks/"
        file_path = folder_path + datetime.datetime.now().strftime("%Y-%m-%d") + "_tasks.json"
        with open(file_path, "r") as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        pass

def summary():
    table = []
    headers = ["Task Type", "Start Time", "End Time", "Duration"]
    for i in range(0, len(tasks), 2):
        task_start = tasks[i]
        task_end = tasks[i+1]
        start_time = datetime.datetime.strptime(task_start["time"], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.strptime(task_end["time"], "%Y-%m-%d %H:%M:%S")
        duration = end_time - start_time
        table.append([task_start["type"], start_time.strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S"), duration])

    print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    load_tasks()

    if len(sys.argv) > 1:
        if sys.argv[1] == "summary":
            summary()
        else:
            task_type = sys.argv[1]
            status = sys.argv[2]
            add_task(task_type, status)

