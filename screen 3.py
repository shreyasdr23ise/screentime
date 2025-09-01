import matplotlib.pyplot as plt
import numpy as np

# Categories and groups
time_spent = ['1 hour', '2 hour', 'more than 3 hours', "don't watch"]
frequency_labels = ['daily', 'several times in a week', 'once in a week', 'rarely']

# Data: frequencies for each time_spent category and frequency label
data = {
    'daily': [50, 20, 10, 120],
    'several times in a week': [60, 35, 15, 10],
    'once in a week': [260, 80, 20, 0],
    'rarely': [200, 105, 160, 0]
}

# Bar width and positions
bar_width = 0.2
x = np.arange(len(time_spent))

# Plot bars for each frequency label
plt.bar(x - 1.5*bar_width, data['daily'], width=bar_width, label='daily')
plt.bar(x - 0.5*bar_width, data['several times in a week'], width=bar_width, label='several times in a week')
plt.bar(x + 0.5*bar_width, data['once in a week'], width=bar_width, label='once in a week')
plt.bar(x + 1.5*bar_width, data['rarely'], width=bar_width, label='rarely')

# Labels and title
plt.ylabel('Frequency')
plt.xticks(x, time_spent)
plt.ylim(0, 300)
plt.yticks(np.arange(0, 301, 50))
plt.legend()

# Customize y-axis label orientation
plt.gca().set_ylabel('Frequency', rotation=90, labelpad=15)

plt.show()
