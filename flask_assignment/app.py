from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
MONGO_URI = 'mongodb+srv://mridulmittal2003:2101JanM@cluster0.stnrtiy.mongodb.net/?retryWrites=true&w=majority'
DB_NAME = 'mydatabase'
COLLECTION_NAME = 'students'

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        college = request.form.get('college')
        stream = request.form.get('stream')
        # Create a document to be inserted into the collection
        student = {
            'name': name,
            'college': college,
            'stream':stream
        }

        # Insert the document into the collection
        collection.insert_one(student)

        return 'Data saved successfully!'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
