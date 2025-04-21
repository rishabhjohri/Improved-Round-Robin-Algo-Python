# main.py

from iwrr.vm import VM, Task
from iwrr.load_balancer import LoadBalancer
import pandas as pd
import random
from metrics_tracker import MetricsTracker
import os

# ----- CONFIG -----
NUM_VMS = 5
TIME_STEPS = 50
TASK_MAX_DURATION = 10
TASK_MAX_PRIORITY = 5
os.makedirs("logs", exist_ok=True)

def generate_tasks(n):
    return [Task(i, random.randint(1, TASK_MAX_DURATION), priority=random.randint(1, TASK_MAX_PRIORITY)) for i in range(n)]

def run_simulation(num_tasks):
    tracker = MetricsTracker()
    vms = [VM(vm_id=i, capacity=random.randint(5, 10)) for i in range(NUM_VMS)]
    balancer = LoadBalancer(vms)
    tasks = generate_tasks(num_tasks)
    task_log = []

    # Static + Dynamic Scheduling
    for task in tasks:
        vm_id = balancer.schedule_task(task)
        task_log.append((task.id, task.duration, task.priority, vm_id))

    # Simulation loop
    for t in range(TIME_STEPS):
        tracker.time_steps += 1
        for vm in vms:
            while len(vm.execution_list) < vm.capacity and vm.waiting_list:
                task = vm.waiting_list.pop(0)
                task.status = "running"
                vm.execution_list.append(task)

            for task in vm.execution_list:
                task.remaining -= 1
                if task.remaining <= 0:
                    task.status = "done"

            vm.execution_list = [task for task in vm.execution_list if task.status != "done"]

        balancer.migrate_tasks()
        for vm in vms:
            for task in vm.waiting_list + vm.execution_list:
                task.was_migrated = False
    # Export logs
    df = pd.DataFrame(task_log, columns=['TaskID', 'Duration', 'Priority', 'Initial_VM'])
    df.to_csv(f"logs/iwrr_assignment_{num_tasks}.csv", index=False)
    tracker.export(num_tasks=num_tasks, method="IWRR")

    print(f"[✓] IWRR run complete for {num_tasks} tasks.")

# ---- BATCH RUN FOR COMPARISON ----
if __name__ == "__main__":
    for num_tasks in range(10, 110, 10):
        run_simulation(num_tasks)
