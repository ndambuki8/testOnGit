#Pandas - fast and powerful package for data analysis and manipulation
#A pandas DataFrame is a sturcture that contains 2D data stored as rows and columns.
#A pandas series is a structure that contains Oe-D data
import pandas as pd
import numpy as np

#Data frame from a dictionary
df =pd.DataFrame({
    'a':np.array([1,2,3]),
    'b':np.array([1,2,3]),
    'c':['x','x','y']
})

# Create a dataframe from a list of dictionaries
# print(pd.DataFrame([
#     {'a':1, 'b':4, 'c':'X'},
#     {'a':1, 'b':4, 'c':'X'},
#     {'a':3, 'b':6, 'c':'y'}
# ]))

print(df.nlargest(1,'a'))

print(df.iloc[2,1])