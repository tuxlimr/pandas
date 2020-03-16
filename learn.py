import pandas as pd
df = pd.read_csv('sample_data.csv')

# for txt file
# df = pd.read_csv('sample.txt')
# df = pd.read_csv('sample.txt',delimiter='\t')

# for excel , pip install xlrd addnal package required for the excel file

# df = pd.read_excel('sample.xlsx')

# for top three rows    
print(df.head(3))
# for last three rows
print(df.tail(3))