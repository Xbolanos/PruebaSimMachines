from pyspark import SparkContext 
import pandas as pd
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
sqlContext = SQLContext(sc)
df = sqlContext.read.load('artistToGaguiel.csv', 
                          format='com.databricks.spark.csv', 
                          header='false', 
                          inferSchema='true')

rows=df.take(df.count())

list_temp=rows[0][0].split('\"')
print(list_temp[1])

