import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

x2 = [1, 2, 3, 4, 5]
y2 = [3, 4, 6, 8, 12]

plt.scatter(x, y, c='blue', label='Dataset 1')
plt.scatter(x2, y2, c='green', label='Dataset 2')
plt.legend()  # Add legend to differentiate datasets
plt.show()


# Create scatter plot
plt.scatter(x, y, s=10, c='red')  # All points in red  # Marker size of 100

# Display plot
plt.show()

colors = [20, 10, 30, 40, 50]  # Color intensity based on value
plt.scatter(x, y, c=colors, cmap='viridis', alpha=1)  # Using a colormap
plt.annotate('First Point', (x[0], y[0]), textcoords="offset points", xytext=(10,10), ha='center')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
plt.grid(True)  # Show grid lines
plt.colorbar(label='Color Intensity')
plt.show()
