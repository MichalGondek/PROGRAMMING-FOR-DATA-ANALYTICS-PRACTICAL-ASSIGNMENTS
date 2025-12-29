# Write a Jupyter notebook that displays a plot of this projected birth-rates

# Michal Gondek

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

birth = pd.read_csv(r"C:\Users\Administrator\Desktop\COLLEGE\PROGRAMMING-FOR-DATA-ANALYTICS-MY-WORK-main\data\birth_rates.csv")

pop   = pd.read_csv("population_by_age.csv")

# Plot birth rates
sns.lineplot(data=birth, x="Year", y="BirthRate", marker="o")
plt.title("Projected Birth Rates in Ireland")
plt.show()

# Aggregate ages into groups
bins  = [0,18,35,50,65,80,100]
labels = ["0-17","18-34","35-49","50-64","65-79","80+"]
pop["AgeGroup"] = pd.cut(pop["Age"], bins=bins, labels=labels)

# Plot population distribution by age group
sns.barplot(data=pop.groupby("AgeGroup")["Population"].sum().reset_index(),
            x="AgeGroup", y="Population")
plt.title("Population Distribution by Age Group")
plt.show()