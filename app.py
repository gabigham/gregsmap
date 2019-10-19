
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_cl

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mission = mongo.db.missions.find_one()

    # Return template and data
    return render_template("index.html", mission=mission)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mission = scrape_cl.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.missions.update({}, mission, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
