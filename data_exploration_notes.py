'''
Created by Steve Mendoza Jr. @stevemendozajr
Last updated 12/11/2019
'''


##############################
######### overview ###########
##############################

#check datatypes of attributes
df.info()

#check datatypes of columns
df.dtypes 

#view all the datatypes within a single column
df['column_name'].apply(type)

#count number of rows and columns of dataframe
df.shape

#percentage of different values in a specific column/attribute
(df['column_name'].value_counts() / df['column_name'].shape[0])*100

#percentage of nulls in each column
(df.isnull().sum() / df.shape[0]) * 100


##############################
######## statistics ##########
##############################

#descriptive stats of dataframe
df.describe()

#descriptive stats of specific column in a groupby
df.groupby('column_name_to_group').column_name.describe()

#sum count of nulls per attribute
df.isnull().sum()

#value counts of attribute
df['column_name'].value_counts()

#view the values themselves from a value count in list form
df['column_name'].value_counts().index[:].tolist()

#percentage of value counts of an attribute
(df['column_name'].value_counts() / df['column_name'].shape[0])*100


##############################
######## filter/sort #########
##############################

#fitler columns of a specific datatype in a dataframe
df.select_dtypes(include='object') #object float int character

#sort by a column and overwrite original dataframe
df.sort_values(by='column_name', inplace=True)

#filter a dataframe on a column using loc/iloc
filtered_df = df.loc[df.column_name=='value']