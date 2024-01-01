// Connect to MongoDB
db = db.getSiblingDB('personal_details');

// Create a collection called 'details'
db.createCollection('details');

// Create a unique index for the Unique ID field
db.details.createIndex({ "unique_id": 1 }, { unique: true });