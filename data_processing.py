import os
import pandas as pd

# Define the directory containing the CSV files
input_directory = 'path/to/your/csv_files'
output_directory = 'path/to/save/processed_files'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to process a single CSV file
def process_csv(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Example processing: Calculate total sales and filter records
    df['Total Sales'] = df['Quantity'] * df['Price']
    processed_df = df[df['Total Sales'] > 100]  # Filter records with Total Sales > 100
    
    return processed_df

# Process each CSV file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        input_file_path = os.path.join(input_directory, filename)
        processed_df = process_csv(input_file_path)
        
        # Save the processed data to a new CSV file in the output directory
        output_file_path = os.path.join(output_directory, f'processed_{filename}')
        processed_df.to_csv(output_file_path, index=False)

print("Data processing completed. Processed files are saved in the output directory.")