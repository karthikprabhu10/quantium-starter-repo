import pandas as pd
import os

# Define the directory containing the CSV files
data_dir = '.'

# List of CSV files
csv_files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

# Initialize an empty DataFrame to store combined data
combined_data = pd.DataFrame()

# Process each CSV file
for file in csv_files:
    # Load the data
    file_path = os.path.join(data_dir, file)
    df = pd.read_csv(file_path)
    
    # Filter rows where the product is 'pink morsel'
    df = df[df['product'] == 'pink morsel']
    
    # Create a 'sales' column by multiplying 'quantity' and 'price'
    df['sales'] = df['quantity'] * df['price']
    
    # Select the relevant columns
    df = df[['sales', 'date', 'region']]
    
    # Append the data to the combined DataFrame
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Save the combined data to a new CSV file
output_file = os.path.join(data_dir, 'formatted_sales_data.csv')
combined_data.to_csv(output_file, index=False)

print(f"Formatted data saved to {output_file}")
