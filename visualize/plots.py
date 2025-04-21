# visualize/plots.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("logs/simulation_metrics.csv")

# 1. Execution Time
plt.figure()
sns.lineplot(x="No. of tasks", y="Execution Time (ms)", hue="Method", data=df, marker="o")
plt.title("Execution Time vs No. of Tasks")
plt.savefig("logs/execution_time_plot.png")

# 2. Task Migration
plt.figure()
sns.lineplot(x="No. of tasks", y="Task Migration Time (ms)", hue="Method", data=df, marker="o")
plt.title("Task Migration Time vs No. of Tasks")
plt.savefig("logs/task_migration_plot.png")

# 3. Delayed Tasks
plt.figure()
sns.lineplot(x="No. of tasks", y="Delayed Tasks", hue="Method", data=df, marker="o")
plt.title("Delayed Tasks vs No. of Tasks")
plt.savefig("logs/delayed_task_plot.png")

# 4. Instructions Re-executed
plt.figure()
sns.lineplot(x="No. of tasks", y="Instructions Re-executed", hue="Method", data=df, marker="o")
plt.title("Instructions Re-executed vs No. of Tasks")
plt.savefig("logs/instructions_reexecuted_plot.png")

#import matplotlib.pyplot as plt

# Hardcoded sample data for different number of tasks
task_counts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
execution_time = [25, 48, 70, 92, 115, 140, 168, 193, 215, 245]
task_migrations = [1, 2, 3, 5, 6, 8, 10, 13, 15, 18]
delayed_tasks = [0, 1, 2, 3, 4, 6, 7, 9, 11, 12]
instructions_reexecuted = [0, 3, 6, 10, 14, 18, 24, 30, 38, 45]

plt.figure(figsize=(10, 6))

# Plot Execution Time
plt.plot(task_counts, execution_time, marker='o', linestyle='-', label='Execution Time (ms)')

# Plot Task Migrations
plt.plot(task_counts, task_migrations, marker='s', linestyle='--', label='Task Migrations')

# Plot Delayed Tasks
plt.plot(task_counts, delayed_tasks, marker='^', linestyle='-.', label='Delayed Tasks')

# Plot Instructions Re-executed
plt.plot(task_counts, instructions_reexecuted, marker='d', linestyle=':', label='Instructions Re-executed')

plt.title('IWRR Load Balancing Metrics')
plt.xlabel('Number of Tasks')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("logs/iwrr_metrics_plot.png")
plt.show()

# Hardcoded example data
task_counts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
execution_time = [25, 48, 70, 92, 115, 140, 168, 193, 215, 245]
task_migrations = [1, 2, 3, 5, 6, 8, 10, 13, 15, 18]
delayed_tasks = [0, 1, 2, 3, 4, 6, 7, 9, 11, 12]
instructions_reexecuted = [0, 3, 6, 10, 14, 18, 24, 30, 38, 45]

# 1. Execution Time Plot
plt.figure(figsize=(8, 5))
plt.plot(task_counts, execution_time, marker='o', linestyle='-')
plt.title('Execution Time vs Number of Tasks')
plt.xlabel('Number of Tasks')
plt.ylabel('Execution Time (ms)')
plt.grid(True)
plt.tight_layout()
plt.savefig("logs/execution_time_plot.png")
plt.close()

# 2. Task Migrations Plot
plt.figure(figsize=(8, 5))
plt.plot(task_counts, task_migrations, marker='s', linestyle='--')
plt.title('Task Migrations vs Number of Tasks')
plt.xlabel('Number of Tasks')
plt.ylabel('Number of Task Migrations')
plt.grid(True)
plt.tight_layout()
plt.savefig("logs/task_migration_plot.png")
plt.close()

# 3. Delayed Tasks Plot
plt.figure(figsize=(8, 5))
plt.plot(task_counts, delayed_tasks, marker='^', linestyle='-.')
plt.title('Delayed Tasks vs Number of Tasks')
plt.xlabel('Number of Tasks')
plt.ylabel('Delayed Tasks')
plt.grid(True)
plt.tight_layout()
plt.savefig("logs/delayed_task_plot.png")
plt.close()

# 4. Instructions Re-executed Plot
plt.figure(figsize=(8, 5))
plt.plot(task_counts, instructions_reexecuted, marker='d', linestyle=':')
plt.title('Instructions Re-executed vs Number of Tasks')
plt.xlabel('Number of Tasks')
plt.ylabel('Instructions Re-executed')
plt.grid(True)
plt.tight_layout()
plt.savefig("logs/instructions_reexecuted_plot.png")
plt.close()
