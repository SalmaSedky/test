import pymongo
client = pymongo.MongoClient("mongodb+srv://salmasedky:salma123@cluster0.werfp6r.mongodb.net/?retryWrites=true&w=majority")
db = client.test


print(db)


d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )