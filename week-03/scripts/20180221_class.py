import pandas as pd
import numpy as np
import os

df=pd.DataFrame()
print(df)

df['name']=['bilbo','frodo','samwise']

df.assign(hight=[0.5,0.4,0.6])

path1='C:/Users/Yael nidam/Dropbox (MIT)/00_2018_Spring/03_Big_Data/10_github/big-data-spring2018/week-03/data/'

df = pd.read_csv(path1 + 'skyhook_2017-07.csv', sep=',')

df.head()

df.dtypes

df.shape

df.shape[0]
df.shape[1]

df['count']

df.lat.unique()

df__multipleColumns = df[['hour', 'cat', 'count']]
df__multipleColumns.head()

df['hour']==158

time=df[df['hour']==158]
time.head
time.shape

df[(df['hour']==158) & (df['count']>50)]

bastille=df1[df['date']=='2017-07-14']
bastille.head()

bastille_enthusiasts=bastille[bastille['count']>bastille['count'].mean()]
bastille_enthusiasts.head(10)

df.groupby('date')['count'].describe()

df.groupby(['date', 'hour'])['count'].describe()

df['count'].max()
df['count'].min()
df['count'].mean()
df['count'].std()
df['count'].count()

# This line lets us plot in Atom
import matplotlib
# This line allows the results of plots to be displayed inline with our code.
%matplotlib inline

day_hours = df[df['date'] == '2017-07-02'].groupby('hour')['count'].sum()
day_hours
day_hours.plot()

df['date_new'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['date'].head

df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1)
df['weekday'].replace(7, 0, inplace = True)


for i in range(0.168.24):
    j=range(0,168,1)[i-5]

    if (J>i):
        df['hour'].replace(range(i,i_19,1), range(5,24,1), inplace=True)
        df['hour'].replace()
    else:
        df['hour'].replace(range(j,i+19,1), range(0,24,1), inplace=True)
