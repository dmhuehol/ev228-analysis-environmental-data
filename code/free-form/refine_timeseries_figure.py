'''refine_timeseries_figure
Make timeseries plot with Global Historical Climatology Network data. This file
is used for in-class demonstrations of various refinements and statistics 
(e.g., removing missing data, customizing plots, etc.)
'''
from icecream import ic
import numpy as np

import fun_import as fi
import fun_plots as fp

file_path = '/Users/danielhueholt/Data/ev228_data/station/'
file_name = 'ASM00094998_temp_194804-202508.csv'
fig_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251112/'
fig_name = '1-asm.png'
var = 'metANN'
time_var = 'YEAR'

#  Import and remove missing data
df, df_year = fi.import_csv_station(
    file_path=file_path + file_name, var=var, time_var=time_var)
filter_data = df[df != 999.9]
filter_year = df_year[df != 999.9]

#  Plot timeseries
fp.timeseries(
    filter_data, in_x=filter_year, out_path=fig_path, out_name=fig_name, 
    x_lim=[1948, 2025])

#  Statistics
mean_var = np.mean(filter_data)
stdev_var = np.std(filter_data)
max_var = np.max(filter_data)
min_var = np.min(filter_data)
ic(mean_var, stdev_var, max_var, min_var)
