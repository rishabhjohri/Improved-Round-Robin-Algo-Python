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
