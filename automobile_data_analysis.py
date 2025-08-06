import pandas as pd 
url='https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
data=pd.read_csv(url,header=None)
#print(data.head(5))
#print(data.dtypes)
#print(data.describe(include= 'all'))
print(data.info())