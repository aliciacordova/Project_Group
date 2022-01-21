
# Import Dependencies
from flask import Flask, render_template, jsonify, json, request, redirect, url_for
from flask_pymongo import PyMongo
import pymongo
from bson.json_util import dumps
import json
import plotly.express as px

# Import user and password
from config import user, password 

# Create the Flask instance
app = Flask(__name__)

# Create the visualization homepage
@app.route("/")
def index():
    pagetitle = "HomePage"
    return render_template("index.html")

@app.route("/Chart")
# Build a test chart using plotly
def Chart():
  fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
  return fig.write_html('first_figure.html', auto_open=True)



# [FOR THE TIME BEING, PASS THE ID AS A FIXED VARIABLE. THIS VARIABLE SHOULD COME 
# FROM THE INPUT FIELD IN THE HTML]
id_selection = "3600"


@app.route("/traders/<id_selection>")
# Define a function to return an object with the Crypto Punk data from the traders_col. 
# The input variable, "id_selection" is the value generated from our input fiels (i.e. punk_id).
def Traders(id_selection):
     # construct the connection string for Atlas
    CONNECTION_STRING = "mongodb+srv://"+ user + ":" + password +"@cluster0.wddnt.mongodb.net/crypto_punks_mdb?retryWrites=true&w=majority"
    # Create the connection client to Atlas
    client = pymongo.MongoClient(CONNECTION_STRING)
    # indicate the database to access in Atlas
    db = pymongo.database.Database(client,'crypto_punks_mdb')
    # assign the connection to the database and collection to a variable (i.e. this still is not 'reading' 
    # the data from the database)
    traders = pymongo.collection.Collection(db, 'traders_col')
    # search the database for the unique punk_id value provided as input to 
    # the function and assign the output to a variable. The output will be an object.
    traders_data = json.loads(dumps(traders.find({"punk_id":id_selection})))
    
    # return the data [ACTIVATE THIS IN THE FINAL VERSION]
    #return crypto_punks_data

    # Test that the data is being read [ELIMINATE IN FINAL CODE]
    return f'''
      <h1> {traders_data} </h1>
    '''    




@app.route("/crypto_punks/<id_selection>")
# Define a function to return an object with the Crypto Punk data from the crypto_punks_col. 
# The input variable, "id_selection" is the value generated from our input fiels (i.e. punk_id). 
def crypto_punks(id_selection):
    # construct the connection string for Atlas
    CONNECTION_STRING = "mongodb+srv://"+ user + ":" + password +"@cluster0.wddnt.mongodb.net/crypto_punks_mdb?retryWrites=true&w=majority"
    # Create the connection client to Atlas
    client = pymongo.MongoClient(CONNECTION_STRING)
    # indicate the database to access in Atlas
    db = pymongo.database.Database(client,'crypto_punks_mdb')
    # assign the connection to the database and collection to a variable (i.e. this still is not 'reading' 
    # the data from the database)
    crypto_punks = pymongo.collection.Collection(db, 'crypto_punks_col')
    # search the database for the unique punk_id value provided as input to 
    # the function and assign the output to a variable. The output will be an object.
    crypto_punks_data = json.loads(dumps(crypto_punks.find_one({"punk_id":id_selection}))) #[Replace "3600" for sample in the final code]
    
    # return the data [ACTIVATE THIS IN THE FINAL VERSION]
    #return crypto_punks_data

    # test that the data is returned correctly [ELIMINATE THIS IN THE FINAL CODE]
    return f'''
      <h1>{crypto_punks_data}</h1>
    '''
    

   

@app.route("/txn_history/<id_selection>")
# Define a function to return an object with the Crypto Punk data from the txn_history_col. 
# The input variable, "id_selection" is the value generated from our input fiels (i.e. punk_id).
def txn_history(id_selection):
    # construct the connection string for Atlas
    CONNECTION_STRING = "mongodb+srv://"+ user + ":" + password +"@cluster0.wddnt.mongodb.net/crypto_punks_mdb?retryWrites=true&w=majority"
    # Create the connection client to Atlas
    client = pymongo.MongoClient(CONNECTION_STRING) 
    # indicate the database to access in Atlas
    db = pymongo.database.Database(client,'crypto_punks_mdb')
    # assign the connection to the database and collection to a variable (i.e. this still is not 'reading' 
    # the data from the database)
    txn_history = pymongo.collection.Collection(db, 'txn_history_col')
    # search the database for the unique punk_id value provided as input to 
    # the function and assign the output to a variable. The output will be an object.
    txn_history_data = json.loads(dumps(txn_history.find({"punk_id":id_selection})))
    
    # return the data [ACTIVATE THIS IN THE FINAL VERSION]
    # return txn_history_data

    # test that the data is returned correctly [ELIMINATE THIS IN THE FINAL CODE]
    return f'''
      <h1>{txn_history_data}</h1>
    '''            


##############################################
# BUILD THE CRYPTO PUNKS FACTS
##############################################

@app.route("/punk_facts/<id_selection>")
def punkFacts(id_selection):

  # 1. read the punk data from the crypto_punk_col
  #crypto_punks_data = crypto_punks(id_selection)
  # 2. select from this data the type and accessories

  # 3. read a new collection (to be exported to MongoDB) called accessories_col

  # 4. search the accessories_col for the accessories shared with the crypto_punk to get the counts
  #for items in punk_accessories


  # 5. build a dataframe (df) with the rarity values


  # 6. export the dataframe to html
  return df.to_html()



if __name__ == '__main__':
    app.run(port=8000)

