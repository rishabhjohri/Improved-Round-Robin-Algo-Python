#!/bin/bash

echo "📊 [START] Clearing old logs and plots..."
rm -f logs/*.csv logs/*.png

echo "🧠 Running IWRR Simulation (main.py)"
python3 main.py

echo "⚖️ Running WRR Simulation (main_wrr.py)"
python3 main_wrr.py

echo "🔄 Running RR Simulation (main_rr.py)"
python3 main_rr.py

echo "📈 Generating Comparison Plots (plots.py)"
python3 visualize/plots.py

echo "✅ All experiments complete. Results saved in /logs"
