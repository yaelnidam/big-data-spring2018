import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from itertools import cycle, islice
import os

%matplotlib inline

import datetime

path1='C:/Users/Yael nidam/Dropbox (MIT)/00_2018_Spring/03_Big_Data/10_github/big-data-spring2018/week-03/data/'

os.chdir('../data/')
df = pd.read_csv(path1 + 'skyhook_2017-07.csv', sep=',')
