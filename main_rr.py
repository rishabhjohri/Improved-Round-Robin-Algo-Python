# main_rr.py

from iwrr.vm import VM, Task
from metrics_tracker import MetricsTracker
import random
import pandas as pd

def generate_tasks(n):
    return [Task(i, duration=random.randint(1, 5), priority=random.randint(1, 10)) for i in range(n)]

def run_simulation(num_tasks):
    vms = [VM(vm_id=i, capacity=5) for i in range(10)]
    tracker = MetricsTracker()

    # Round-robin assignment
    for i, task in enumerate(generate_tasks(num_tasks)):
        vms[i % len(vms)].waiting_list.append(task)

    TIME_STEPS = 50
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

            vm.execution_list = [t for t in vm.execution_list if t.status != "done"]

    tracker.export(num_tasks=num_tasks, method="RR")

if __name__ == "__main__":
    for n in range(10, 110, 10):
        run_simulation(n)
