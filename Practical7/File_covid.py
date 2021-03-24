import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

os.chdir("D:/pythonProject")


covid_data = pd.read_csv("full_data.csv")
covid_data.head(7)

print(covid_data.iloc[0:12:2,])

my_columns = [True, True, False, True, False, False]

print(covid_data.loc[covid_data['location'] == "Afghanistan","total_cases"])

world_new_cases = covid_data.loc[covid_data['location']=="World","new_cases"]

a = np.array(world_new_cases)
mean = np.mean(a)
median = np.median(a)
print(mean,median)

plt.boxplot(a, vert=True, whis=1.5, patch_artist=True, meanline=True, showbox=True, showcaps=True, showfliers=True, boxprops= {'facecolor':'orange'})
plt.title("new cases worldwide")
plt.xlabel("worldwide")
plt.ylabel("number")
plt.show()

world_dates = covid_data.loc[covid_data['location'] == "World","date"]
world_deaths = covid_data.loc[covid_data['location'] == "World","new_deaths"]
plt.plot(world_dates, world_new_cases, 'bo', label='new cases')
plt.plot(world_dates, world_deaths, 'yo', label='deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-60, fontsize=6)
plt.title("new cases and deaths worldwide")
plt.xlabel("date")
plt.ylabel("number")
plt.legend()
plt.show()

Spain = covid_data.loc[(covid_data['location'] == "Spain"), ["date","new_cases","total_cases"]]
plt.plot(Spain.date, Spain.new_cases, 'bo', label='new cases')
plt.plot(Spain.date, Spain.total_cases, 'go', label='total cases')
plt.title("new cases and total cases developed over time in Spain")
plt.xticks(Spain.date.iloc[0:len(Spain.date):4],rotation=-60, fontsize=6)
plt.xlabel("date")
plt.ylabel("number")
plt.legend()
plt.show()


