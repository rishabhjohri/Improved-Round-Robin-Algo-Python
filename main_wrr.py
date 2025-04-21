# main_wrr.py

from iwrr.vm import VM, Task
from metrics_tracker import MetricsTracker
import random
import pandas as pd

def generate_tasks(n):
    return [Task(i, duration=random.randint(1, 5), priority=random.randint(1, 10)) for i in range(n)]

def run_simulation(num_tasks):
    vms = [VM(vm_id=i, capacity=random.randint(3, 10)) for i in range(10)]
    tracker = MetricsTracker()

    # Create tasks
    tasks = generate_tasks(num_tasks)

    # WRR Scheduler (simple static weighted round robin)
    weights = [vm.capacity for vm in vms]
    total_weight = sum(weights)
    vm_distribution = []
    for i, w in enumerate(weights):
        vm_distribution.extend([i] * w)

    vm_index = 0
    for task in tasks:
        vm_id = vm_distribution[vm_index % len(vm_distribution)]
        vms[vm_id].waiting_list.append(task)
        vm_index += 1

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

    tracker.export(num_tasks=num_tasks, method="WRR")

if __name__ == "__main__":
    for n in range(10, 110, 10):
        run_simulation(n)
