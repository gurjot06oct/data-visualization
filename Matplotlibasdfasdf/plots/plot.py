import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a basic plot
plt.plot(x, y)

# Add labels and a title
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Title of the Plot')

# Display the plot
plt.show()

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, 'bo', x, y2, 'go')
plt.legend()
plt.show()
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Multiple Lines')
plt.legend()  # Add a legend to differentiate the lines

# plt.plot(x, y, 'go--', linewidth=2, markersize=12)
plt.plot(x, y, color='green', marker='H', linestyle=':',
     linewidth=2, markersize=12)
plt.show()