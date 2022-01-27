# CRYPTO PUNKS Machine Learning Project

### ✓ Topic Selection
Explore the surging world of  NFT's, focused on a collection of 10,000 digital assets known as Crypto Punks. The aim is to analize the associated *PNG* images using Machine Learning and establish which graphical features and attributes determine either the type of Crypto Punk (*'Male'*, *'Female'*, or *'Other'* -*'Zombie'*, *'Ape'* or *'Alien'*-) or if the Crypto Punk has glasses (*'3D Glasses'*, *'Big Shades'*, *'Classic Shades'*, *'Horned Rim Glasses'*, *'Nerd Glasses'*, *'Regular Glasses'*, *'Small Shades'*,  *'VR'* and *'Welding Goggles'*). 

### ✓ Reason for Topic Selection
With this project we seek to apply our data analytics skills using Machine Learning while expanding our knowledge-base to include an image classification model, as this is an increasingly relevant field in the use of Machine Learning. We also wanted to further our skills in using *MongoDB*, a non-relational database and cloud resource deployment using *Amazon Web Services*.

### ✓ Description of Data Source
CryptoPunks were created by Larva Labs in 2017. They are the first NFT series to catch popular interest, and one of the most actively traded (https://www.larvalabs.com/cryptopunks). 

The dataset consists of a *JSON* file with all Crypto Punk blockchain transactions as well as the relevant attributes of the 10,000 CryptoPunks such as type (*'Male'*, *'Female'*, *'Zombie'*, *'Ape'* or *'Alien'*) and any of 87 different accessories (such as beards, glasses, hair, etc.). 

The dataset is available in Kaggle at:

https://www.kaggle.com/tunguz/cryptopunks?select=txn_history-2021-10-07.jsonl

A second dataset contains a folder with individual *.png* image files for each of the 10,000 Crypto Punks. The image files can be found at:

https://www.kaggle.com/tunguz/cryptopunks?select=imgs

### ✓ What We Hope to Answer:

Our project runs two models. These are used to predict, given an image file, the attributes of the image. The first model predicts which type of CryptoPunks the image represents, while the second model predicts if the image has glasses or not. 


### ✓ Description of Team Communication Protocols

- The team kept constant communication through a dedicated *Slack* channel and *Zoom* virtual calls.
- The team also shared a *Google Docs* folder for relevant documents, such as interesting articles on image processing techniques, presentation drafts and project rubrics. 
- Each member uploaded working files to their own branch, with final code merged to a main branch. 
- Tasks were divided among the team members according to the different roles (triangle, circle, square), but also according to team member expertise.

## Machine Learning Model

The preliminary data included column fields describing the transactional information for the 10,000 Crypto Punk collection, including fields describing the relevant Crypto Punk characteristics (*id*, *type* and *accessories*). 

After exploring the available data, we chose the features we wanted to base the Machine Learning Model on.

We decide to create 2 models: one classification model to determines which *type* of Crypto Punk the image represented, and a second binary model to determine if the Crypto Punk image had glasses or not. For both models we followed the same process:

* The data was split into training and test data using the train_test_split function. We used the default 75% to 25% split.

* The data was fed to a Convolutional - Neural Network (CNN) Model made up of several layers.

Some of these layers use Relu, Sofmax (for Classification model) and Sigmoid (for Binary Model), the accuracy rate for both model was 100%. This means our models accurately predicted the outcome of nearly all the Crypto Punk images.

The image below provides a better understanding of the layers included in the model's construction:
![ConvNN_Image](https://user-images.githubusercontent.com/87447639/149681824-c98a2e0d-75c0-4c75-8516-46efc8be58a7.png)


The input data for the models is a list of numpy arrays of dimension 24 x 24 x 4. These arrays represent the digital information that corresponds to the image. The original images are 24 pixels by 24 pixels, and the arrays express the value of each pixel as a number between 0 and 255, representing the RGB color of the pixel. Before providing the input to the models, the arrays were normalized by dividing the values by 255, so that they would fall in a range between 0 and 1.

For the Classification model, the output label is *'type'*, represented as a one_hot_encoded field.

For the Binary model, the output label is 'glasses_ML'

The following tables present the confusion matrix after running the model: 

![confusionmatrix](https://user-images.githubusercontent.com/87447639/151213205-8481797b-eab8-4478-9d85-1860cb03c1a3.PNG)

Binary Model

![binarymodel](https://user-images.githubusercontent.com/87447639/151262580-ebf44de9-7340-4b24-8444-a6195171bcfc.PNG)

Classification Model

![clasificationmodel](https://user-images.githubusercontent.com/87447639/151262587-fcd003dd-8769-40e6-9e25-af9a51351331.PNG)



INSERT ACCURACY PRINTOUT FOR EACH MODEL



## Database

Our database consists of a *MongoDB* database, which has been loaded to the cloud using *MongoDB Atlas* cloud hosting service.

The database, *crypto_punks_mdb*, containes 3 main collections:

- *crypto_punks_col* with 10,000 documents each containing 10 fields.
- *traders_col* with 132526 documents each containing 9 fields.
- *txn_history_col* with 167,492 documents each containing 12 fields.

The collections can be cross-referenced using the field *'punk_id'* as key.

A fourth collection, *attributes_col*, represents a dictionary of attributes and their relative frequencies in the Crypto Punk collection.

The database and collections can be visualized using *MongoDB Compass* by establishing a connection with *MongoDB Atlas* through a secure URL.

## Description of Data Exploration Phase

![Database_ERD](https://user-images.githubusercontent.com/87447639/149681985-a86e2efd-dbc7-48c5-9e67-369967f2df83.png)

Two datasets where available for our analysis. One contains all blockchain transactions since the minting of the Crypto Punk NFT collection, and is available as a *JSON* file in Kaggle. The other associated data set is a collection of 10,000 *png* files also available in Kaggle, containing the individual images of each Crypo Punk.

Our ETL process entailed reading the *JSON* file and creating utilitary dataframes for the different elements of our analysis.

One dataframe extracts the unique Crypto Punk *'punk_id'*, their unique *'type'* and the *'accessories'* associated with each individual Crypto Punk. By analyzing this data, we determined that several *'types'* were underrepresented and would pose a challenge for the accuracy of our Machine Learning predictions. These *'types'*, which include *'Ape'*, *'Alien'* and *'Zombie'*, where grouped into a class *'Other'*.


INSERT TABLE WITH TYPE DISTRIBUTION


Another dataframe decomposes all the unique *'accessories'* present in the collection, and establishes the count of Crypto Punks sharing this accessory. We also used this dataframe to group *'accessories'* into broad classes (for example, beards, headgear, glasses) in order to select a feature with variable visual representation that could lend itself for machine learning recognition.

Once we had analyzed the data and decided on our prediction target, we created additional dataframes containing columns with numerical representation of the features: *'type_ML'* with 0, 1 or 2 to represent if the type was *'Male'*, *'Female'* or *'Other'*, and *'glasses_ML'* with 0 or 1 to represent if the Crypto Punk did not have or did have glasses.

For each Crypto Punk *'punk_id'*, we looped through the ids to read each *png* image file, convert the image into a bitmap array, and store the associated *'punk_id'* and bitmap array in a list of dictionaries. With this list, we could then re-create any of the images using plotting functions without having to access the original *png* files.

A second list of dictionaries was also created for machine learning purposes, where the bitmap arrays were normalized. The original bitmap arrays were 24x24x4, with the numerical values in the arrays representing an RGB color between 0-255. By normalizing these numbers to conform to a range between 0 and 1 (achieved by dividing each one by 255), we improved the input data for the machine learning model.

Finally, we created additional dataframes for the transaction history of the whole collection by eliminating unnecesary columns, and an additional dataframe to identify each trader or collector of these NFTs and their own transaction history.

All of these dataframes where exported as *csv* files to our repository *Data* folder.

In addition to the ETL process notebook, another notebook converts each of the *csv* files to *json* format. These are stored in the *JSON_datafiles* subfolder of our *Data* repository folder. It also consolidates the *csv* files into 3 collections that are stored in our *MongoDB* local host.

A third ETL notebook reads the *csv* files, consolidates them into the three collections, but this time exports them to a *MongoDB Atlas* cluster in the cloud.

The database is accessed by our visualization dashboard through a connection string pointing to the secure *MongoDB Atlas* url associated with our database.

### ✓ Presentation

Our presentation can be found here Google Slide Presentation https://docs.google.com/presentation/d/17QrwkucoQluYAyOd0sKMI5KkpIkx8blE9acwNgYu1Bc/edit#slide=id.p

### ✓ Dashboard

Our dashboard consists of an *html* webpage connected to a *Python* application, *app.py*. The dashboard provides the viewer the option to generate a random Crypo Punk id through the use of an interactive button. Once generated, the image of the Crypto Punk is updated, a table of facts is provided on the Crypo Punk including how many other Crypto Punks share the same attributes and the rarity score of these attributes. The dashboard also makes a prediction on the *type* and if the accessories include glasses. Finally, the dashboard presents a price history chart for the Crypto Punk, as well as a network graph that illustrates it's trading history. The data displayed on the dashboard is processed from reading the *MongoDB* data available in the *Atlas* cluster, while the images are processed, exported to the cloud using *Amazon Web Services* *S3* bucket, and fed to the dashboard via *url* links.

The following is an image of our actual dashboard.

![Visualization_Screenshot](https://user-images.githubusercontent.com/87447639/151211870-627a617b-7d5f-48bc-8a53-1c0d40e5e4ab.png)
