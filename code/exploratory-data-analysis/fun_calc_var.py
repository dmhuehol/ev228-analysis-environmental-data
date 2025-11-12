import numpy as np
import xarray as xr

def calc_lin_reg_vec(np_x, da_y):
    ''' Calculate linear regression and retrieve coefficients in a
    vectorized way. This saves massive amounts of time for
    multidimensional data, such as large ensembles.
    Derived from implementation at:
    hrishichandanpurkar.blogspot.com/2017/09/vectorized-functions-for-correlation.html
    
    Arguments:
    np_x -- 1-D numpy array of independent variable
    da_y -- DataArray of dependent variable with 'time' or 'year' dimension
    
    Returns:
    temporal_grad -- dict containing grad and intercept for each rlz
    '''
    time_entries = len(np_x)
    x_time_mn = np_x.mean()
    x_time_stdev = np_x.std()
    try:
        y_time_mn = da_y.mean(dim='year')
        y_time_stdev = da_y.std(dim='year')
    except ValueError:
        y_time_mn = da_y.mean(dim='valid_time')
        y_time_stdev = da_y.std(dim='valid_time')       
    cov = np.sum(
        (np_x - x_time_mn) * (da_y - y_time_mn), axis=0) / (time_entries)
    reg_slp = cov / (x_time_stdev ** 2)
    reg_int = y_time_mn - x_time_mn * reg_slp
    temporal_grad = {
        "grad": reg_slp,
        "intcpt": reg_int
    }

    return temporal_grad