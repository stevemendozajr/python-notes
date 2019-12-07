'''
Created by Steve Mendoza Jr. @stevemendozajr
Last updated 
'''

#rename columns of a dataframe
df.rename(columns={"A": "a", "B": "c"}, inplace=True)

##############################
###########replace############
##############################

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




