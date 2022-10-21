# Modules:
try:
    import sys
    import json
    from datetime import datetime, timezone
    import pymongo
    from pymongo import MongoClient
except Exception:
    print("Some modules are missing!\nCheck requirements.txt!")
    sys.exit(1)

# Functions:
def parse(dic: dict, _id: int) -> dict:
    
    new_item = {}
    
    new_item["_id"] = _id 

    new_item["name"] = str(dic['name'])
    new_item["created_at"] = datetime.fromisoformat(dic['created_at']).replace(tzinfo=timezone.utc).timestamp()
    new_item["status"] = str(dic["status"])
    
    addrlst = []
    
    if (dic['status'] == "Running"):

        new_item["memory_usage"] = dic['state']['memory']['usage']
        new_item["cpu_usage"] = dic['state']['cpu']['usage']

        for addr in dic['state']['network']:
            for adapt in dic['state']['network'][str(addr)]["addresses"]:
                addrlst.append(adapt["address"])
    
        new_item["addresses"] = addrlst
    
    return new_item

def main() -> None:
    
    # Database connection:
    cluster = MongoClient("mongodb+srv://admin:pepega@cluster0.gbnhq7y.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["test"]
    collection = db["test"]

    # Parsing:
    profiles = []
    with open(sys.argv[1], "r") as datafile:
        data = json.loads(datafile.read())
    
        for idx, item in enumerate(data):
            profiles.append(parse(item, idx))

        collection.insert_many(profiles)

# Main:
if __name__ == "__main__":
    main()
