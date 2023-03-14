

import pymongo

# Connection URL and database name
url = "mongodb://localhost:27017/"
db_name = "myproject"

# Create a MongoClient
client = pymongo.MongoClient(url)

# Get the database
db = client[db_name]

# Insert an HTML document
collection = db["documents"]
html_doc = {
    "title": "My HTML Document",
    "content": "<html><head><title>My HTML Document</title></head><body><h1>Hello World!</h1></body></html>"
}
insert_result = collection.insert_one(html_doc)
print("HTML document inserted with ID:", insert_result.inserted_id)

# Retrieve the HTML document
query = {"title": "My HTML Document"}
html_doc = collection.find_one(query)
html_content = html_doc["content"]
print("HTML content:", html_content)

# Close the MongoClient
client.close()
