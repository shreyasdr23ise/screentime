import matplotlib.pyplot as plt

# Data
ages = ['age 5', 'age 6', 'age 7', 'age 8', 'age 9']
frequency = [200, 400, 200, 200, 200]

# Plot
plt.bar(ages, frequency, color='cornflowerblue')

# Title and labels
plt.title('Age Distribution among Children Aged 5 to 9 Years.')
plt.ylabel('Frequency')

# Customize y-axis limits and ticks similar to the image
plt.ylim(0, 450)
plt.yticks(range(0, 451, 50))

# Show plot
plt.show()
