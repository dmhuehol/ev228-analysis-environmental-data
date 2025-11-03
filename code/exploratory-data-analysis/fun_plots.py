'''fun_plots
Functions to make various plots relevant for EV228 course at Colorado College.
'''
import sys

from icecream import ic
import matplotlib.pyplot as plt

def timeseries(in_df, in_x=None, out_path='', out_name=''):
    ''' Plot timeseries from 1D dataframe '''
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(in_x, in_df, color='#dc6b2b', linewidth=2.5)
    plt.xlabel('years')
    plt.xlim(1887, 2025)
    plt.ylabel('annual temperature (deg C)')
    plt.title('ROE00108901 Sibiu, Romania 1880-2025')
    plt.savefig(out_path + out_name, dpi=400)

def map(in_da, out_path='', out_name=''):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(lons, lats, in_da)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('ERA5 2m temperature 1997-2025 mean')
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('deg C')
    plt.savefig(out_path + out_name, dpi=400)
