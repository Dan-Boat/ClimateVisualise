# ClimateVisualize 
plot_options.py

This script contains all the required specifications required for visualizing 
global simulation output or reanalysis dataset.Please contact the author for more information if necessary
--------------------------------------------------------------
1. directories to input datasets and for output figure -(str)
2. setting projection, variable(eg. Temperature) and limit of dataset(must be the same for 
   positive and negative values) for the background plot: Projection must be 
   available from cartopy package (default is PlateCarre())
3. Defining title of plot, output file name and format (eg. pdf, svg)

plot_utils.py 

This script contains all the functions for computing the long-term annual means and monthly differences

1. loading data
2. extracting variables
3. converting units 
4. averaging for annual mean
5. annual and monthly difference
6. Function for generating the backgroud of plotting - projection, add boarderlines, coords formatter etc

plot_long_term_mean.py

Contains functions for generating annual and monthly long-term averages
