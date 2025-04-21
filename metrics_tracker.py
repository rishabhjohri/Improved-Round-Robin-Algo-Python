# metrics_tracker.py

class MetricsTracker:
    def __init__(self):
        self.time_steps = 0
        self.task_migrations = 0
        self.delayed_tasks = 0
        self.total_instructions_reexecuted = 0

    def log_task_migration(self):
        self.task_migrations += 1

    def log_delayed_task(self, delay_time):
        self.delayed_tasks += 1
        self.total_instructions_reexecuted += delay_time

    def export(self, num_tasks, method="IWRR", filename="logs/simulation_metrics.csv"):
        import pandas as pd
        from os.path import exists

        row = {
            "No. of tasks": num_tasks,
            "Method": method,
            "Execution Time (ms)": self.time_steps,
            "Task Migration Time (ms)": round(self.task_migrations * 0.1, 2),
            "Delayed Tasks": self.delayed_tasks,
            "Instructions Re-executed": self.total_instructions_reexecuted,
        }

        if exists(filename):
            df = pd.read_csv(filename)
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        else:
            df = pd.DataFrame([row])
        df.to_csv(filename, index=False)
