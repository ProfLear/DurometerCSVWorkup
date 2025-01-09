import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import glob

# Paths to the CSV files
# file_paths = glob.glob("RawData/*.csv")
file_paths = ['RawData\\R.csv', 'RawData\\RL.csv', 'RawData\\RLO.csv', 'RawData\\LR.csv', 'RawData\\LRO.csv', 'RawData\\O.csv', 'RawData\\OL.csv']


# Initialize lists to store data and labels
data_list = []
file_names = []  # Add more labels if needed
print(file_paths)
# Load the data
for file_path in file_paths:
    file_name = file_path.split("\\")[-1].split(".")[0]
    print(file_name)
    file_names.append(file_name)
    data = pd.read_csv(file_path, header=1)
    data.columns = ["Sample", 0, 0.5, 1, 1.5, 2]
    reshaped_data = data.melt(id_vars=["Sample"], var_name="Distance", value_name="Hardness").dropna()
    data_list.append(reshaped_data)

# Plot the data
colors = ['#f29898', '#c15555', '#781010', '#90d8ae', '#136b2e', '#9b9cd7', '#131463']  # Add more colors if needed
for i, (file_name, reshaped_data) in enumerate(zip(file_names, data_list)):
    stats = reshaped_data.groupby("Distance")["Hardness"].agg(["mean", "std", "count"])
    plt.plot(
        stats.index, stats["mean"], marker='o', markersize=10, color=colors[i % len(colors)], label=file_name, alpha=0.95
    )
    plt.fill_between(
        stats.index, stats["mean"] - stats["std"], stats["mean"] + stats["std"], color=colors[i % len(colors)], alpha=0.2
    )

# Customize plot appearance
fontsize = 20
plt.xlabel("Distance from Center (cm)", fontsize=fontsize)
plt.ylabel("Average Shore A Hardness", fontsize=fontsize)
plt.tick_params(axis='both', which='major', labelsize=fontsize, direction='out', length=6)
plt.tick_params(axis='both', which='minor', labelsize=fontsize, direction='out', length=4)

# Set y-axis ticks to increments of 5
y_max = max([reshaped_data["Hardness"].max() for reshaped_data in data_list])
plt.yticks(np.arange(0, int(y_max) + 1, 5))
plt.xticks([0, 0.5, 1, 1.5, 2])

plt.grid(False)
plt.axhline(y=0, color='black', linewidth=0.8)  # Show x-axis

# Add legend
plt.legend(fontsize=fontsize, frameon=False)

# Show the plot
plt.show()

# # Perform Tukey HSD tests for each pair of samples
# for file_name, reshaped_data in zip(file_names, data_list):
#     tukey_data = reshaped_data.copy()
#     tukey_data["Distance"] = tukey_data["Distance"].astype(str)  # Tukey test requires categorical grouping
#     tukey_result = pairwise_tukeyhsd(
#         tukey_data["Hardness"],
#         tukey_data["Distance"],
#         alpha=0.05
#     )
#     print(f"Tukey HSD Test Results for {file_name}")
#     print(tukey_result)
#     print("\n")