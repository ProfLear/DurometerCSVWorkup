import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Set the path to your folder containing the CSV files
dataFolder = "RawData"

# Define the sample order and load files
fileOrder = ["48h-RT", "Laser_48h-RT", "Laser_RT_Oven"]
filePaths = {sample: os.path.join(dataFolder, f"{sample}.csv") for sample in fileOrder}

# Prepare data storage for plotting
data_summary = {}

# Process each file
for sample_name, file_path in filePaths.items():
    # Load the CSV, skipping the first row (sample type)
    df = pd.read_csv(file_path, skiprows=1)
    
    # Positions (second row, no header in file)
    positions = df.columns.astype(float)
    
    # Convert measurement rows to numeric, calculate means and stds
    measurements = df.apply(pd.to_numeric, errors='coerce')
    mean_values = measurements.mean()
    std_values = measurements.std()
    
    # Store processed data
    data_summary[sample_name] = {
        "positions": positions,
        "means": mean_values,
        "stds": std_values
    }

# Calculate bar width and offset dynamically based on the number of samples
num_samples = len(data_summary)
total_width = 0.6  # Total width allocated for each cluster on the x-axis (adjustable)
bar_width = total_width / num_samples * 0.7 # Bar width so bars within cluster touch
cluster_offset = bar_width * (num_samples + 0.5) / 2  # Offset to center clusters, with separation outside clusters

# Plotting with calculated bar width and cluster offset
plt.figure(figsize=(14, 8))
font_size = 18  # Set global font size

# Define color map for the remaining samples
colors = plt.cm.viridis(np.linspace(0, 1, num_samples))

# Plot each sample with dynamically calculated bar width and offset
for i, (sample_name, data) in enumerate(data_summary.items()):
    # Offset positions to center clusters around each x-tick and create space between clusters
    offset_positions = data["positions"] + (i - num_samples / 2 + 0.5) * bar_width
    # Bar plot with error bars
    plt.bar(offset_positions, data["means"], yerr=data["stds"], 
            label=sample_name, alpha=0.7, color=colors[i], width=bar_width, capsize=3)

# Labels, tick formatting, and legend
plt.xlabel("Position (cm from center)", fontsize=font_size)
plt.ylabel("Average Shore A Hardness", fontsize=font_size)
plt.xticks(data["positions"], fontsize=font_size)  # Position x-ticks at central positions
plt.yticks(fontsize=font_size)
plt.legend(title="Sample Type", fontsize=font_size, title_fontsize=font_size)
plt.gca().tick_params(axis='both', which='both', direction='out', length=6)

# Remove grid lines and title
plt.gca().grid(False)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()