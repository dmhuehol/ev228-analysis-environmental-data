import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path = '/Users/danielhueholt/Data/ev228_data/eds/Group3/'
fn = 'Selected_Station_Observations_Daily_Xtab_202510261705.csv'

df = pd.read_csv(file_path + fn)
dates = df['Date Time']
print(dates[0])
new_dates = list()
for d in dates:
    new_dates.append(d[2:-1])
print(pd.to_datetime(new_dates))