import yfinance as yf
import pandas as pd

# Define the ticker symbol
ticker = "^FTAS"

# Define the start and end dates
start_date = "2005-02-11"
end_date = "2025-03-25"

# Download the historical data from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)

# Reset the index to make 'Date' a regular column
data = data.reset_index()

# Display the first few rows of the data
print("First few rows of the data:")
print(data.head())

# Display the last few rows of the data
print("\nLast few rows of the data:")
print(data.tail())

# Save the data to a CSV file
data.to_csv("FTAS_historical_data.csv", index=False)

# Confirm the file has been saved
print("\nData has been saved to FTAS_historical_data.csv")

# Save the data to an Excel file
data.to_excel("FTAS_historical_data.xlsx", index=False)
print("\nData has been saved to FTAS_historical_data.xlsx")
