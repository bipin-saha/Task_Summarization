import pandas as pd
import re
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Assign names to each column
df.columns = ['Column_1', 'Column_2', 'Column_3', 'Column_4', 'Column_5', 
              'Column_6', 'Column_7', 'category', 'Column_9', 'description']

# Replace NaN values in the 'description' column with an empty string
df['description'] = df['description'].fillna('')

# Remove non-English characters from the 'description' column
df['description'] = df['description'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', str(x)))

new_df = df[['category', 'description']].copy()

# Create separate DataFrames for each category
df_shortfall = new_df[new_df['category'] == 'Shortfall']
df_rejected = new_df[new_df['category'] == 'Rejected']

# Save the new DataFrames as CSV files
df_shortfall.to_csv('shortfall.csv', index=False)
df_rejected.to_csv('rejected.csv', index=False)


# Read the 'shortfall_merged.csv' file into a DataFrame
df_shortfall = pd.read_csv('shortfall_merged.csv')

# Read the 'rejected_merged.csv' file into a DataFrame
df_rejected = pd.read_csv('rejected_merged.csv')

# Keep only the 'summary' and 'dialogue' columns
df_shortfall = df_shortfall[['dialogue', 'summary']]
df_rejected = df_rejected[['dialogue', 'summary']]

# Save the new DataFrames as CSV files
df_shortfall.to_csv('shortfall_filtered.csv', index=False)
df_rejected.to_csv('rejected_filtered.csv', index=False)