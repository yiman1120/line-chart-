import numpy as np
import matplotlib.pyplot as plt

# Example data for two groups
time = [4, 5, 6]  # X-axis values: 4 months, 5 months, 6 months
mean_pemf = [3618.85, 3875.65, 5662.45]  # Mean values for PEMF group
SEM_pemf = [453.10, 552.44, 979.53]  # SEM for PEMF group

mean_sham = [3985.55, 7015.15, 5706.21]  # Mean values for Sham group
SEM_sham = [657.55, 2042.8, 848.78]  # SEM for Sham group

# Create a figure and axis
plt.figure(figsize=(8, 6))

# Plot the first group (PEMF) with error bars
plt.errorbar(time, mean_pemf, yerr=SEM_pemf, fmt='-o', capsize=5, label='PEMF')

# Plot the second group (Sham) with error bars
plt.errorbar(time, mean_sham, yerr=SEM_sham, fmt='-s', capsize=5, label='Sham')

# Customize the chart
plt.xlabel('post-op Time')
plt.xticks([4, 5, 6], ['4 months', '5 months', '6 months'])  # Custom X-axis labels
plt.ylabel('Side to side difference (mm) ')
plt.title('IPAQ (MET/week)')
# Place the legend on the left
plt.legend(loc='upper left')  # Legend position
plt.grid(True)

# Set the y-axis limits to start at 0 and extend to a higher value
plt.ylim(0, 14000)  # Adjust the upper limit as needed

# Set x-axis limits to create more space on the left
plt.xlim(3.5, 6.5)  # Adjust the limits as needed

# Show the chart
plt.show()