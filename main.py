from pymongo import MongoClient
from random import randint

# Establish connection to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['personal_details']
collection = db['details']

def create_record(data):
    unique_id = randint(10000, 99999)  # Generate a random unique ID
    data['unique_id'] = unique_id
    collection.insert_one(data)

def read_record(unique_id):
    return collection.find_one({"unique_id": unique_id})

def update_record(unique_id, data):
    collection.update_one({"unique_id": unique_id}, {"$set": data})

def delete_record(unique_id):
    collection.delete_one({"unique_id": unique_id})

if __name__ == "__main__":
    # List of data inputs
    data_list = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "age": 30,
            "address": "123 Main St",
            "contact_number": "123-456-7890",
            "nationality": "US"
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "age": 25,
            "address": "456 Elm St",
            "contact_number": "987-654-3210",
            "nationality": "UK"
        },
        {
            "first_name": "Michael",
            "last_name": "Johnson",
            "age": 35,
            "address": "789 Oak St",
            "contact_number": "111-222-3333",
            "nationality": "CA"
        },
        {
            "first_name": "Emily",
            "last_name": "Williams",
            "age": 28,
            "address": "101 Pine St",
            "contact_number": "444-555-6666",
            "nationality": "AU"
        },
        {
            "first_name": "David",
            "last_name": "Brown",
            "age": 40,
            "address": "202 Maple St",
            "contact_number": "777-888-9999",
            "nationality": "NZ"
        }
    ]

    # Perform CRUD operations for each data input
    for data in data_list:
        # Create a record
        create_record(data)
        print(f"Created record for {data['first_name']} {data['last_name']}")

        # Read the created record
        record = read_record(data['unique_id'])
        print("Read record:", record)
        print('\n---------------------------------------------------------------\n')

        # Update the record
        update_data = {"age": data['age'] + 1}  # Increment age by 1
        update_record(data['unique_id'], update_data)
        updated_record = read_record(data['unique_id'])
        print("Updated record:", updated_record)
        print('\n---------------------------------------------------------------\n')

        # Delete the record
        delete_record(data['unique_id'])
        deleted_record = read_record(data['unique_id'])
        print("Deleted record:", deleted_record)  # This should print 'None'
        print('\n---------------------------------------------------------------\n')

    print('CRUD operations completed for all data inputs\n')
