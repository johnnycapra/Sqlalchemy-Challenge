# Import the dependencies.

from flask import Flask, jsonify
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import datetime as dt


#################################################

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
# reflect the tables

Base = automap_base()
Base.prepare(engine, reflect=True)



# Save references to each table

Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB

session = Session(engine)


#################################################

# Flask Setup

app = Flask(__name__)


#################################################

# Flask Routes

@app.route('/')
def home():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():

    # Use latest date from climate data and calculate a year from latest date

    date = dt.date(2017,8,23)
    year_ago = date - dt.timedelta(days=365)

    # Query data over last 12 months 

    prcp_scores = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_ago).\
        order_by(Measurement.date).all()
    
    # Convert data to dictionary 
    
    prcp_data = {date: prcp for date, prcp in prcp_scores}

    return jsonify(prcp_data)

@app.route('/api/v1.0/stations')
def stations():

    # Query for all stations ans list them 

    stations_query = session.query(Station.station).all()
    stations_list = [station for station, in stations_query]

    return jsonify(stations_list)


@app.route('/api/v1.0/tobs')
def tobs():
    # Use latest date from climate data and calculate a year from latest date

    date = dt.date(2017,8,23)
    year_ago = date - dt.timedelta(days=365)

    # Get most active station 

    most_active = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()
    
    # Most active ID 

    most_active_id = most_active[0]

    # Query for last 12 months of data at most active station

    temp_data = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == most_active_id).\
    filter(Measurement.date >= year_ago).all()

    # Convert to dictionary 

    temp_dict = [{"date": date, "temperature": tobs} for date, tobs in temp_data]

    return jsonify(temp_dict)

@app.route('/api/v1.0/<start>')
def temp_start(start):

    # Query for min, avg, and max by specific start date 

    tobs_query = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    # Convert to dictionary 

    temp_dict = {
        "Min Temperature": tobs_query[0][0],
        "Average Temperature": tobs_query[0][1],
        "Max Temperature": tobs_query[0][2]
    }

    return jsonify(temp_dict)

@app.route('/api/v1.0/<start>/<end>')
def temp_start_end(start, end):

    # Query for min, avg, max from specific start and end date

    tobs_query = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()    
    
    # Convert to dictionary
    
    temp_data = {
        "Min Temperature": tobs_query[0][0],
        "Average Temperature": tobs_query[0][1],
        "Max Temperature": tobs_query[0][2]
    }

    return jsonify(temp_data)

    #################################################

if __name__ == '__main__':
    app.run(debug=True)