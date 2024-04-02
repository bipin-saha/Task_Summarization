import pandas as pd

# Read the two CSV files into pandas DataFrames
# Assuming file 1 doesn't have a column name for the 'Tracking' column
# Replace 'Tracking' with the actual column name if known
#df1 = pd.read_csv('x2.csv', names=['Tracking No'])
df2 = pd.read_csv('x1.csv')

# Compare the 'Tracking' columns between the two DataFrames
tracking_diff = df2.drop_duplicates(keep=False)

# Count the number of unique tracking numbers that are different between the two CSV files
unique_tracking_count = len(tracking_diff)

print("Number of unique tracking numbers that differ between the two CSV files:", unique_tracking_count)
