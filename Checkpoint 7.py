import numpy as np
import pandas as pd

my_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(my_data, index=labels)

# delete rows with NaN values
df = df.dropna()
print(df)

#First three rows
print(df.head(3))

#Extract 'name' and 'score' columns
df = df[['name', 'score']]
print(df)

#Add new row
df.loc['k'] = ['Suresh', 15.5]
print(df)


#Delete 'attempts' column by duplicationg the dict since we already deleted this column and we may have errors

my_data2 = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2 = pd.DataFrame(my_data2, index=labels)

df2.drop('attempts', axis=1, inplace=True)

print(df2)

#Add new column 'Success'
df['Success'] = np.where(df['score'] > 10, 1, 0)
print(df)

#Export to CSV
df.to_csv('my_data_final.csv')
