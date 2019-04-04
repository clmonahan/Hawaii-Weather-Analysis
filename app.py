# %matplotlib inline
# from matplotlib import style
# import matplotlib.pyplot as plt
# import matplotlib.mlab as mlab
import numpy as np
# import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Stations = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Home page.
# List all routes that are available.

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:</br>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/START YYYY-MM-DD</br>"
        f"/api/v1.0/START YYYY-MM-DD/END YYYY-MM-DD"
    )

# /api/v1.0/precipitation
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precip():
    prcpQuery = session.query(Measurement.date, Measurement.prcp).all()
    prcpDate = [row[0] for row in prcpQuery]
    prcpPRCP = [row[1] for row in prcpQuery]
    prcpDict = dict(zip(prcpDate, prcpPRCP))
    return jsonify(prcpDict)

# /api/v1.0/stations
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of station data """
    # Query all stations
    stationQuery = session.query(Stations.station).order_by(Stations.station.asc()).all()
    return jsonify(stationQuery)

# /api/v1.0/tobs
# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.
@app.route("/api/v1.0/tobs/")
def temperature():
    """Return a list of temperatures from the last year"""
    tobsQuery = session.query(Measurement.tobs, Measurement.date)\
    .filter(Measurement.date.between('2016-08-23','2017-08-23')).order_by(Measurement.date.asc()).all()
    # Convert the query results to a Dictionary
    tobsDate = [row[0] for row in tobsQuery]
    tobsTobs = [row[1] for row in tobsQuery]
    tobsDict = dict(zip(tobsDate, tobsTobs))
    return jsonify(tobsDict)

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>")
def start(start):
    tempQuery = session.query(func.min(Measurement.tobs).label("min"),\
        func.avg(Measurement.tobs).label("avg"),\
        func.max(Measurement.tobs).label("max"))\
        .filter(Measurement.date >= start).all()
    tempStats = ('Min', 'Avg', 'Max')
    tempNums = (tempQuery[0][0], tempQuery[0][1], tempQuery[0][2])
    tempDict = dict(zip(tempStats, tempNums))
    return jsonify(tempDict)

@app.route("/api/v1.0/<start>/<end>")
def startEnd(start, end):
    tempQuery = session.query(func.min(Measurement.tobs).label("min"),\
        func.avg(Measurement.tobs).label("avg"),\
        func.max(Measurement.tobs).label("max"))\
        .filter(Measurement.date >= start)\
        .filter(Measurement.date <= end).all()
    tempStats = ('Min', 'Avg', 'Max')
    tempNums = (tempQuery[0][0], tempQuery[0][1], tempQuery[0][2])
    tempDict = dict(zip(tempStats, tempNums))
    return jsonify(tempDict)

if __name__ == '__main__':
    app.run(debug=True)