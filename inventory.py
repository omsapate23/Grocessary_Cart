#This is invetory
#Dictionary datatype is used to create this database (Nested Dictionary)

items_database = {
    "1001": {"name":"Bread", "price": 20},
    "1002": {"name":"milk",  "price": 30},
    "1003": {"name":"banana", "price":60},
    "1004": {"name":"pen",    "price":10},
    "1005": {"name":"paneer", "price":240},
    "1006": {"name":"aloo bhujiya", "price":56},
    "1005": {"name":"curd", "price": 30},
    "1005": {"name":"drinking water", "price":20},
    "1005": {"name":"Thumbs-up", "price":40}
    }

def get_item(barcode):
    #To get access the item
    return items_database.get(barcode)
