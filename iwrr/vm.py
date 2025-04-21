# iwrr/vm.py

class Task:
    def __init__(self, task_id, duration, priority=0):
        self.id = task_id
        self.duration = duration  # total duration
        self.remaining = duration  # for simulation
        self.priority = priority
        self.status = "waiting"  # could be: waiting, running, paused, done
        self.was_migrated = False  

    def __repr__(self):
        return f"Task-{self.id}(P:{self.priority}, D:{self.duration}, R:{self.remaining}, {self.status})"


class VM:
    def __init__(self, vm_id, capacity):
        self.id = vm_id
        self.capacity = capacity  # number of tasks it can handle concurrently
        self.execution_list = []  # running tasks
        self.pause_list = []      # paused tasks
        self.waiting_list = []    # queued tasks

    def current_load(self):
        return len(self.execution_list) + len(self.waiting_list)

    def total_execution_time(self):
        return sum(task.remaining for task in self.execution_list)

    def __repr__(self):
        return f"VM-{self.id} | Cap: {self.capacity} | Exec: {len(self.execution_list)} | Wait: {len(self.waiting_list)}"
