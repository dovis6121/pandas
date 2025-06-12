import pandas as pd
import numpy as np

# Create a DataFrame with at least 5 rows and 3 columns, one of which is temperature
data = {
    'Date': pd.date_range(start='2025-01-01', periods=5, freq='D'),
    'Temperature': [15, -5, 20, 0, -2],
    'Humidity': [30, 45, 50, 60, 40]
}
df = pd.DataFrame(data)

# Print the second and fourth rows
print("Second and fourth rows:")
print(df.iloc[[1, 3]])

# Print all rows where the temperature is not negative
print("\nRows with non-negative temperatures:")
print(df[df['Temperature'] >= 0])

# Calculate and print the total sum of the temperatures
total_temp = df['Temperature'].sum()
print("\nTotal sum of temperatures:", total_temp)

# Add a new column "Wind" with random values (between 5 and 25)
df['Wind'] = np.random.randint(5, 26, size=len(df))

# Add a column "Cold Risk" with "Yes" where temperature is less than 0
df['Cold Risk'] = df['Temperature'].apply(lambda x: 'Yes' if x < 0 else 'No')

# Change values in "Wind" column to "Weak", "Moderate", "Strong" using apply
def categorize_wind(speed):
    if speed < 10:
        return 'Weak'
    elif 10 <= speed <= 20:
        return 'Moderate'
    else:
        return 'Strong'

df['Wind'] = df['Wind'].apply(categorize_wind)

# Group by "Cold Risk" and calculate average temperature
grouped = df.groupby('Cold Risk')['Temperature'].mean()
print("\nAverage temperature by Cold Risk:")
print(grouped)

# Sort the DataFrame by "Temperature" in descending order
sorted_df = df.sort_values(by='Temperature', ascending=False)
print("\nSorted DataFrame by Temperature:")
print(sorted_df)

# Create two DataFrames and join them on "Date"
df_temp = pd.DataFrame({
    'Date': pd.date_range(start='2025-01-01', periods=5),
    'Temperature': [10, -2, 18, 3, -7]
}).set_index('Date')

df_wind = pd.DataFrame({
    'Date': pd.date_range(start='2025-01-01', periods=5),
    'WindSpeed': [12, 7, 15, 20, 25]
}).set_index('Date')

# Join the two DataFrames using join (index-based)
joined_df = df_temp.join(df_wind)
print("\nJoined DataFrame on Date:")
print(joined_df)
