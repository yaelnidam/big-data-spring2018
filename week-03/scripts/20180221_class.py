import pandas as pd
import numpy as np
import os

df=pd.DataFrame()
print(df)

df['name']=['bilbo','frodo','samwise']

df.assign(hight=[0.5,0.4,0.6])

path1='C:/Users/Yael nidam/Dropbox (MIT)/00_2018_Spring/03_Big_Data/10_github/big-data-spring2018/week-03/data/'

os.chdir('../data/')
df2 = pd.read_csv('skyhook_2017-07.csv', sep=',')

df1 = pd.read_csv(path1 + 'skyhook_2017-07.csv', sep=',')

df1.head()

df1.dtypes

df1.shape

df1.shape[0]
df1.shape[1]

df1['count']

df1.lat.unique()

df1__multipleColumns = df1[['hour', 'cat', 'count']]
df1__multipleColumns.head()

df1['hour']==158

time=df1[df1['hour']==158]
time.head
time.shape

df1[(df1['hour']==158) & (df1['count']>50)]

bastille=df1[df1['date']=='2017-07-14']
bastille.head()

bastille_enthusiasts=bastille[bastille['count']>bastille['count'].mean()]
bastille_enthusiasts.head(10)

df1.groupby('date')['count'].describe()

df1.groupby(['date', 'hour'])['count'].describe()

df1['count'].max()
df1['count'].min()
df1['count'].mean()
df1['count'].std()
df1['count'].count()
