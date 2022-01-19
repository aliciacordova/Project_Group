
from flask import Flask, render_template, jsonify, json, request, redirect, url_for
from config import user, password 
from flask_pymongo import PyMongo
import pymongo
from bson.json_util import dumps
import json

app = Flask(__name__)

@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"


#test to read a collection in the database and read a specific punkID


@app.route("/test")
def index():
    pagetitle = "HomePage"
    return render_template("index.html")


@app.route("/traders/")
def Traders():
    CONNECTION_STRING = "mongodb+srv://"+ user + ":" + password +"@cluster0.wddnt.mongodb.net/crypto_punks_mdb?retryWrites=true&w=majority"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = pymongo.database.Database(client,'crypto_punks_mdb')
    traders = pymongo.collection.Collection(db, 'traders_col')
    traders_col = json.loads(dumps(traders.find()))
    example = len(traders_col)
    return f'''
      <h1> example </h1>
    '''    


@app.route("/crypto_punks/")
def crypto_punks():
    CONNECTION_STRING = "mongodb+srv://"+ user + ":" + password +"@cluster0.wddnt.mongodb.net/crypto_punks_mdb?retryWrites=true&w=majority"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = pymongo.database.Database(client,'crypto_punks_mdb')
    crypto_punks = pymongo.collection.Collection(db, 'crypto_punks_col')
    crypto_punks_col = json.loads(dumps(crypto_punks.find()))
    example = len(crypto_punks_col)
    return f'''
      <h1>{example}</h1>
    '''    

@app.route("/txn_history/")
def txn_history():
    CONNECTION_STRING = "mongodb+srv://"+ user + ":" + password +"@cluster0.wddnt.mongodb.net/crypto_punks_mdb?retryWrites=true&w=majority"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = pymongo.database.Database(client,'crypto_punks_mdb')
    txn_history = pymongo.collection.Collection(db, 'txn_history_col')
    txn_history_col = json.loads(dumps(txn_history.find()))
    example = len(txn_history)
    return f'''
      <h1>{example}</h1>
    '''            


if __name__ == '__main__':
    app.run(port=8000)

