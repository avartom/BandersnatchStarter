from os import getenv

from certifi import where
from dotenv import load_dotenv, find_dotenv
from pandas import DataFrame
from pymongo import MongoClient




class Database():
    """A database class to connect to MongoDB and CRUD data.
    Attributes
    ----------
    collection: dict 
        a collection of data in the form of a dictionary
    Methods
    ----------
    seed(amount:dictionary) 
    reset()
    count()
    dataframe()
    html_table()
  """
    load_dotenv(find_dotenv())
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self, collection: str):
        self.collection = self.database[collection]
        """
        Connects to database usning .env file with 
        the name initialized to colletion
        
        parameters
        ----------
        collection: str
        """

    
    def seed(self, amount):
        self.collection.insert_many(amount)
        """
        Inserts the specified number of documents list into the collection.
        
        parameters
        ----------
        amount: collection of dict 
        """
        
    def reset(self):
        self.collection.delete_many({})
        """
        Deletes all documents from the collection.
        """

    def count(self) -> int:
        """
        returns the number of documents in the collection
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        '''
        Returns a DataFrame containing all documents in the collection
        '''
        return DataFrame(self.collection.find({}, {"_id": False}))

    def html_table(self) -> str:
        '''
        Returns an HTML table representation of the DataFrame, or None if the collection is empty.
        '''
        return self.dataframe().to_html()


if __name__ == '__main__':
    db = Database("collection")
    print(db.count())
    