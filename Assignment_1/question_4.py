#📘 Scenario Question 
# A company surveyed the salaries of 1,000 employees. The average salary was around $50,000, with most employees earning 
# within a spread of about $10,000. 
# The HR department wants to visualize the distribution of salaries to understand pay structure and 
# identify whether salaries are # clustered around the average or spread out widely. # You are asked to: 
# - Plot a histogram showing the salary distribution. 
# - Add a title to make the chart clear. 
# - Interpret the chart: 
# - What does the shape of the distribution suggest about how salaries are spread? 
# - Are most employees earning close to the average, or is there a wide variation? 
# - How could HR use this information to review compensation policies?

import matplotlib.pyplot as plt
import numpy as np

salaries=np.random.normal(50000,10000,1000)

#Plot Histogram
plt.hist(salaries, bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary ($)")
plt.ylabel("Number of Employees")
plt.show()