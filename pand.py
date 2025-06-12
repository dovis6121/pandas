import pandas as pd
import numpy as np

def create_dataframe():
    data = {
        'Date': pd.date_range(start='2025-01-01', periods=5, freq='D'),
        'Temperature': [15, -5, 20, 0, -2],
        'Humidity': [30, 45, 50, 60, 40]
    }
    return pd.DataFrame(data)

def print_selected_rows(df):
    print("Second and fourth rows:")
    print(df.iloc[[1, 3]])

def print_non_negative_temperatures(df):
    print("\nRows with non-negative temperatures:")
    print(df[df['Temperature'] >= 0])

def print_total_temperature(df):
    total_temp = df['Temperature'].sum()
    print("\nTotal sum of temperatures:", total_temp)

def add_wind_and_cold_risk(df):
    df['Wind'] = np.random.randint(5, 26, size=len(df))
    df['Cold Risk'] = df['Temperature'].apply(lambda x: 'Yes' if x < 0 else 'No')
    return df

def categorize_wind_column(df):
    def categorize_wind(speed):
        if speed < 10:
            return 'Weak'
        elif 10 <= speed <= 20:
            return 'Moderate'
        else:
            return 'Strong'
    
    df['Wind'] = df['Wind'].apply(categorize_wind)
    return df

def print_avg_temp_by_cold_risk(df):
    grouped = df.groupby('Cold Risk')['Temperature'].mean()
    print("\nAverage temperature by Cold Risk:")
    print(grouped)

def print_sorted_by_temperature(df):
    sorted_df = df.sort_values(by='Temperature', ascending=False)
    print("\nSorted DataFrame by Temperature:")
    print(sorted_df)

def join_temperature_and_wind_data():
    df_temp = pd.DataFrame({
        'Date': pd.date_range(start='2025-01-01', periods=5),
        'Temperature': [10, -2, 18, 3, -7]
    }).set_index('Date')

    df_wind = pd.DataFrame({
        'Date': pd.date_range(start='2025-01-01', periods=5),
        'WindSpeed': [12, 7, 15, 20, 25]
    }).set_index('Date')

    joined_df = df_temp.join(df_wind)
    print("\nJoined DataFrame on Date:")
    print(joined_df)

# --- Main Execution ---
def main():
    df = create_dataframe()
    print_selected_rows(df)
    print_non_negative_temperatures(df)
    print_total_temperature(df)
    
    df = add_wind_and_cold_risk(df)
    df = categorize_wind_column(df)

    print_avg_temp_by_cold_risk(df)
    print_sorted_by_temperature(df)

    join_temperature_and_wind_data()

# Run the main function
if __name__ == "__main__":
    main()

