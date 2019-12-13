from timeit import default_timer as timer
import markovify
import os
import io
import json
import argparse
from datetime import datetime, timedelta
from random import randrange

# Get raw text as string.
infile = os.path.dirname(__file__) + '/ESL conversatison.txt'
with io.open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)


def createTime():
    oldest = datetime.strptime('1/1/1983', '%m/%d/%Y')
    newest= datetime.strptime('12/31/2019', '%m/%d/%Y')
    delta = newest - oldest
    dateRange = (delta.days)
    randomDays = randrange(dateRange)    
    date = oldest + timedelta(days=randomDays)

    return date

date = createTime()

# Fill a list with generated sentences
data = []
count =1 
for i in range(100000):
    message = text_model.make_sentence()
    data.append({
        'messageID' : count,
        'message' + str(i): message
        })


# Write the list to a json file
messages = os.path.dirname(__file__) + '/messages.json'
with io.open(messages, 'w+', encoding='utf-8') as f:
    json.dump(data, f)# , indent=4) 
        # indent=4 gives the file pretty formatting but uses many more lines

input()