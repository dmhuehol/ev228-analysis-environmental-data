'''fun_plots
Functions to make various plots relevant for EV228 course at Colorado College.
'''
import sys

import cartopy.crs as ccrs
from icecream import ic
import matplotlib.pyplot as plt

def timeseries(in_df, in_x=None, out_path='', out_name=''):
    ''' Plot timeseries from 1D dataframe '''
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(in_x, in_df, color='#dc6b2b', linewidth=2.5)
    plt.xlabel('years')
    plt.xlim(1948, 2025)
    plt.ylabel('annual temperature (deg C)')
    plt.title('ASM00094998 Macquarie Island 1948-2025')
    plt.savefig(out_path + out_name, dpi=400)

def map(in_da, out_path='', out_name=''):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(lons, lats, in_da, cmap='turbo')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('ERA5 10m wind 1980-1989 mean')
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('m/s')
    plt.savefig(out_path + out_name, dpi=400)

def map_cartopy(
        in_da, out_path='', out_name='', cmap='', in_title='', vmin=-1, 
        vmax=1):
    ''' Plot map from 2D DataArray with cartopy for grid '''
    fig = plt.figure()
    # ax = fig.add_subplot(111)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    # ax.stock_img()
    # gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
    #               linewidth=2, color='gray', alpha=0.5, linestyle='--')
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(
        lons, lats, in_da, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title(in_title)
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('standard deviation')
    plt.savefig(out_path + out_name, dpi=400)
