# Climate & Weather Analysis

## Goal
Create a Flask app to call weather data from a variety of micro weather stations throughout Hawaii to make it simple for the user to find historic weather data.

##Data Sources
Weather Data SQLite Database: https://github.com/clmonahan/Hawaii-Weather-Analysis/blob/master/climate_starter.ipynb

##Method
This project used Python, SQL, SQLite SQLAlchemy, Matplotlib, and the Pandas library.

## Procedures
1. Use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. Analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
2. Design a query to retrieve the last 12 months of precipitation data.
3. Design a query to calculate the total number of stations.
4. Design a query to find the most active stations.
5. Design a query to retrieve the last 12 months of temperature observation data.
6. Return the minimum, average, and maximum temperatures for desired dates and plot the data in a histogram.
7. Calculate the rainfall per weather station using the previous year's matching dates
8. Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.
9. Design a Flask API based on the queries that you have just developed.

## Challenges
The most difficult part of this project were making accurate calls to the SQLite file, and constructing the Flask app, which took a lot of patience and work to overcome.
