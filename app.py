from flask import Flask, jsonify
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from matplotlib import pyplot
import matplotlib
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt


app = Flask(__name__)

hello_dict = {"Hello": "World!"}

@app.route("/")
def home():#display routes
    return ("Routes: precipitation, stations, tobs, start, end")
#display route discription

@app.route("/api/v1.0/precipitation")
def prcp():
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")
    conn=engine.connect()
    base=automap_base()
    base.prepare(engine, reflect=True)
    station_count = pd.read_sql("SELECT station, count(station) FROM measurement WHERE station NOT NULL GROUP BY station ORDER BY count(station) DESC", conn)
    measurement = base.classes.measurement
    station=base.classes.station
    session=Session(engine)
    station_data = pd.read_sql("SELECT * FROM station", conn)
    measurement_data = pd.read_sql("SELECT * FROM measurement", conn)
    
#select the most active station
    max_count=station_count['count(station)'].max()
    max_row=station_count.loc[station_count["count(station)"]==max_count]
#extract the string of the most active station name
    rawname=str(max_row["station"])
    string_it=str(rawname)
    split_it=string_it.split(" ")[4]
    split_again=split_it.split("\n")
    station_name=split_again[0]

     #get only the data from the relevant station from the dataset
    maxstation_df=measurement_data.loc[measurement_data["station"]==station_name]

    # dropping null value columns to avoid errors 
    maxstation_df.dropna(inplace = True) 
    

    # converting to dict 
    dict_df=maxstation_df[['date', 'tobs']].set_index(["date"])
    data_dict = dict_df.to_dict() 

    json=jsonify(data_dict)

    return(json)
    print(json)   

@app.route("/api/v1.0/stations")
def stations():

    #Every dependency in the universe I could possibly need
    from matplotlib import style
    style.use('fivethirtyeight')
    import matplotlib.pyplot as plt
    from datetime import datetime
    from datetime import timedelta
    from matplotlib import pyplot
    import matplotlib
    from flask import Flask, jsonify
    import numpy as np
    import pandas as pd
    import datetime as dt
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")
    conn=engine.connect()
    base=automap_base()
    base.prepare(engine, reflect=True)
    measurement = base.classes.measurement
    station=base.classes.station
    session=Session(engine)
    station_data = pd.read_sql("SELECT * FROM station", conn)
    measurement_data = pd.read_sql("SELECT * FROM measurement", conn)

    dict_df=station_data['station']
    data_dict = dict_df.to_dict() 

    json=jsonify(data_dict)

    return(json)


@app.route("/api/v1.0/<start>")
def start(start):
#Every dependency in the universe I could possibly need
    from matplotlib import style
    style.use('fivethirtyeight')
    import matplotlib.pyplot as plt
    from datetime import datetime
    from datetime import timedelta
    from matplotlib import pyplot
    import matplotlib
    from flask import Flask, jsonify
    import numpy as np
    import pandas as pd
    import datetime as dt
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")
    conn=engine.connect()
    base=automap_base()
    base.prepare(engine, reflect=True)
    measurement = base.classes.measurement
    station=base.classes.station
    session=Session(engine)
    station_data = pd.read_sql("SELECT * FROM station", conn)
    measurement_data = pd.read_sql("SELECT * FROM measurement", conn)

    temps=session.query(measurement.date, measurement.tobs).\
    filter(func.strftime("%Y-%m-%d", measurement.date) > start, func.strftime("%Y-%m-%d", measurement.date) < '2017-08-23').all()
    
    temp_df = pd.DataFrame(temps).set_index("date")
            
    dict_df=temp_df['tobs']
    data_dict = dict_df.to_dict() 

    json=jsonify(data_dict)

    return(json)




@app.route("/api/v1.0/tobs")
def tobs():
    from matplotlib import style
    style.use('fivethirtyeight')
    import matplotlib.pyplot as plt
    from datetime import datetime
    from datetime import timedelta
    from matplotlib import pyplot
    import matplotlib
    from flask import Flask, jsonify
    import numpy as np
    import pandas as pd
    import datetime as dt
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")
    conn=engine.connect()
    base=automap_base()
    base.prepare(engine, reflect=True)
    measurement = base.classes.measurement
    station=base.classes.station
    session=Session(engine)


    calc_temps=session.query(measurement.date, measurement.tobs).\
    filter(func.strftime("%Y-%m-%d", measurement.date) > '2017-08-08',func.strftime("%Y-%m-%d", measurement.date) < '2017-08-23').all()
    calc_df = pd.DataFrame(calc_temps).set_index("date")

    #make dictionary and JSON
    dict_df=calc_df['tobs']
    data_dict = dict_df.to_dict() 

    json=jsonify(data_dict)

    return(json)


@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
#Every dependency in the universe I could possibly need
    from matplotlib import style
    style.use('fivethirtyeight')
    import matplotlib.pyplot as plt
    from datetime import datetime
    from datetime import timedelta
    from matplotlib import pyplot
    import matplotlib
    from flask import Flask, jsonify
    import numpy as np
    import pandas as pd
    import datetime as dt
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")
    conn=engine.connect()
    base=automap_base()
    base.prepare(engine, reflect=True)
    measurement = base.classes.measurement
    station=base.classes.station
    session=Session(engine)
    station_data = pd.read_sql("SELECT * FROM station", conn)
    measurement_data = pd.read_sql("SELECT * FROM measurement", conn)

    temps=session.query(measurement.date, measurement.tobs).\
    filter(func.strftime("%Y-%m-%d", measurement.date) > start, func.strftime("%Y-%m-%d", measurement.date) < end).all()
    
    temp_df = pd.DataFrame(temps).set_index("date")
            
    dict_df=temp_df['tobs']
    data_dict = dict_df.to_dict() 

    json=jsonify(data_dict)

    return(json)


if __name__ == "__main__":
    app.run(debug=True)
