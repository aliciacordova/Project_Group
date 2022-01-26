# CRYPTO_PUNKS_Project

### ✓ Selected topic: 
Explore the surging world of  NFT's, focused on a collection of 10.000 Crypto Punks as PNG images, to establish which features and attributes using Machine Learning determine the type of Crypto Punk such as [“Male', 'Female', 'Zombie'. 'Ape' or 'Alien'] or or if it has accessories in the image  [Glasses]. 

### ✓ Reason for selecting topic: 
With this project we seek to apply our data analytics skills using Machine Learning while expanding our knowledge base by implementing an image classification model, as this is an increasingly relevant field in the use of Machine Learning.

### ✓ Description of the source data: 
CryptoPunks were created by Larva Labs in 2017. They are the first NFT series to catch popular interest, and one of the most actively traded. The dataset consists of json file with all CryptoPunk transactions and the relevant attributes of the 10,000 CryptoPunks such as type [“Male', 'Female', 'Zombie'. 'Ape' or 'Alien'] and any of the 87 differets accessories [such as beard, glasses, hair, etc].   

https://www.kaggle.com/tunguz/cryptopunks?select=txn_history-2021-10-07.jsonl

A second dataset cotains png image file for each of the 10,000 CryptoPunks NFT's.

https://www.kaggle.com/tunguz/cryptopunks?select=imgs

### ✓ Questions we hope to answer with the data

Our model should predict, given an image file, which type of CryptoPunks the image represents. [“Male', 'Female', 'Zombie'. 'Ape' or 'Alien']. or if it has accessories in the image  [Glasses].


### ✓ Description of the communication protocols

- The team has been in continue communication through slack. 
- Each member has been working in their own branch. 
- We divide task according to the different roles (triangle, circle, square).
- In order to keep updated on the status of each of our parts of the project, we organized regular zoom meetings.

### ✓ Machine Learning Model

The preliminary data includes columns that describe the information refer to 10.000 Crypto Punks

After connecting to the database, we printed out the header for each column to see all of the features available. From that list, we chose the features we need to create the Machine Learning Model. 

We decide to create 2 models. One classification model to determines which type if Crypto Punks the image is. And one binary model to determine is the Crypto Punk image has glasses or not. For both models we did the same process: 

1- The data was split into training and test data using the train_test_split function. We used the default 75% to 25% split.

2- In this project we choose to use a Convolutional and Neural Network model.

3- After careful analyzing, we used the sequential models and Neural network model to make predictions. After adding some layers using Relu, Sofmax (for Classification model) and Sigmoid (for Binary Model), the accuracy rate for both model was 100%. This means our models accurately predict the outcome of all the Crypto Punk images .


### ✓ Database

Our database consists of a MongoDB database, which has been loaded to the cloud using MongoDB Atlas cloud hosting service.

The database, crypto_punks_mdb, containes 3 collections:
   - crypto_punks_col with 10,000 documents each containing 10 fields.
   - traders_col with 132526 documents each containing 9 fields.
   - txn_history_col with 167,492 documents each containing 12 fields.

The collections can be cross-referenced using the field 'punk_id' as key.

The database and collections can be visualized using MongoDB Compass by establishing a connection with MongoDB Atlas through a secure URL.


### ✓ Presentation

Our presentation can be found here Google Slide Presentation https://docs.google.com/presentation/d/17QrwkucoQluYAyOd0sKMI5KkpIkx8blE9acwNgYu1Bc/edit#slide=id.p

### ✓ Dashboard

Thus far, we have obtained the information we need to present in a dashboard. We built a successful machine learning model that can predict the type of CryptoPunks, as well as predict whether it has glasses or not. Now we need to visualize the prediction data for each CryptoPunk.

Specifically, the user should be able to select a CryptoPunk and identify what type it is and whether has glasses or not. This way, the user will be able to interact with the data and have a better understanding of it. 

