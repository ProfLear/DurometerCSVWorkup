import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Paths to the CSV files
file_1 = "RawData/48h-rt.csv"
file_2 = "RawData/laser_RT.csv"
file_3 = "RawData/laser_RT_oven.csv"

file_1_name = file_1.split("/")[-1].split(".")[0]
file_2_name = file_2.split("/")[-1].split(".")[0]
file_3_name = file_3.split("/")[-1].split(".")[0]

# Load the data
data_1 = pd.read_csv(file_1, header=1)
data_2 = pd.read_csv(file_2, header=1)
data_3 = pd.read_csv(file_3, header=1)

# Rename columns for clarity
data_1.columns = ["Sample", 0, 0.5, 1, 1.5, 2]
data_2.columns = ["Sample", 0, 0.5, 1, 1.5, 2]
data_3.columns = ["Sample", 0, 0.5, 1, 1.5, 2]

# Reshape data for analysis
reshaped_1 = data_1.melt(id_vars=["Sample"], var_name="Distance", value_name="Hardness").dropna()
reshaped_2 = data_2.melt(id_vars=["Sample"], var_name="Distance", value_name="Hardness").dropna()
reshaped_3 = data_3.melt(id_vars=["Sample"], var_name="Distance", value_name="Hardness").dropna()

# Calculate means and standard deviations
stats_1 = reshaped_1.groupby("Distance")["Hardness"].agg(["mean", "std", "count"])
stats_2 = reshaped_2.groupby("Distance")["Hardness"].agg(["mean", "std", "count"])
stats_3 = reshaped_3.groupby("Distance")["Hardness"].agg(["mean", "std", "count"])

# Plot the data
plt.errorbar(
    stats_1.index, stats_1["mean"], yerr=stats_1["std"], fmt='o', 
    markersize=20, capsize=10, capthick=2, color='steelblue', ecolor='steelblue', elinewidth=1.5, 
    label=file_1_name, alpha=0.95
)
plt.errorbar(
    stats_2.index, stats_2["mean"], yerr=stats_2["std"], fmt='o', 
    markersize=20, capsize=10, capthick=2, color='indianred', ecolor='indianred', elinewidth=1.5, 
    label=file_2_name, alpha=0.95
)
plt.errorbar(
    stats_3.index, stats_3["mean"], yerr=stats_3["std"], fmt='o', 
    markersize=20, capsize=10, capthick=2, color='mediumseagreen', ecolor='mediumseagreen', elinewidth=1.5, 
    label=file_3_name, alpha=0.95
)

# Customize plot appearance
fontsize = 20
plt.xlabel("Distance from Center (cm)", fontsize=fontsize)
plt.ylabel("Average Shore A Hardness", fontsize=fontsize)
plt.tick_params(axis='both', which='major', labelsize=fontsize, direction='out', length=6)
plt.tick_params(axis='both', which='minor', labelsize=fontsize, direction='out', length=4)

# Set y-axis ticks to increments of 5
y_max = max(stats_1["mean"].max(), stats_2["mean"].max(), stats_3["mean"].max())
plt.yticks(np.arange(0, int(y_max) + 1, 5))
plt.xticks([0, 0.5, 1, 1.5, 2])

plt.grid(False)
plt.axhline(y=0, color='black', linewidth=0.8)  # Show x-axis

# Add legend
plt.legend(fontsize=fontsize, frameon=False)

# Show the plot
plt.show()

# Perform Tukey HSD tests for each pair of samples
for label, data in [
    ("RT", reshaped_1),
    ("Laser RT Oven", reshaped_2),
    ("Laser RT", reshaped_3)
]:
    tukey_data = data.copy()
    tukey_data["Distance"] = tukey_data["Distance"].astype(str)  # Tukey test requires categorical grouping
    tukey_result = pairwise_tukeyhsd(
        tukey_data["Hardness"],
        tukey_data["Distance"],
        alpha=0.05
    )
    print(f"Tukey HSD Test Results for {label}")
    print(tukey_result)
    print("\n")
