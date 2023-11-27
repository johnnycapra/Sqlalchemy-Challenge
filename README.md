# Sqlalchemy-Challenge

# Honolulu Holiday Climate Analysis

Congratulations on planning a long holiday vacation in Honolulu, Hawaii! To enhance your trip planning, conduct a climate analysis for the area. The following sections outline the steps to accomplish this task.

## Part 1: Analyze and Explore Climate Data

In this section, Python, SQLAlchemy, Pandas, and Matplotlib will be utilized for a basic climate analysis and data exploration of the climate database. Follow these steps:

1. Use the SQLAlchemy `create_engine()` function to connect to your SQLite database.
2. Use the SQLAlchemy `automap_base()` function to reflect tables into classes (e.g., `station` and `measurement`).
3. Save references to the classes created.
4. Link Python to the database by creating a SQLAlchemy session.

**Important:**
Remember to close your session at the end of your notebook.

Perform a precipitation analysis and a station analysis following the steps in the two subsections below.

### Precipitation Analysis

- Find the most recent date in the dataset.
- Query the previous 12 months of precipitation data using that date.
  - *Hint:* Select only the "date" and "prcp" values.
- Load the query results into a Pandas DataFrame and explicitly set the column names.
- Sort the DataFrame values by "date."
- Plot the results using the DataFrame plot method.
  - *See the attached screenshot for reference.*
- Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

- Design a query to calculate the total number of stations in the dataset.
- Design a query to find the most-active stations (those with the most rows).
  - List the stations and observation counts in descending order.
  - *Hint:* Utilize the `func.count` function in your query.
  - Answer the question: Which station ID has the greatest number of observations?
- Design a query that calculates the lowest, highest, and average temperatures filtering on the most-active station ID.
  - Design a query to get the previous 12 months of temperature observation (TOBS) data.
  - Filter by the station with the greatest number of observations.
  - Query the previous 12 months of TOBS data for that station.
  - Plot the results as a histogram with bins=12.
    - *See the attached histogram screenshot for reference.*
- Close your session.

## Part 2: Design Your Climate App

Now that the initial analysis is complete, design a Flask API based on the developed queries.

### Routes:

- `/`: Start at the homepage.
- List all available routes.
- `/api/v1.0/precipitation`: Convert the last 12 months of precipitation data to a dictionary and return the JSON representation.
- `/api/v1.0/stations`: Return a JSON list of stations from the dataset.
- `/api/v1.0/tobs`: Query the dates and temperature observations of the most-active station for the previous year of data. Return a JSON list of temperature observations for the previous year.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Return a JSON list of the minimum temperature, average temperature, and maximum temperature for a specified start or start-end range.
  - For a specified start, calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date.
  - For a specified start and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
