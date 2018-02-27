import pandas as pd
import numpy as np
import os

df=pd.DataFrame()
print(df)

df['name']=['bilbo','frodo','samwise']

df.assign(hight=[0.5,0.4,0.6])

path1='C:/Users/Yael nidam/Dropbox (MIT)/00_2018_Spring/03_Big_Data/10_github/big-data-spring2018/week-03/data/'

os.chdir('../data/')
df = pd.read_csv('skyhook_2017-07.csv', sep=',')

df1 = pd.read_csv(path1 + 'skyhook_2017-07.csv', sep=',')

df1
