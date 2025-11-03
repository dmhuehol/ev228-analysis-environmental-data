import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import fun_import as fi
import fun_plots as fp

file_path = '/Users/danielhueholt/Data/ev228_data/station/'
file_name = 'ROE00108901_temp_188001-202508.csv'
fig_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251103/'
fig_name = '1-roe.png'

var = 'metANN'
time_var = 'YEAR'

df, df_year = fi.import_ghcn(file_path=file_path + file_name, var=var)
filter_data = df[df != 999.9]
filter_year = df_year[df != 999.9]

print(filter_data)
print(df_year)

mean_var = np.mean(filter_data)
stdev_var = np.std(filter_data)
max_var = np.max(filter_data)
min_var = np.min(filter_data)
print(mean_var, stdev_var, max_var, min_var)

fp.timeseries(filter_data, in_x=filter_year, out_path=fig_path, out_name=fig_name)