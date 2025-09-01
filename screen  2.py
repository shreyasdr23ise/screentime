import matplotlib.pyplot as plt
import numpy as np

# Categories and groups
groups = ['Male', 'Female']
activities = ['watching TV', 'using smart phone', 'using Tablet', 'using computer']

# Data: frequencies for each group and activity
data = {
    'watching TV': [580, 390],
    'using smart phone': [590, 200],
    'using Tablet': [460, 290],
    'using computer': [300, 120]
}

# Bar width and positions
bar_width = 0.2
x = np.arange(len(groups))

# Create bars for each activity
plt.bar(x - 1.5*bar_width, data['watching TV'], width=bar_width, label='watching TV')
plt.bar(x - 0.5*bar_width, data['using smart phone'], width=bar_width, label='using smart phone')
plt.bar(x + 0.5*bar_width, data['using Tablet'], width=bar_width, label='using Tablet')
plt.bar(x + 1.5*bar_width, data['using computer'], width=bar_width, label='using computer')

# Labels and title
plt.ylabel('Frequency')
plt.xticks(x, groups)
plt.ylim(0, 700)
plt.yticks(np.arange(0, 701, 100))
plt.legend()

# Customize y-axis label orientation
plt.gca().set_ylabel('Frequency', rotation=90, labelpad=15)

plt.show()
