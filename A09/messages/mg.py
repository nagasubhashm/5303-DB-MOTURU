import markovify
import pymongo  # package for working with MongoDB

#client = pymongo.MongoClient("mongodb://localhost:27017/")

# Get raw text as string.
with open("11.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
#for i in range(5):
#    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 50 characters
for i in range(100000):
    print(text_model.make_short_sentence(50))
