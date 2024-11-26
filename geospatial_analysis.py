import geopandas as gpd
import matplotlib.pyplot as plt

# Load sample geospatial data (naturalearth_lowres for world data)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Example: Visualizing population density
world['pop_density'] = world['pop_est'] / world['area']

# Plotting
plt.figure(figsize=(12, 8))
world.plot(column='pop_density', cmap='coolwarm', legend=True, 
           legend_kwds={'label': "Population Density (people per unit area)"})
plt.title('World Population Density')
plt.show()
