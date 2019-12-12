'''
Created by Steve Mendoza Jr. @stevemendozajr
Last updated 12/11/2019
'''

#create a new 2 category only column from an old column
df['new_column'] = np.where(df['column_name']>=50, 'yes', 'no')

#create a new 2 category only column from an old column using list comprehension
df['new_column'] = [1500 if x =='Music' else 800 for x in df['column_name']]

#create a new column using map function and dictionary
dictionary_map = {'old value': 'new value', 'old value 2': 'new value 2'}
df['new_column'] = df['column_name'].map(dictionary_map) 

#creat a new column using apply function
df['new_column'] = df['column_name'].apply(my_function, args =(another_param, ))