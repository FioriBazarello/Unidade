from pymongo import MongoClient

database_name = "unidade_db"
con = MongoClient('mongodb://localhost:27017')
db = con[database_name]

def insert_into(col_name, data):
    """ Insert data into a collection.

    Usage:
     - controls.database.insert_into('collection', {'foo':'bar'})

    Parameters:
     - `col_name`: The collection name
     - `data`: A data/value object to be inserted.
    """
    collection = db[col_name]
    collection.insert_one(data)

def get_from(col_name, query):
    """ Find the documents returned from a query.

    Usage:
     - controls.database.get_from('collection', {'foo':'bar'})

    Return:
     - Array with documents returned from collection

    Parameters:
     - `doc`: The collection name
     - `data`: A data/value object with the properties to be found.
    """
    collection = db[col_name]
    cursor = collection.find(query)

    result = []
    for value in cursor:
        result.append(value)

    return result