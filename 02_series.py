# A pandas series is like a column in a table. it is 1D array which holds any type of data
#here we will create a simple pandas series
import pandas as pd

# abhay=[1,7,2]
# abhaynew = pd.Series(abhay)
# print(abhaynew)

# to access a perticular element using indexing

#labeling - lable can be used to access a specified value

# abhay=[1,7,2]
# abhaynew = pd.Series(abhay)
# print(abhaynew[0])

# we can also label our own type of indexing

# abhay=[1,7,2]
# abhaynew = pd.Series(abhay,index=["x","y","z"])
# print(abhaynew["y"])

# you can also use a key or value object like a dictionary,when creating a series
#here we will create a simple pandas series from pandas dictionary.

# cal={"day1":420,"day2":380,"day3":320}
# abhaynew=pd.Series(cal)
# print(abhaynew)


# now we will create a series from only day1 and day 2

# cal={"day1":420,"day2":380,"day3":320}
# abhaynew=pd.Series(cal,index=["day1","day2"])
# print(abhaynew)

#Dataframes: datasets  in pandas are usually multidimensional tables and they are called dataframes
# series are like columns and dataframes is the whole table
#Now we will create a dataframe from two tables


abhay={"cal":[420,380,320],"duration":[50,40,45]}
abhaynew=pd.DataFrame(abhay)
print(abhaynew)