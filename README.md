# CRYPTO PUNKS Machine Learning Project

## Presentation
*[Content
Team members have drafted their project, including the following:]*

### ✓ Selected topic: 
Explore the surging world of  NFT's, focused on a collection of 10,000 digital assets known as Crypto Punks, by analyzing the associated *PNG* images using Machine Learning, to establish which graphical features and attributes determine the type of Crypto Punk, such as *'Male'*, *'Female'*, and *'Other'* (*'Zombie'*, *'Ape'* or *'Alien'*) or if the Crypto Punk has a given accessory, in our case, glasses, which includes any of 9 different accessories (*'3D Glasses'*, *'Big Shades'*, *'Classic Shades'*, *'Horned Rim Glasses'*, *'Nerd Glasses'*, *'Regular Glasses'*, *'Small Shades'*,  *'VR'* and *'Welding Goggles'*). 

### ✓ Reason why they selected their topic: 
With this project we seek to apply our data analytics skills using Machine Learning while expanding our knowledge-base to include an image classification model, as this is an increasingly relevant field in the use of Machine Learning. We also wanted to further our skills in using *MongoDB*, a non-relational database.

### ✓ Description of their source of data: 
CryptoPunks were created by Larva Labs in 2017. They are the first NFT series to catch popular interest, and one of the most actively traded (https://www.larvalabs.com/cryptopunks). 

The dataset consists of a *JSON* file with all CryptoPunk transactions and the relevant attributes of the 10,000 CryptoPunks such as type (*'Male'*, *'Female'*, *'Zombie'*, *'Ape'* or *'Alien'*) and any of 87 different accessories (such as beards, glasses, hair, etc.). 

The dataset is available in Kaggle at:

https://www.kaggle.com/tunguz/cryptopunks?select=txn_history-2021-10-07.jsonl

A second dataset contains a folder with individual *.png* image files for each of the 10,000 Crypto Punks. The image files can be found at:

https://www.kaggle.com/tunguz/cryptopunks?select=imgs

### ✓ Questions they hope to answer with the data

Our project runs two models to predict, given an image file, the attributes of the image. The first model predicts which type of CryptoPunks the image represents, while the second model predicts if the image has glasses or not. 

## GitHub

## Main Branch 
### ✓ Includes a README.md

README.md README.md must include: 

### ✓ Description of the communication protocols

- The team has been in constant communication through a dedicated *Slack* channel and *Zoom* virtual calls.
- The team also shares a *Google Docs* folder for relevant documents, such as interesting articles on image processing techniques, presentation drafts and project rubrics. 
- Each member has been working in their own branch, uploading files. 
- Tasks are divided among the team members according to the different roles (triangle, circle, square), but also according to team member expertise.

## Machine Learning Model

*[Team members present a provisional machine learning model that stands in for the final machine learning model and accomplishes the following:

✓ Takes in data in from the provisional database 

✓ Outputs label(s) for input data]*

The project employs a Convolutional - Neural Network (CNN) model.

The model operates several layers as presented in the image below:

![Machine Learning CNN Model](filename.png)

The input data for the models is a list of numpy arrays of dimension 24 x 24 x 4. These arrays represent the digital information that conforms the image. The original images are 24 pixels by 24 pixels, and the arrays express the value of each pixel as a number between 0 and 255, representing the RGB color of the pixel. Before providing the input to the models, the arrays are normalized by dividing the values by 255, so that they fall in a range between 0 and 1.

For one of the models, the output label is 'type', represented as a one_hot_encoded field.

For the second model, the output label is 'glasses_ML'



## Database

*[Team members present a provisional database that stands in for the final database and accomplishes the following:

✓ Sample data that mimics the expected final database structure or schema 

✓ Draft machine learning module is connected to the provisional database]*

Our database consists of a *MongoDB* database, which has been loaded to the cloud using *MongoDB Atlas* cloud hosting service.

The database, *crypto_punks_mdb*, containes 3 collections:

- *crypto_punks_col* with 10,000 documents each containing 10 fields.
- *traders_col* with 132526 documents each containing 9 fields.
- *txn_history_col* with 167,492 documents each containing 12 fields.

The collections can be cross-referenced using the field *'punk_id'* as key.

The database and collections can be visualized using *MongoDB Compass* by establishing a connection with *MongoDB Atlas* through a secure URL.

## Description of the Data Exploration Phase

Two datasets where available for our analysis. One contains all blockchain transactions since the minting of the Crypto Punk NFT collection, and is available as a JSON file in Kaggle. The other associated data set is a collection of 10,000 *png* files also available in Kaggle, containing the individual images of each Crypo Punk.

Our ETL process entailed reading the JSON file and creating utilitary dataframes for the different elements of our analysis.

One dataframe extracts the unique Crypto Punk *'punk_id'*, their unique *'type'* and the *'accessories'* associated with each individual Crypto Punk. By analyzing this data, we determined that several *'types'* were underrepresented and would pose a challenge for the accuracy of our Machine Learning predictions. These *'types'*, which include *'Ape'*, *'Alien'* and *'Zombie'*, where grouped into a class *'Other'*.

Another dataframe decomposes all the unique *'accessories'* present in the collection, and establishes the count of Crypto Punks sharing this accessory. We also used this dataframe to group *'accessories'* into broad classes (for example, beards, headgear, glasses) in order to select a feature with variable visual representation that could lend itself for machine learning recognition.

Once we had analyzed the data and decided on our prediction target, we created additional dataframes containing columns with numerical representation of the features: *'type_ML'* with 0, 1 or 2 to represent if the type was *'Male'*, *'Female'* or *'Other'*, and *'glasses_ML'* with 0 or 1 to represent if the Crypto Punk did not have or did have glasses.

For each Crypto Punk *'punk_id'*, we looped through the ids to read each *png* image file, convert the image into a bitmap array, and store the associated *'punk_id'* and bitmap array in a list of dictionaries. With this list, we could then re-create any of the images using plotting functions without having to access the original *png* files.

A second list of dictionaries was also created for machine learning purposes, where the bitmap arrays were normalized. The original bitmap arrays were 24x24x4, with the numerical values in the arrays representing an RGB color between 0-255. By normalizing these numbers to conform to a range between 0 and 1 (achieved by dividing each one by 255), we improved the input data for the machine learning model.

Finally, we created additional dataframes for the transaction history of the whole collection by eliminating unnecesary columns, and an additional dataframe to identify each trader or collector of these NFTs and their own transaction history.

All of these dataframes where exported as *csv* files to our repository *Data* folder.

In addition to the ETL process notebook, another notebook converts each of the *csv* files to *json* format. These are stored in the *JSON_datafiles* subfolder of our *Data* repository folder. It also consolidates the *csv* files into 3 collections that are stored in our *MongoDB* local host.

A third ETL notebook reads the *csv* files, consolidates them into the three collections, 
but this time exports them to a *MongoDB Atlas* cluster in the cloud.

The database will be accessed by our visualization dashboard through a connection string pointing to the secure *MongoDB Atlas* url associated with our database.