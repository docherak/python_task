try:
    import sys
    import json
    from datetime import datetime, timezone
    import pymongo
    from pymongo import MongoClient
except Exception:
    print("Some modules are missing!\nCheck requirements.txt!")
    sys.exit(1)

cluster = MongoClient("mongodb+srv://admin:<PASSWORD>@cluster0.gbnhq7y.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection=db["test"]

with open('sample-data.json',"r") as datafile:
    data = json.loads(datafile.read())
    _id=0 
    for dic in data:
        new_item={}

        new_item["_id"]=_id
        
        #print("name:            "+dic['name'])
        new_item["name"]=str(dic['name'])

        #print("created at:      "+str(datetime.fromisoformat(dic['created_at']).replace(tzinfo=timezone.utc).timestamp()))
        new_item["created_at"]=str(datetime.fromisoformat(dic['created_at']).replace(tzinfo=timezone.utc).timestamp())
        
        #print("status:          "+dic['status'])
        new_item["status"]=str(dic["status"])
        
        addrlst=[]
        
        if (dic['status']=="Running"):

            #print("memory usage:    "+str(dic['state']['memory']['usage']))
            new_item["memory_usage"]=str(dic['state']['memory']['usage'])

            #print("cpu usage:       "+str(dic['state']['cpu']['usage']))
            new_item["cpu_usage"]=str(dic['state']['cpu']['usage'])

            for addr in dic['state']['network']:
                for adapt in dic['state']['network'][str(addr)]["addresses"]:
                    addrlst.append(adapt["address"])
        
            #print("addresses:")
            new_item["addresses"]=addrlst
            #print(addrlst)
        
        #print("----------")
        print(new_item)
#        collection.replace_one(new_item, new_item)
        collection.insert_one(new_item, new_item)
        
        _id+=1
