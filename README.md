# ev228-analysis-environmental-data
Code for EV228: Analysis of Environmental Data at Colorado College

# Code Index
Code is kept inside the `code` folder, which contains further subfolders relevant for different parts of the course.

## colab
Colab notebooks used to introduce fundamental statistical, data science, and coding concepts for the earliest part of the course.
* `fizzbuzz`: Fizzbuzz exercise to demonstrate loops and conditional statements
* `import-data`: Importing timeseries data and fundamentals of exploratory data analysis
* `probability`: Fundamentals of probability and coding using a virtual dice roller
* `statistical_moments`: Visualizing moments of a distribution with probability distribution functions
* `what_is_pdf`: Create and visualize a probability distribution function

## free-form
Free-form Python code used for data analysis and software development during most of the course.
### Explanation of prefixes
* `fun_`: Modules that contain functions to be imported and called elsewhere
* `refine_`: Scripts used in class to demonstrate refining specific figures and processes
* `test_`: Scripts for testing code to address specific problems in class or troubleshooting sessions
* `wrap_`: Scripts for general use that call functions from the custom `fun_` modules
* Code without these prefixes serve other specific purposes and don't call any functions in a `fun_` module (i.e., they don't "wrap" anything!)
### Individual files
Some of these files overlap conceptually: for example, `wrap_map_cartopy` could be easily used to do the same thing as `wrap_plot_anom`. For class purposes, however, it is often easier to have separate files to work with on different days.
* `fun_calc_var`: Calculate variables for derived datasets
* `fun_import`: Import various datasets
* `fun_plots`: Make plots for station and gridded datasets
* `refine_map_figure`: Use to make map plot for in-class demonstration of iteration on visuals and statistics
* `refine_timeseries_figure`: Use to make timeseries plot for in-class demonstration of iteration on visuals and statistics
* `test_eds_troubleshooting`: Troubleshooting for Environmental Data Story assignment
* `test_listedcolormap`: Testing custom discrete colormap
* `utensils_demo`: Plots bar graph with utensils data from opening class
* `vectorized_example`: Contrast efficiency of loop-based and vectorized array addition
* `wrap_calc_anom`: Calculate z-score anomalies
* `wrap_eda_bishoprock`: Exploratory data analysis on the Bishop Rock weather station from the [Everest](https://doi.org/10.1175/BAMS-D-22-0120.1) dataset (from Retrieval 3)
* `wrap_lr_gridded`: Loop-based versus vectorized linear regression on a gridded dataset
* `wrap_lr_station`: Linear regression on a station dataset
* `wrap_map_cartopy`: Plot a gridded dataset on a map with Cartopy
* `wrap_plot_anom`: Plot anomalies calculated through `wrap_calc_anom` for in-class demonstration

# Testing
Code has been tested on Apple M4 Max. The YML environment file assumes this platform and may not build successfully on others, particularly Windows or Intel OS X. Critical packages include `cartopy`, `icecream`, `matplotlib`, `numpy`, `pandas`, `scipy`, `xarray`, and their dependencies.

# Credit
Unless otherwise specified, code was written by [Daniel Hueholt](https://www.hueholt.earth). Code in this repository is available under an MIT License, included as the LICENSE file.
