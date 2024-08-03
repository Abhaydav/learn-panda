#Dataframe : it is a 2d datastructure like a 2D array with table incl. rows and columns

# import pandas as pd

# data={"cal":[400,500,600],"duration":[40,50,60]}
# datanew=pd.DataFrame(data)
# print(datanew)

#locate row: pandas use loc attribute to return one or more specific row.

# import pandas as pd
# data={"cal":[420,380,390],"dur":[50,40,45]}
# abhay=pd.DataFrame(data)
# print(abhay.loc[0])


#example of returning row 0 and 1

# import pandas as pd
# data={"cal":[420,380,390],"dur":[50,40,45]}
# abhay=pd.DataFrame(data)
# print(abhay.loc[[0,1]])

 #locate the named index

# import pandas as pd
# data={"cal":[420,380,390],"dur":[50,40,45]}
# abhay=pd.DataFrame(data,index=["day1","day2","day3"])
# print(abhay.loc["day1"])

#output in a dataframe
import pandas as pd
data={"cal":[420,380,390],"dur":[50,40,45]}
abhay=pd.DataFrame(data,index=["day1","day2","day3"])
print(abhay.loc[["day1","day2"]])

