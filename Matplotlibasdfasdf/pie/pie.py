import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [10,20,30,40]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels,autopct='%1.1f%%', hatch=['**O', 'oO', 'O.O', '.||.'])
plt.show()