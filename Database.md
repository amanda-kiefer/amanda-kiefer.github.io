# Client/Server System

For the Databases portion of the ePortfolio, I have selected a Client Server project which was coded in Python and developed within the Codio environment. This project illustrates proficiency in creating scripts using the Python language for the purpose of conducting CRUD function on a database. The Codio environment utilizes a virtual Linux operating system, and the use thereof illustrates proficiency in multiple operating systems. Additionally, the work completed for this assignment displays the ability to index and organize the information within the database for more efficient queries. This will be demonstrated using screenshot images and an informative summary essay. For these reasons, I have selected this artifact for the Database portion of the ePortfolio. 
	I have enhanced the CRUD operations for the Python scripts. The original assignment was intended to show proficiency in the subject but did not provide scripts that would be functional in a real-world scenario. This is because the scripts were developed to preform one very specific task, per project requirements. I have expanded the abilities of these scripts so that they can be utilized in a realistic manner. For the script to update the database, the original functionality only allowed the Volume key-value pair to be updated. This has been enhanced to allow the user to select any of the available key-value pair options to update. The script first asks to the Ticker ID, which is used to identify the specific data piece to be updated. Then the user is asked first for the key, and then for the updated value. When the update is performed correctly, a success message is displayed. 
	The query script has also been updated substantially. This script had three options to guide the user’s query. I have enhanced this by adding three addition options. These options have been completed through the code so that they are fully functional. They allow the user to search the database based on Profit Margin (all results within a range), Country, and Company name. In addition to these enhancements, title strings have been added which will be output when the scripts are executed. The purpose of this to is provide details on what each script will do and how it should be utilized. 
	A few aspects of this project were completed using a RESTful web service. Because of how it was developed in Codio, the curl function was required to test these URIs. I have enhanced this part of the project to show better on the GitHub ePortfolio platform by creating additional scripts. These scripts are for obtaining a summary of data for a particular datapoint, and for getting a list of top results based on industry. I believe this format is better suited for the ePortfolio environment. Databases are one of the areas where I have limited experience. My courses at SNHU which discuss this topic have been limited. I am proud of my work with the scripts and with the functionality they contain. This time spent reworking and enhancing this project has helped to reinforce what I have learned in previous courses concerning database management and manipulation. 

# Python Scripts:

## Create
```
import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.market
collection = db.stocks

print("Add New Key-Value Pair to Stock Using Ticker ID")
tick = input('Ticker: ')
arr = input('New Doc: ')

def create_document(document):
  try:
    collection.update({"Ticker" : tick}, {"$set" : document})
    print("Successfully Added ")
    return json.loads(json.dumps(document, indent=4, default=json_util.default))
  except ValidationError as ve:
    abort(400,str(ve))
    return result

def main():
  myDocument = arr 
  
  print create_document(myDocument)
  
main()
```

## Read / Query
```
import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.market
collection = db.stocks

print("Select a Query to Perform on the Database")
menu = input(
  '50 Day Moving Average: Press 1  | Industry Search: Press 2 | Search Industry By Sector: Press 3  |\n'
  'Profit Margin Seach: Press 4    | Country Search : Press 5 | Search by Company: Press 6')

def read_document(document):
  if 0 < menu < 7:
    if menu == 1:
      max = input('Max Range: ')
      min = input('Min Range ')
      result = collection.find({"50-Day Simple Moving Average" : {"$gte" : min, "$lte" : max}})
      for doc in result:
        print(doc)
    elif menu == 2:
      arr = input('Enter Industry: ')
      result = collection.find({"Industry" : arr})
      for doc in result:
        print(doc)
    elif menu == 3:
      sec = input('Enter Sector: ')
      result = collection.find({"Sector" : sec}, {"Industry" : 1})
      for doc in result:
        print(doc)
    elif menu == 4:
      max = input('Max Range: ')
      min = input('Min Range: ')
      result = collection.find({"Profit Margin" : {"$gte" : min, "$lte" : max}})
      for doc in result:
        print(doc)
    elif menu == 5:
      arr = input('Enter Country: ')
      result = collection.find({"Country" : arr}, {"Company" : 1})
      for doc in result:
        print(doc)
    elif menu == 6:
      arr = input('Enter Company: ')
      result = collection.find({"Company" : arr})
      for doc in result:
        print(doc)
  else:
    print("Error: Enter 1, 2, 3, 4, 5, or 6")

def main():
  myDocument = menu
  read_document(myDocument)
  
main()
```

## Update
```
import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.market
collection = db.stocks

print("Update Key-Value Pair to Stock Using Ticker ID")
tick = input('Ticker: ')
key = input('Key to be Updated: ')
arr = input('New Value: ')


def update_document(document):
  try:
    collection.update({"Ticker" : tick}, {"$set" : {key : document}})
    print("Document Successfully Updated ")
    return json.loads(json.dumps(document, indent=4, default=json_util.default))
  except ValidationError as ve:
    abort(400,str(ve))
    return result

def main():
  myDocument = arr  
  print update_document(myDocument)
  
main()
```

## Delete
```
import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.market
collection = db.stocks

print("Delete a Stock Using Ticker ID")
arr = input('Ticker: ')

def delete_document(document):
  try:
    collection.remove({"Ticker" : arr})
    print("Document Successfully Removed: ")
    return json.loads(json.dumps(document, indent=4, default=json_util.default))
  except ValidationError as ve:
    abort(400,str(ve))
    return result

def main():
  myDocument = arr  
  print delete_document(myDocument)
  
main()
```

## Top 5 Query
```
import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.market
collection = db.stocks

print("View Top 5 Stocks by Industry")
arr = input('Industry: ')

def get_top5(document):
  try:
    result = collection.find({"Industry" : "Diagnostic Substances"}, {"Price" : -1}).limit(5)
    return dumps(result)
  except ValidationError as ve:
    abort(400,str(ve))
    return result

def main():
  myDocument = arr  
  print get_top5(myDocument)
  
main()
```

## Summary Query
```
import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.market
collection = db.stocks

print("View Stock Summary using Ticker ID")
arr = input('Ticker: ')

def get_summary(document):
  try:
    result = collection.find({"Ticker": document}, {"Company": 1, "Profit Margin": 1, "Performance (YTD)": 1, "Quick Ratio": 1})
    return dumps(result)
  except ValidationError as ve:
    abort(400,str(ve))
    return result

def main():
  myDocument = arr  
  print get_summary(myDocument)
  
main()
```

