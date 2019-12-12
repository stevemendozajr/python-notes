'''
Created by Steve Mendoza Jr. @stevemendozajr
Last updated 12/11/2019
'''


##############################
########### rename ###########
##############################

#rename columns of a dataframe
df.rename(columns={"A": "a", "B": "c"}, inplace=True)


##############################
####### remove/replace #######
##############################

#remove or replace a character from column names
df.columns.str.replace(' ', '_', inplace=True)

#remove/replace a character found inside entire dataframe using regex
df.replace(regex=r'^ba.$', value='new', inplace=True) 

#remove/replace a character found in a single column of a dataframe
df['column_name'] =  df['column_name'].str.replace('s', '', regex=True)

#replace specific cell values with a new value
df.replace(0, 5, inplace=True) #inplace true if you want to update original dataframe

#replace multiple specific cell values using a dictionary
df.replace({0: 10, 1: 100}, inplace=True) #inplace true if you want to update original dataframe

#replace specific cell value in multiple columns with the same new value
df.replace({'A': 0, 'B': 5}, 100, inplace=True) #inplace true if you want to update original dataframe

#replace specific values in a single column with new values
df.replace({'A': {0: 100, 4: 400}}, inplace=True) #inplace true if you want to update original dataframe


##############################
###### fill/drop nulls #######
##############################

#drop all rows if any null value present
df.dropna(axis=0, inplace=True) #inplace True to overwrite original dataframe

#drop every column that has all null values all the way down
df.dropna(axis=1, how='all', inplace=True) #how='any' for any nulls found

#fill all nulls in dataframe with a value
df.fillna(-1, inplace=True)

#fill nulls in a specific column with the column mean
df['column_name'].fillna((df['column_name'].mean()), inplace=True) #can be other stat as well

#fill nulls in a particular column
df['column_name'].fillna(value=-1, inplace=True)

#forward fill nulls in entire dataframe
df.fillna(method='ffill', inplae=True)


##############################
##### drop rows/columns ######
##############################

#drop columns using a list
df.drop(columns_list, axis=1, inplace=True)


##############################
###### change datatypes ######
##############################

#convert a column to a new datatype
df['column_name'] = df['column_name'].astype(int) #float int str character

#let pandas convert to a numeric datatype of float or int on its own
df['column_name']  pd.to_numeric(df['column_name'])

#convert to a datetime datatype
df['column_name']  pd.to_datetime(df['column_name'])