import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)  # First subplot in a 2x1 grid
plt.plot([1, 2, 3], [1, 4, 9])
plt.plot([1, 2, 3], [1, 4, 10])
plt.subplot(2, 1, 2)  # Second subplot in a 2x1 grid
plt.plot([1, 2, 3], [1, 2, 3])

plt.show()

fig, ax = plt.subplots(2, 2)  # 2x2 grid of subplots

ax[0, 0].plot([1, 2, 3], [1, 4, 9])  # Top-left subplot
ax[0, 1].plot([1, 2, 3], [1, 2, 3])  # Top-right subplot
ax[1, 0].plot([1, 2, 3], [9, 4, 1])  # Bottom-left subplot
ax[1, 1].plot([1, 2, 3], [3, 6, 9])  # Bottom-right subplot

plt.show()

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
ax[0, 0].plot([1, 2, 3], [1, 4, 9])
ax[0, 1].plot([1, 2, 3], [1, 2, 3])
ax[1, 0].plot([1, 2, 3], [9, 4, 1])
ax[1, 1].plot([1, 2, 3], [3, 6, 9])
fig.tight_layout()  # Automatically adjusts subplot parameters
ax[0, 1].axis('off')  # Hide the top-right subplot
plt.show()
