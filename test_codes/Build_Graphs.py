

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


##############################################
# BUILD THE CRYPTO PUNK GRAPHS
##############################################
def buildImagesGraphs (id_selection):
    # construct the connection string for Atlas
    CONNECTION_STRING = "mongodb+srv://"+ user + ":" + password +"@cluster0.wddnt.mongodb.net/crypto_punks_mdb?retryWrites=true&w=majority"

    # Create the connection client to Atlas
    client = pymongo.MongoClient(CONNECTION_STRING) 

    # indicate the database to access in Atlas
    db = pymongo.database.Database(client,'crypto_punks_mdb')
      
    # assign the connection to the database and collection to a variable (i.e. this still is not 'reading' 
    # the data from the database)
    deals = pymongo.collection.Collection(db, 'txn_history_col')
    punks = pymongo.collection.Collection(db, 'crypto_punks_col')
          
    # search the database for the unique punk_id value provided as input to 
    # the function and assign the output to a variable. The output will be an object.
    deals_data = json.loads(dumps(deals.find({"punk_id":id_selection})))
    punks_data = json.loads(dumps(punks.find({"punk_id":id_selection})))

    # Convert the json strings to dataframe
    deals_df = pd.DataFrame(deals_data)
    deals_df = deals_df.drop(columns=["_id"])

    # Convert date to datetime
    deals_df['date'] = pd.to_datetime(deals_df['date'])

    # Re-index the dataframe
    deals_df = deals_df.reset_index(drop=True)

    ########################################
    # BUILD PRICE HISTORY CHART
    ########################################

    # Display transaction and price history
    sold = deals_df[deals_df.txn_type == 'Sold'].groupby("date").agg({"eth": ["median"]}).reset_index("date")
    bid = deals_df[deals_df.txn_type == 'Bid'].groupby("date").agg({"eth": ["median"]}).reset_index("date")
    offered = deals_df[deals_df.txn_type == 'Offered'].groupby("date").agg({"eth": ["median"]}).reset_index("date")

    plt.figure(figsize=(10,5))
    plt.plot(sold['date'], sold['eth']['median'], label="Sold Median Eth")
    plt.plot(bid['date'], bid['eth']['median'], label="Bid Median Eth")
    plt.plot(offered['date'], offered['eth']['median'], label="Offered Median Eth")

    plt.legend()
    plt.xticks(rotation=60)
    plt.title("Median Eth Price Over Time for Punk ID")

    # Save the image locally
    image_name = "price_graph.png"
    plt.savefig("static/images/" + image_name)

    # Call the function to Export Chart to AWS
    exportAWS(image_name)
    

    ########################################
    # BUILD THE TRANSACTION HISTORY CHART
    ########################################

    # Transaction types to filter
    filter_types = ["Sold", "Bid", "Transfer", "Claimed"]

    # Filter the dataframe for relevant transaction types
    deals_df = deals_df.loc[deals_df["txn_type"].isin(filter_types)]

    # Sort by dates
    deals_df = deals_df.sort_values(["date"], ascending=True)

    # Re-index the dataframe
    deals_df = deals_df.reset_index(drop=True)

    # Correct dataframe for nan's
    for row in range(len(deals_df)):
        if (deals_df.at[row,"from"] == "nan") & (deals_df.at[row,"txn_type"] == "Claimed"):
            deals_df.at[row,"from"] = "larvalabs"
        if (deals_df.at[row,"to"] == "nan") & (deals_df.at[row,"txn_type"] == "Bid"):
            deals_df.at[row,"to"] = deals_df.at[row-1,"to"]

    # Build graph elements
    plt.figure(figsize=(8,8))

    G = nx.MultiDiGraph()

    # Create an empty dictionary for the edge labels
    mylabels={}

    for row in range(len(deals_df)):
        
        # Add to-from nodes
        G.add_node(deals_df.at[row,"from"])
        
        # Add edges to the nodes
        G.add_edge(deals_df.at[row,"from"],deals_df.at[row,"to"], color="red", weight=deals_df.at[row,"eth"], size=deals_df.at[row,"eth"])
        
        # Add the transaction type as edge label
        mylabels[deals_df.at[row,"from"],deals_df.at[row,"to"]]=deals_df.at[row,"txn_type"]

    pos=nx.circular_layout(G)

    d = dict(G.degree)

    nx.draw(G, pos, node_size = [v**2*200 for v in d.values()], node_color='turquoise', edge_color="cornflowerblue", arrowsize=20, width=3, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, mylabels, label_pos=.5)

    # Save the image locally
    image_name = "network_graph.png"
    plt.savefig("static/images/" + image_name)

    # Call the function to Export Chart to AWS
    exportAWS(image_name)


    ########################################
    # BUILD THE CRYPYO PUNK IMAGE
    ########################################

    # Obtain the image bitmap
    image_bitmap = punks_data[0]["image_bitmap"]

    plt.figure(figsize=(7,7))
    img = plt.imshow(image_bitmap)
    
    # Remove axes tick and tickmarks
    ax = plt.gca()
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])
    
    # Add a title
    plt.title("Crypto Punk "+str(id_selection), fontsize=40)
    
    # Add description of features
    punk_type = punks_data[0]["type"]
    punk_accessories = str(punks_data[0]["accessories"])
    wrapped_label = punk_type+"\n"+("\n".join(wrap(punk_accessories,30)))
    plt.xlabel(wrapped_label, fontsize=25)

    # Save the image locally
    image_name = "crypto_punk.png"
    plt.savefig("static/images/" + image_name)

    # Call the function to Export Chart to AWS
    exportAWS(image_name)

    return



def exportAWS (image_name):

    # Create AWS connection
    s3 = boto3.resource('s3', aws_access_key_id=key_id, aws_secret_access_key=secret_access_key)

    # Provide S3 bucket name
    bucket = "cryptopunksbucket"

    # upload image to aws s3
    # warning, the ACL here is set to public-read
    img_data = open("static/images/" + image_name, "rb")
    s3.Bucket(bucket).put_object(Key=image_name, Body=img_data, ContentType="image/png", ACL="public-read")

    return

