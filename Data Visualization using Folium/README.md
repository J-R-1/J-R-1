# Data Visualization and Geospatial Analysis using Folium

<img src="https://media2.giphy.com/media/3ov9k06VQ0SU6f15rW/giphy.gif?cid=790b76114e7ed87fe72e540b6641f7c468c4ecb1693f9d7a&rid=giphy.gif&ct=g" />


One of the most important tasks for someone working on datasets with countries, cities, etc. is to understand the relationships between their data’s physical location and their geographical context.  And one such way to visualize the data is using <b>Folium</b> since it was developed for the sole purpose of visualizing geospatial data. 

<b>Folium</b> builds on the data wrangling strengths of the <b>Python</b> ecosystem and the mapping strengths of the <b>Leaflet.js</b> library. Manipulate our data in Python, then visualize it in on a Leaflet map via Folium. It enables both the binding of data to a map for choropleth visualizations as well as passing Vincent/Vega visualizations as markers on the map.

<b>Folium</b> has a number of built-in tilesets from OpenStreetMap, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys. The library also supports both GeoJSON and TopoJSON overlays, as well as the binding of data to those overlays to create choropleth maps with color-brewer color schemes.

</hr>

## Data Source:

1. San Francisco Police Department Incidents for the year 2016 - Incidents derived from San Francisco Police Department (SFPD) Crime Incident Reporting system. Updated daily, showing data for the entire year of 2016. Address and location has been anonymized by moving to mid-block or to an intersection.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/PI_2016.png" />


2. The respondents' interest in the different data science topics surveyed . The csv file can be found 
<a href="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/Topic_Survey_Assignment%20(1).csv">here</a>.

</hr>

## Application Demo using Folium:

#### Creating a map of Mexico with a zoom level of 4.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/sc_mex.png" />

</hr>

#### Creating a Stamen Terrain map of Canada with zoom level 4.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/sc_canada.png" />

</hr>

#### Using San Francisco police department incidents from 2016 dataset, lets visualize where these crimes took place in the city of San Francisco. A pop-up text that would get displayed when we hover over a marker.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/sf_popup.png" />

</hr>

####  Adding the text to the circle markers for much cleaner display.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/sf_cm.png" />

</hr>

#### Grouping the markers into different clusters. Each cluster is then represented by the number of crimes in each neighborhood.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/sf_cluster.png" />

</hr>

#### Using the artist layer of Matplotlib, lets visualize the percentage of the respondents' interest in the different data science topics surveyed

<img src="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/sc_ds.png" />

</hr>

#### Using 'Choropleth' map, lets convert the San Francisco dataset to represent the total number of crimes in each neighborhood. A 'Choropleth map' is a thematic map in which areas are shaded or patterned in proportion to the measurement of the statistical variable being displayed on the map. The choropleth map provides an easy way to visualize how a measurement varies across a geographic area or it shows the level of variability within a region.

#### As per our Choropleth map legend, the darker the color and the closer the color to red, the higher the number of Crimes from that Neighbourhood.


<img src="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/sf_choro.png" />

</hr>

For a complete implementation of this project, Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Data%20Visualization%20using%20Folium/Data_Visualization.ipynb">notebook</a>.


