import json
import iso8601

datafile = open('sample-data.json',"r")
data = json.loads(datafile.read())
#print(data)
#print(len(data))
for dic in data:
    print("name:            "+dic['name'])
    #print("created at:      "+dic['created_at'])
    print("created at:      "+str(iso8601.parse_date(dic['created_at'])))
    print("status:          "+dic['status'])
    if (dic['status']!="Stopped"):
        print("memory usage:    "+str(dic['state']['memory']['usage']))
        print("cpu usage:       "+str(dic['state']['cpu']['usage']))
        for addr in dic['state']['network']:
            print(addr)

    print("----------")
    print(dic.keys())
    print("----------")
    print("----------")
#print(data[1]['state'])
#print(json.dumps(data, indent=4))
datafile.close()
