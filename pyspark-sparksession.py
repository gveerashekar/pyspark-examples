

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]") \
                    .appName('Around-sparksession') \
                    .getOrCreate()

print("First SparkContext:");
print("APP Name :"+spark.sparkContext.appName);
print("Master :"+spark.sparkContext.master);

sparkSession2 = SparkSession.builder \
      .master("local[1]") \
      .appName("sparksession-test") \
      .getOrCreate();

print("Second SparkContext:")
print("APP Name :"+sparkSession2.sparkContext.appName);
print("Master :"+sparkSession2.sparkContext.master);


sparkSession3 = SparkSession.newSession

print("Second SparkContext:")
print("APP Name :"+sparkSession3.sparkContext.appName);
print("Master :"+sparkSession3.sparkContext.master);