import pymongo
from bson.objectid import ObjectId
from bson.objectid import InvalidId

from config import CLIENT_URI, COLLECTION_NAME, DATABASE_NAME

client = pymongo.MongoClient(CLIENT_URI)
db = client[COLLECTION_NAME]
orders = db[DATABASE_NAME]

class Order:
    """Order is an object that has [to] and [from] properties. It also can be taken or not taken"""
    def __init__(self, llm_from, llm_to):
        self.llm_to = llm_to
        self.llm_from = llm_from
        self.taken = False

    def json_order(self):
        """Generate json-like object from order"""
        json_order = {"from": self.llm_from, "to": self.llm_to, "taken": self.taken}
        return json_order

def create_order(llm_from, llm_to):
    """Create and upload order to the MongoDB"""
    order = Order(llm_from, llm_to)
    order_id = orders.insert_one(order.json_order()).inserted_id
    print(order_id, "is placed")
    return order_id

def list_orders():
    """List all orders in database"""
    results = orders.find({'taken': False})
    for order in results:
        print(f'{order.get("_id")}, {order.get("from")}, {order.get("to")}')
    return results

def take_order(id):
    """Find order using id and change its \"taken\" field to True"""
    try:
        taken_order = orders.find_one({"_id": ObjectId(id)})
        if taken_order is None:
            print(f"order \"{id}\" does not exist")
        elif taken_order.get('taken'):
            print(f"order \"{id}\" already taken")
        elif taken_order.get('taken')==False:
            orders.find_one_and_update({"_id": ObjectId(id)}, {'$set': {'taken': True}})
            print(f"order \"{id}\" is successfully taken")
    except InvalidId:
        return("ERROR: Invalid id. Id should be 24-character hex string")