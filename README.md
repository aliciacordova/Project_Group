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

### Machine Learning Model

The preliminary data includes columns that describe the information refer to 10.000 Crypto Punks

After connecting to the database, we printed out the header for each column to see all of the features available. From that list, we chose the features we need to create the Machine Learning Model. 

We decide to create 2 models. One classification model to determines which type if Crypto Punks the image is. And one binary model to determine is the Crypto Punk image has glasses or not. For both models we did the same process: 

1- The data was split into training and test data using the train_test_split function. We used the default 75% to 25% split.

2- In this project we choose to use a Convolutional and Neural Network model.

3- After careful analyzing, we used the sequential models and Neural network model to make predictions. After adding some layers using Relu, Sofmax (for Classification model) and Sigmoid (for Binary Model), the accuracy rate for both model was 100%. This means our models accurately predict the outcome of all the Crypto Punk images .


### Database

Team members present a provisional database that stands in for the final database and accomplishes the following:

✓ Sample data that mimics the expected final database structure or schema 

✓ Draft machine learning module is connected to the provisional database

### Presentation

Our presentation can be found here Google Slide Presentation

### Dashboard

## The link to the dashboard repository is Link Dashboard Repo.

DASHBOARD CONCEPT

Thus far, we have obtained the information we need to present in a dashboard. We built a successful machine learning model that can predict the type of CryptoPunks, as well as predict whether it has glasses or not. Now we need to visualize the prediction data for each CryptoPunk.
 Specifically, the user should be able to select a CryptoPunk and identify what type it is and whether has glasses or not. This way, the user will be able to interact with the data and have a better understanding of it. 

What we need to create:

This dashboard consists of the following materials:
Design

![htlm1](https://user-images.githubusercontent.com/87447639/149423340-df51b870-6a79-4d77-9c39-3494b36233f9.PNG)

![htlm2](https://user-images.githubusercontent.com/87447639/149423342-8f0f8623-d892-4776-bdba-f910aab5b6eb.PNG)

Drop Down Menu
-	Create a drop down menu so the user can select a CryptoPunk.
-	Create an interactive button option to obtain more info about that Crypto Punk. When the user click that button a second page will be display with a menu to show “Graph Price”, “Accessories attributes” and “History Transaction”.  
Crypto Punk Image
-	Display the image of the selected cryptopunk
o	Visual
 
Crypto Punk Table Information
-	Create a table containing basic information about the selected cryptopunk

Glasses Prediction
-	Option A: Create a Red and Green button group that changes the intensity of the color depending whether the CryptoPunk has glasses or not.  Using the opacity property, reduce the opacity of red when the option is YES or reduce the opacity of green when the option is NO. 
Resource: https://www.w3schools.com/css/css3_buttons.asp 


Type Prediction
-	Option A: Create an image box that changes the icon depending on the prediction. Display de Female Icon if its female, Male Icon if its Male or Other Icon if its other. 
o	Recources: 
o	Female Icon https://www.toptal.com/designers/htmlarrows/symbols/female-sign/
o	Male Icon https://www.toptal.com/designers/htmlarrows/symbols/male-sign/
o	None Icon https://www.toptal.com/designers/htmlarrows/punctuation/non-breaking-hyphen/ 
 
-	Option B: Create a Gauge chart that places the needle according to the type
                              




## Dashboard Live Demo (heroku)