import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. User Input Handling
print("Welcome to the Data Science Script!")
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# Ask user to select a cryptocurrency
crypto = input("Enter the cryptocurrency you want to analyze (e.g., bitcoin, ethereum): ").lower()
days = input("Enter the number of days of historical data you want to retrieve (e.g., 30, 90, 180): ")

# 2. Connecting to an API
print(f"\nFetching data for {crypto} for the last {days} days...")

url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart"
params = {'vs_currency': 'usd', 'days': days}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Data fetched successfully!\n")
else:
    print("Failed to fetch data. Please check the cryptocurrency name and try again.")
    exit()

# 3. Data Manipulation
# Extracting prices from the response
prices = data['prices']
df = pd.DataFrame(prices, columns=['Timestamp', 'Price'])
df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
df = df[['Date', 'Price']]

# User input to perform a simple analysis
analysis_choice = input("Choose an analysis:\n1. Show the first 5 rows of data\n2. Show summary statistics\n3. Find the highest price\n4. Plot the price trend\nEnter the number of your choice: ")

# 4. Data Analysis and Visualization
if analysis_choice == '1':
    print("\nFirst 5 rows of the data:")
    print(df.head())
elif analysis_choice == '2':
    print("\nSummary Statistics:")
    print(df.describe())
elif analysis_choice == '3':
    max_price = df['Price'].max()
    max_date = df.loc[df['Price'].idxmax(), 'Date']
    print(f"\nThe highest price was ${max_price:.2f} on {max_date}.")
elif analysis_choice == '4':
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Price'], label=f'{crypto.capitalize()} Price')
    plt.title(f'{crypto.capitalize()} Price Trend over Last {days} Days')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()
else:
    print("Invalid choice! Please run the script again.")

print("\nThank you for using the script!")

