'''
Created by Steve Mendoza Jr. @stevemendozajr
Last updated 
'''

#check datatypes of attributes
df.info()

#count number of rows and columns of dataframe
df.shape

#sum count of nulls per attribute
df.isnull().sum()

#value counts of attribute
df['column_name'].value_counts()

#percentage of value counts of an attribute
(df['column_name'].value_counts() / df['column_name'].shape[0])*100

#descriptive stats of dataframe
df.describe()

