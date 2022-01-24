

##################################################################
# IMPORT DEPENDENCIES
##################################################################

# Import Dependencies
from flask import Flask, render_template, jsonify, json, request, redirect, url_for
from flask_pymongo import PyMongo
import pymongo

from bson.json_util import dumps
import json
import pandas as pd
import random

# Import MongoDB and AWS access paramaters
from config import user, password, key_id, secret_access_key

# Import plotting libraries
import matplotlib.pyplot as plt
import networkx as nx 
import plotly.graph_objects as go
from textwrap import wrap

# Import AWS SDK
import boto3

##################################################################



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
id_selection = "3600" #str(random.randrange(0,10000,1))


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

@app.route("/punk_facts/<id_selection>", methods=("POST", "GET"))
def punkFacts(id_selection):

    # construct the connection string for Atlas
    CONNECTION_STRING = "mongodb+srv://"+ user + ":" + password +"@cluster0.wddnt.mongodb.net/crypto_punks_mdb?retryWrites=true&w=majority"
    # Create the connection client to Atlas
    client = pymongo.MongoClient(CONNECTION_STRING) 
    # indicate the database to access in Atlas
    db = pymongo.database.Database(client,'crypto_punks_mdb')
    # assign the connection to the database and collection to variables (i.e. this still is not 'reading' 
    # the data from the database)
    attributes = pymongo.collection.Collection(db, 'attributes_col')
    crypto_punks = pymongo.collection.Collection(db, 'crypto_punks_col')

    # search the database for the unique punk_id value provided as input to 
    # the function and assign the output to a variable. The output will be an object.
    crypto_punks_data = json.loads(dumps(crypto_punks.find({"punk_id":id_selection}))) #[Replace "3600" for sample in the final code]
    
    # import the list of all crypto punk attributes
    attributes_data = json.loads(dumps(attributes.find()))
    
    # Convert the json lists to dataframes and drop un-needed columns
    punks_df = pd.DataFrame(crypto_punks_data)
    punks_df = punks_df.drop(columns=["_id"])
    attributes_df = pd.DataFrame(attributes_data)
    attributes_df = attributes_df.drop(columns=["_id"])

    # Create the summary punk_facts dataframe
    # 1. Create an empty list for all the attributes in the punk_id
    punk_attribute_list = []

    # 2. Populate the list
    punk_attribute_list.append(punks_df.at[0,"type"])
    punk_accessories = punks_df.at[0,"accessories"]
    for accessory in punk_accessories:
      punk_attribute_list.append(accessory)
    punk_attribute_list.append(str(len(punk_accessories))+" accessories")
    
    # Create the core dataframe of punk facts
    punk_facts_df = attributes_df[attributes_df['Attribute'].isin(punk_attribute_list)]
    # reset index
    punk_facts_df.reset_index(drop=True, inplace=True)
    # convert the "counts" column to numeric
    punk_facts_df["counts"] = pd.to_numeric(punk_facts_df["counts"])

    # Add rarity scores
    for row in range(len(punk_facts_df)):
      punk_facts_df.at[row,"Rarity %"] = punk_facts_df.at[row,"counts"]/10000 * 100
      punk_facts_df.at[row,"Rarity Score"] = 10000 / punk_facts_df.at[row,"counts"]
      
    # rename the "counts" column
    punk_facts_df.rename(columns = {"counts":"Punks that Share this Attribute"}, inplace = True)
    
    # remove the index
    punk_facts_df = punk_facts_df.set_index("Attribute")
    
    # test that the data is returned correctly [ELIMINATE THIS IN THE FINAL CODE]
    #return f'''
    #  <h1>{punk_facts_df.to_html}</h1>
    #'''    

    # 6. export the dataframe to html
    #return render_template("index.html")

    #return punk_facts_df.to_html()
    # Convert the dataframe to html and assign it to a variable
    punk_facts = punk_facts_df.to_html()

    # Return the dataframe object to a copy of the index html, and point
    # the variable to the html container name where it will be displayed
    return render_template('index.html', punk_facts=punk_facts)
  

##############################################
# BUILD THE CRYPTO PUNK GRAPHS
##############################################








if __name__ == '__main__':
    app.run(port=8000)

