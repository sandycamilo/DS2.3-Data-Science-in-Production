"""
    Visualizing avocado sales from 2015 - 2018
"""
from functools import reduce
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Attach our dataframe to our app
app.df = pd.read_csv("avocado.csv", skiprows=1)
app.df.columns = ["i", "Date", "AveragePrice", "Total Volume", 
                    "4046", "4225", "4770", "Total Bags", "Small Bags", 
                    "Large Bags", "XLarge Bags", "type", "year", "region"]


@app.route("/", methods=["GET"])
def get_root():
    """
        Root route that returns the index page
    """
    return render_template("index.html"), 200


@app.route("/time_series", methods=["GET"])
def get_time_series_data():
    """
        Return the necessary data to create a time series
    """
    # Grab the requested prices and columns from the query arguments
    ls_sales = [int(sale) for sale in request.args.getlist("n")]

    # Generate a list of all the prices we need to get
    all_sales = [str(sale) for sale in range(min(ls_sales), max(ls_sales) + 1)]

    # Grab all of the wanted prices by filtering for the ones we want
    wanted_sales = reduce(
        lambda a, b: a | b, (app.df["Total Volume"].str.contains(sale) for sale in all_sales)
    )

    print(wanted_sales)

    # Create a new dataframe from the one that
    # total volume is number of sales 
    # type is conventional or organic 
    df_new = app.df[wanted_sales][["Total Volume"] + ["region", "type"]]

    # Return the dataframe as json
    return df_new.to_json(), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)
