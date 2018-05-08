import os
os.environ["PYSPARK_PYTHON"] = "python3"
import functools 
from pyspark import SparkContext 
import pandas as pd
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.functions import explode
sc =SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
# Get information for .csv and transform in dataform 
df = sqlContext.read.load('artistToGaguiel.csv', 
                          format='com.databricks.spark.csv', 
                          header='false', 
                          inferSchema='true')

# Get top 10 of the beatles fan 
def top10_thebeatles(df):
	selected_information=df.select(['_c0','_c1','_c2']).rdd.map(lambda x: [x[0],x[1].split(';'),x[2].split(';')])
	result= selected_information.filter(lambda x: 'the beatles' in x[1]).top(10,lambda x: x[2][x[1].index('the beatles')])
	print("TOP 10- THE BEATLES FAN")
	for user in result:
		print(user[0])
	return result

# Get the most popular band 
def mostpopular_band(df):
	print("The  Most Popular Band")
	selected_information=df.select(['_c1']).rdd.repartition(6)
	information_set=selected_information.flatMap(lambda x: x[0].split(';')).map(lambda word: (word,1)).reduceByKey(lambda a, b: a + b)
	result=information_set.sortBy(lambda a: a[1],False).take(1)
	print(result)
	return result

# Get two users who share the largest amount of bands
def share_largestamountofbands(df):
	
	selected_information=df.select(['_c0','_c1'])
	map_information= selected_information.rdd.map(lambda x:[x[0],x[1].split(";")]).toDF()
	explode_information=map_information.select(['_1',explode(map_information._2).alias("bands")])
	explode_information.registerTempTable("data")
	sql_result=sqlContext.sql("SELECT t._1,t1._1, count(t._1) from data t, data t1 where t._1 != t1._1 and t.bands=t1.bands  group by t._1 , t1._1  order by  count(t._1) DESC")
	result=sql_result.rdd.take(1)
	print("USERS:")
	print(result)
	return result

#top10_thebeatles(df)
#mostpopular_band(df)
share_largestamountofbands(df)