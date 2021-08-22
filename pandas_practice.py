from os import name
import pandas as pd 

df = pd.read_csv('pokemon_data.csv')

# prints top 3 
# print(df.head(3)) 

# prints bottom 3 
# print(df.tail(3)) 

# read Headers
# print(df.columns)

#read specific column
# print(df['Name'])


#read specific columns and number wanted
# print(df['Name'][0:5])

#read more than one column
# print(df[['Name', 'Type 1', 'HP',]][0:5])

# read specific rows
# print(df.iloc[1:4])

# read a specific location (fig of data)
# print(df.iloc[2,1])
# # OR
# for index, row in df.iterrows():
#     print(index,row['Name'])

# Used to find specific data - not always interger based 
# print(df.loc[df['Type 1'] == "Water"])

# prints values
# print(df.describe())

# Sort values to be read in desired way
# print(df.sort_values('Name', ascending = False))

# Sort values to be read in desired way
print(df.sort_values(['Type 1', 'HP'], ascending =[1,0]))