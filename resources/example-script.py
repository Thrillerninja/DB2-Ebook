# Sample airline document
sample_airline = {
	"type": "airline",
	"id": 8091,
	"callsign": "CBS",
	"iata": None,
	"icao": None,
	"name": "Couchbase Airways",
}
key = "airline_8091"

# Create a document with specific ID
result = collection.insert(key, sample_airline)

# Retrieve a document by ID
result = collection.get(key)

# Update a document by ID
sample_airline["name"] = "Couchbase Airways!!"
result = collection.replace(key, sample_airline)

# Delete a document by ID
result = collection.remove(key)
