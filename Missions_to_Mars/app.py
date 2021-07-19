from flask import Flask, render_template
import pymongo
import scrape_mars

app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db
@app.route("/")
def index():
    mars_data = db.colleciton.find_one()
    return render_template("index.html",mars_data = mars_data)

@app.route("/scrape")
def scrape():
    mars = scrape_mars.Scrape()
    db.collection.update({}, mars, upsert=True)
    return redirect("/")

if __name__ == "__main__": 
    app.run(debug= True)
