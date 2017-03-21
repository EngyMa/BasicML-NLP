'''
This program generates fake data using the Python library 'random', and dumps the data into a JSON file.
Currently, only one temperature and one humidity sensor is assumed on a single machine.
'''

#Importing libraries
import time
from datetime import datetime
import csv
import random
import json
#from thread import start_new_thread

#Populate the JSON file
def create_json():
	while True:
		temp = random.randrange(25, 150) #generate random temperature value
		humidity = random.randrange(25, 100) #generate random humidity value
		time.sleep(1) #new entry every 1 second
		ts = str(datetime.now()) #get current timestamp		
		jdoc = {} #a JSON document
		#put attributes in a document
		jdoc["timestamp"] = ts 
		jdoc["temp"] = temp
		jdoc["humidity"] = humidity
		#dump into JSON file
		with open("test1.json", "a") as outfile:
			json.dump(jdoc, outfile) #write to output JSON file

#call to function
create_json()			