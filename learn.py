import pandas as pd
import re
df = pd.read_csv('sample_data.csv')
# print(df.head())
# for txt file
# df = pd.read_csv('sample.txt')
# df = pd.read_csv('sample.txt',delimiter='\t')

# for excel , pip install xlrd addnal package required for the excel file

# df = pd.read_excel('sample.xlsx')

# for top three rows    
# print(df.head(3))
# for last three rows
# print(df.tail(3))

# Getting Columns
# print(df.columns)  

# find the count of cols
# print(len(df.columns))

# read particular values from specific column
# print(df['Name'][0:5])  # name is column name 
# print(df[['Name', 'Type 1', 'Type 2']][0:5])  # Additional bracket and more cols 

# Rows 
# print(df.iloc[1:4])

# to get the position of particular elemen
# print(df.iloc[2,1]) # 2 is row and 1 is column here 

# iteration of rows and columns 

# for index, row in df.iterrows():
    # print(index, row['Name'])

# filter 
# print(df.loc[df['Type 1']=="Grass"]) # Grass is a value which we want to filter from a particular column

# Sorting and describing
# Mean Standard Count etc. 
# print(df.describe())

# Sort values by name 


# print(df.sort_values('Name', ascending=False))#ascending and descending
# print(df.sort_values(['HP','Type 2'], ascending=[0,1]))#ascending and descending
        
# 
#changes to data 
df['Total']=  df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+\
            df['Sp. Def']+df['Speed']+df['Generation']


# print(df.head(100))  

# to drop any particular column 
# df = df.drop(columns=['Speed'])
# print(df.head(5))  

# to make addition ;
df['Total'] = df.iloc[:, 4:6].sum(axis=1)# axis=1 for x axis 
# print(df.head(5))

# Changing the position of column
# sce ; mv last col postion to fourth place 

cols =  list(df.columns)

df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# print(df.head(5))



# saving file to diff formats
# df.to_csv('modified.csv',index=False)
# df.to_csv('modified.txt',index=False, sep='\t')
# df.to_excel('modified.xls',index=False)

# filter data Part 2 

# df = df.loc[(df['Type 1']=='Grass') & (df['Type 2'] == "Poison")] # (and Operator)
# df = df.loc[(df['Type 1']=='Grass') & (df['Type 2'] == "Poison") & (df['HP'] > 70)] # (Or Operator)

# df.to_csv('filtered.csv')

# df = df.loc[df['Name'].str.contains('Mega')] # filter by specific words in names    
# df = df.loc[~df['Name'].str.contains('Mega')] # Reverse of previous one     
# df = df.loc[~df['Name'].str.contains('Mega|IVy', flags=re.I, regex=True)] # filter with Regex function Part 1     
# df = df.loc[df['Name'].str.contains('^pi[a-z]', flags=re.I, regex=True)] # Pi should be at the start of filter with Regex function Part 2    

# df.loc[df['Type 1'] == 'Fire'] = 'Flamer' #( Replace words )
# df.loc[df['Type 1'] == 'Flamer',['Generation','Legendary']] = 'Test Value' #(Replace words for more than one column)
# df.loc[df['Total'] > 500,['Generation','Legendary']] = 'Test Value' #(Replace words for more than one column)
# df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'


# Grouping
df = df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)  # mean
print(df.head(30))  