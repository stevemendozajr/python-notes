'''
Created by Steve Mendoza Jr. @stevemendozajr
Last updated 05/18/2020
'''


##############################
######## import data #########
##############################


# load a parquet file
df = spark.read.load('parquet file here', format='parquet')

# load in a csv file. also use for text files
df = spark.read.csv('csv file here', header=True, sep=',') # lots of other parameters you can edit as well


##############################
######## export data #########
##############################


# write to parquet
df.write.parquet('file path') # .mode('overwrite/append') if file already exists

# write to single csv
df.repartition(1).write.csv(path='file path and name', sep=',', header=True) # mode='overwrite/append' if file already exists


##############################
######## inpsect data ########
##############################


# count of rows
df.count()

# count of rows and columns
print((df.count(), len(df.columns)))

# show dataframe
df.show(n=5, vertical=True, truncate=False)

# see dataframe in row format
df.collect()

# view datatypes of columns
df.dtypes

# view schema of dataframe
df.schema

# print the schema of a dataframe
df.printSchema()

# view columns of dataframe
df.columns

# view summary stats of dataframe
df.describe().show()


##############################
######## filtering  ##########
##############################


# filter column equal to a specific value
df.filter(df['column1'] == 'value') 
df.where(df['column1'] == 'value') # where and filter are the exact same

# filter on multiple conditions
df.filter((f.col('column1') != f.col('column2')) & (f.col('column3') == f.col('column4')))

# filter for values not in a list of values
df.filter(df['column1'].isin(['value1', 'value2']) == False)

# filter for not null values
df.filter(df['column1'].isNotNull())


##############################
###### slicing/querying ######
##############################


# select certain columns from a dataframe
df.select('column1', 'column2', 'column3')

# select a certain column and rename as an alias
df.selct(df['column1'].alias('NewColumnName'))


##############################
#### feature engineering #####
##############################


# create a new calculated column based off another column
df = df.withColumn('NewColumnName', df['column1'].substr(5, 4))

# create a new column based on meeting multiple or/and condtions
df = df.withColumn('NewColumnName',\
    F.when((F.col('column1') == 'value1') | (F.col('column2') == 'value2'),'newvalue')\
    .otherwise('othervalue'))

# create a new column that is dependent on certain specific condition
df = df.withColumn('NewColumnName',\
    F.when(F.col('column1') == 'somevalue1', 'newvalue1')\
    .when(F.col('column2') == 'somevalue2', 'newvalue2')\
    .otherwise('other')\
    )

# rename a column
df = df.withColumnRenamed('OldColumnName', 'NewColumnName')

# remove a column from dataframe
df = df.drop('column1', 'column2')


##############################
######## joining data ########
##############################


# left join or inner join on 2 fields to create unique key
cond_join = [df_left['column1'] == df_right['column1'], df_left['column2'] == df_right['column2']]
df_joined = df_left.join(df_right, cond_join, 'left').select(df_left['*'],df_right['column1'],df_right['column2'])

# append dataframes together vertically - aka union

# unions by column position
df.union(df2) # same as SQL UNION ALL where we see duplicate records

df.union(df2).distinct() # no duplicate records

# unions by column name
df.unionByName(df2) # duplicate records

df.unionByName(df2).distinct() # no duplicate records


##############################
####### grouping data ########
##############################

# group data by 1 or more columns and perform an aggregate funciton
df_result = df.groupBy(['column1', 'column2']).agg({'column3': 'agg_function_here'}) # avg, sum, max, min, count, mean


##############################
########### misc. ############
##############################


# sort data ascending based on 1 or more columns
df_result = df.orderBy(['column2', 'column2'], ascending=[1, 1]) # 1 means true, 0 means false

# create a copy of dataframe - needed when you do multiple joins with same 2 tables
df_2 = df.alias('df2')

# cast a column to a new datatype
df = df.withColumn('column1', df['column1'].cast(DoubleType()))

# turn a field into row format, then create array of field values
column1_list = df.select('column1').collect()
column1_array = [row.column1 for row in column1_list]

# pivot a dataframe
df_result = df.groupBy('column1').pivot('column2', ['value1', 'value2']).sum('column3')


