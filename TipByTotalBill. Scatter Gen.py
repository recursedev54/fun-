import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in dataset
tips = sns.load_dataset("tips")

# Create a scatter plot with seaborn
sns.scatterplot(x="total_bill", y="tip", hue="time", data=tips)

# Customize plot appearance
plt.title('Tip by Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

# Show the plot
plt.show()
