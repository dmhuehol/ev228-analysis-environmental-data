import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import fun_import as fi
import fun_plots as fp

file_path = '/Users/danielhueholt/Data/ev228_data/station/'
file_name = 'ASM00094998_temp_194804-202508.csv'
fig_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251109/'
fig_name = '1-asm.png'

var = 'metANN'
time_var = 'YEAR'

df, df_year = fi.import_csv_station(
    file_path=file_path + file_name, var=var, time_var=time_var)
filter_data = df[df != 999.9]
filter_year = df_year[df != 999.9]

# print(filter_data)
# print(df_year)

mean_var = np.mean(filter_data)
stdev_var = np.std(filter_data)
max_var = np.max(filter_data)
min_var = np.min(filter_data)
print(mean_var, stdev_var, max_var, min_var)
# print(filter_year[filter_data == max_var])
# print(filter_data[128])

fp.timeseries(filter_data, in_x=filter_year, out_path=fig_path, out_name=fig_name)