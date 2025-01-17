import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

# Function to process and plot data
def process_and_plot_hardness_data(file_pattern, colors):
    # Load all text files matching the pattern
    file_paths = glob.glob(file_pattern)

    if not file_paths:
        print("No files found matching the pattern.")
        return

    # Read data into DataFrames
    data_frames = {
        file_path.split('/')[-1].split('.')[0]: pd.read_csv(file_path, sep="\t")
        for file_path in file_paths
    }

    # Extract distance labels from the first file (assuming uniform structure)
    distance_labels = [float(label) for label in data_frames[next(iter(data_frames))].columns[2:]]

    # Aggregate means and errors across all samples for each dataset
    average_means = {}
    average_stds = {}

    for key, df in data_frames.items():
        reshaped_df = df.melt(id_vars=["sample", "iteration"], var_name="Distance", value_name="Hardness")
        stats = reshaped_df.groupby("Distance")["Hardness"].agg(["mean", "std"]).reset_index()
        average_means[key] = stats["mean"]
        average_stds[key] = stats["std"]

    # Plotting averages across datasets
    fig, ax = plt.subplots(figsize=(10, 6))

    for idx, (key, means) in enumerate(average_means.items()):
        x = distance_labels
        y = means.values
        yerr = average_stds[key].values

        # Plot mean line
        ax.plot(
            x, y, marker='o', markersize=10, color=colors[idx % len(colors)], label=key, alpha=0.95
        )
        # Add fill_between for error range
        ax.fill_between(
            x, y - yerr, y + yerr, color=colors[idx % len(colors)], alpha=0.2
        )

    # Adjust x-axis ticks
    ax.set_xticks(np.arange(0, 2.5, 0.5))
    ax.tick_params(axis='both', which='both', direction='out', labelsize=14, length=6)

    # Set axis labels
    ax.set_xlabel("Distance from Center (cm)", fontsize=20)
    ax.set_ylabel("Hardness Value", fontsize=20)

    # Remove gridlines and title
    ax.grid(False)
    ax.set_title("")

    # Adjust legend font size
    ax.legend(fontsize=12, loc="upper left", bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()

# Parameters
file_pattern = "*.txt"  # Match all text files in the directory
colors = ['#ff0000', '#ffc5c5', '#bb4500', 
           '#4e9e4e', '#d0ffd0', '#00b89c', 
          '#0000ff', '#2b2bae', '#4e4e9e', '#cbcbff', '#7f00c9']

# Run the function
process_and_plot_hardness_data(file_pattern, colors)
