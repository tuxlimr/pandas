import pandas as pd
df = pd.read_csv('sample_data.csv')

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
print(df.columns)  

# read particular values from specific column
print(df['Name'][0:5])  # name is column name 
print(df[['Name', 'Type 1', 'Type 2']][0:5])  # Additional bracket and more cols 

# Rows 
print(df.iloc[1:4])

# to get the position of particular elemen
print(df.iloc[2,1]) # 2 is row and 1 is column here 

# iteration of rows and columns 

# for index, row in df.iterrows():
    # print(index, row['Name'])

# filter 
print(df.loc[df['Type 1']=="Grass"]) # Grass is a value which we want to filter from a particular column



