from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
@app.route("/")
def index():
    mars_data = mongo.db.colleciton.find_one()
    return render_template("index.html",mars_data = mars_data)

@app.route("/scrape")
def scrape():
    mars = scrape_mars.Scrape()
    mongo.db.collection.update({}, mars, upsert=True)
    return redirect("/")

if __name__ == "__main__": 
    app.run(debug= True)
