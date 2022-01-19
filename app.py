from flask import Flask, render_template, jsonify, json, request, redirect, url_for
from flask_pymongo import PyMongo
from joblib import dump, load
from pickle import dump as dump_p, load as load_p

import numpy as np
import pandas as pd

* import "FILENAME"

app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb+srv://cryptopunks:coding2021@cluster0.wddnt.mongodb.net/crypto_punks_mdb?retryWrites=true&w=majority
mongo = PyMongo(app)

#app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
#"mongodb://localhost:27017/DATABASE NAME" is the URI we'll be using to connect our app to Mongo. 
# This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "DATABASE NAME".


#SET UP FLASK APP ROUTE for the main HTML page the user will view when visiting the web app. 
# CryptoPunks(CollectionName) = mongo.db.mars.find_one() uses PyMongo to find the "CryptoPunks" collection in our database, 
# CryptoPunks=CryptoPunks tells Python to use the collection in MongoDB
#This function is what links our visual representation of our work, our web app, to the code that powers it.

@app.route("/test")
def index():
   CryptoPunks(crypto_punks_col) = mongo.db.CryptoPunks(crypto_punks_col).find_one()
   return render_template("index.html", CryptoPunks=CryptoPunks

@app.route("/cryptopunk/<punk_id>")
def cryptopunk(punk_id):
    example = mongo.db.crypto_punks_col.find_one_or_404({'punk_id':punk_id})
    return f'''
      <h1>{punk_id}</h1>
    '''

#MISSING: function to 

@app.route("/Select")
def Select():
   Collection_name = mongo.db.collection_name
   select_data = #code that uses the input from the drop down menu and search the data of an specific CryptoPunk
   Collection_name.update_one({}, {"$set":select_data}, upsert=True)
   return redirect('/', code=302)

#Last lines of code to run the app

if __name__ == "__main__":
   app.run()