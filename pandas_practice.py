from os import name
import pandas as pd 

df = pd.read_csv('pokemon_data.csv')

# prints top 3 
print(df.head(3)) 

# prints bottom 3 
print(df.tail(3)) 

# read Headers
print(df.columns)

#read specific column
print(df['Name'])

#read specific columns and number wanted
print(df['Name'][0:5])

#read more than one column
print(df[['Name', 'Type 1', 'HP',]][0:5])

# read specific rows
print(df.iloc[1:4])

# read a specific location (fig of data)
print(df.iloc[2,1])
# OR
for index, row in df.iterrows():
    print(index,row['Name'])

# Used to find specific data - not always interger based 
print(df.loc[df['Type 1'] == "Water"])

# prints values
print(df.describe())

# Sort values to be read in desired way
print(df.sort_values('Name', ascending = False))

# Sort values to be read in desired way
print(df.sort_values(['Type 1', 'HP'], ascending =[1,0]))


# Add a column
df['Total'] = df['HP'] + df['Attack'] + df['Defence'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))

# Delete column 
df = df.drop(columns=['Legendary'])
print(df.head(5))

# Save to CSV
df.to_csv('modified.csv')

# Filtering Data
print(df.loc[df['Type 1'] == 'Grass'])
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])

# Create new database containing filtered data only - part 1
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# new_df.to_csv('filtered.csv')

# Reset index for new databases (created from filtered data) - part 2
new_df = new_df.reset_index()




