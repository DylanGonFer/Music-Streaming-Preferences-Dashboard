import pandas as pd

# Load the CSV file and set 'User_ID' as index
df = pd.read_csv("Global_Music_Streaming_Listener_Preferences.csv", index_col="User_ID")

# Delete rows where 'User_ID' is null
df = df.dropna(subset=['User_ID'])

# Imputation of missing values ​​in the 'Age' column using the median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill null values ​​in categorical columns with 'Unknown' or generic values
df['Country'] = df['Country'].fillna('Unknown')
df['Streaming Platform'] = df['Streaming Platform'].fillna('Unknown')
df['Top Genre'] = df['Top Genre'].fillna('Unknown')
df['Most Played Artist'] = df['Most Played Artist'].fillna('Unknown')
df['Subscription Type'] = df['Subscription Type'].fillna('Unknown')
df['Listening Time (Morning/Afternoon/Night)'] = df['Listening Time (Morning/Afternoon/Night)'].fillna('Sin información')

# Fill null values ​​in numeric columns with the mean or specific values
df['Minutes Streamed Per Day'] = df['Minutes Streamed Per Day'].fillna(df['Minutes Streamed Per Day'].mean())
df['Number of Songs Liked'] = df['Number of Songs Liked'].fillna(0)
df['Discover Weekly Engagement (%)'] = df['Discover Weekly Engagement (%)'].fillna(df['Discover Weekly Engagement (%)'].mean())
df['Repeat Song Rate (%)'] = df['Repeat Song Rate (%)'].fillna(df['Repeat Song Rate (%)'].median())

# Save the cleaned DataFrame to a new CSV file
df.to_csv("clean_dataset.csv", index=False)
