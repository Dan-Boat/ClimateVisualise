# ClimateVisualize 
@daniel.boateng@uni-tuebingen.de (don't hesitate to contact me for more information)

This scripts contain functions required for visualizing global climate simulation dataset or reanalysis dataset using python.
To use this scripts, the following python packages must be installed on your python environment
-xarray, pandas, numpy, matplotlib, cartopy and their dependencies 


The module contains four different files (which might change for future development)

plot_long_term_difference.py - contain the function for plotting the long-term annual and monthly difference for specific variable

plot_long_term_mean.py - contain the functions for generating the plot for annual and monthly long-term means 

plot_utils.py - contains the funtions for displaying required domian (global, Africa, Europe etc) and also extracts the define variable like Temperature or Precipitation  and contains all the necessary computations needed

plot_options - contains the input variables that must be specified by the user (check the script for details)

Steps to use this module 
-------------------------
1. Edit the plot_option.py by defining the directory to the datasets for plotting (check the comments for every variable to advise yourself), variable to be plotted, domian name , plotting type (Average or Difference) and the projection if required. The plot title, colorbar label and format for saving the data must be defined if necessary
2. Run the plot_long_term_mean or plot_long_term_difference.py  depending on Average or Difference plotting type---this might change with argument parser when calling from a command line 
3. Check the defined plot_path for generated plots 


