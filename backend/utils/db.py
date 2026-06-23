import os
from pymongo import MongoClient

_mock_db = None

def get_db():
    global _mock_db
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    try:
        # Try connecting with a short timeout so it doesn't hang
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
        # Force a command to test connection
        client.admin.command('ping')
        db = client.get_database("kriyeta")
        return db
    except Exception as e:
        print(f"[WARNING] Could not connect to real MongoDB (URI: {mongo_uri}). Falling back to in-memory mongomock database. Error: {e}")
        if _mock_db is None:
            import mongomock
            client = mongomock.MongoClient()
            _mock_db = client.get_database("kriyeta")
        return _mock_db
