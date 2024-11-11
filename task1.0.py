import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('E:\\tasks\\API_SP.POP.TOTL_DS2_en_csv_v2_9949 (1).zip', compression='zip', skiprows=4)

# Filter out India's population data
india_data = data[data['Country Name'] == 'India']

# Extract only the population values across the years for India
year_columns = india_data.columns[4:-1]  # Exclude non-year columns and any NaN at the end
india_population = india_data[year_columns].values.flatten()

# Convert years to a list of integers for plotting
years = list(map(int, year_columns))

# 1. Plot India's Population Trend Over Time
plt.figure(figsize=(12, 6))
plt.plot(years, india_population, marker='o', color='b', label="India Population")
plt.title("India's Population Over Time")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(True)
plt.legend()
plt.show()

# 2. Calculate India's Year-on-Year Population Growth Rate
# Calculate the annual growth rate: (current year - previous year) / previous year * 100
india_growth_rate = ((pd.Series(india_population).pct_change()) * 100).values

# Plot the growth rate
plt.figure(figsize=(12, 6))
plt.plot(years[1:], india_growth_rate[1:], marker='o', color='g', label="India Population Growth Rate (%)")
plt.title("India's Year-on-Year Population Growth Rate")
plt.xlabel("Year")
plt.ylabel("Growth Rate (%)")
plt.grid(True)
plt.legend()
plt.show()

# 3. Highlight Key Population Milestones
# (Optional) You could add annotations for significant years if you have any specific milestones in mind.
# For example:
milestone_years = [1950, 2000, 2010, 2020]
for year in milestone_years:
    if year in years:
        plt.annotate(f'{year}', xy=(year, india_population[years.index(year)]), 
                     xytext=(year, india_population[years.index(year)] + 10000000),
                     arrowprops=dict(arrowstyle="->", color='gray'))

plt.show()
