from pyspark import SparkContext 
from pyspark.sql import SQLContext 
import pandas as pd
myrdd = sc.textFile("artistToGaguiel.csv").map(lambda line: line.split(","))
print(myrdd)
