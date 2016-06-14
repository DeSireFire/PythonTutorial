from pymongo import *


def select():
    uri = "mongodb://d2:123456@127.0.0.1:27017/d2"
    client = MongoClient(uri)
    db = client.d2
    t1 = db.t1


    #print(t1.find_one())

    cur = t1.find()

    for i in cur:
        print(i)

    # print(cur.next())
    # print(cur.next())
    # print(cur.next())
    client.close()


def insert1():
    uri = "mongodb://d2:123456@127.0.0.1:27017/d2"
    client = MongoClient(uri)
    db = client.d2
    t1 = db.t1
    #python字典键必须加引号
    t1.insert_one({'num':1})

    client.close()

def insert2():
    uri = "mongodb://d2:123456@127.0.0.1:27017/d2"
    client = MongoClient(uri)
    db = client.d2
    t1 = db.t1

    t1.insert_many([{'num':4,'name':'a'},{'num':5,'name':'b'}])

    client.close()

def delete1():
    uri = "mongodb://d2:123456@127.0.0.1:27017/d2"
    client = MongoClient(uri)
    db = client.d2
    t1 = db.t1

    t1.delete_one({'num':{'$gt':3}})

    client.close()
def delete2():
    uri = "mongodb://d2:123456@127.0.0.1:27017/d2"
    client = MongoClient(uri)
    db = client.d2
    t1 = db.t1

    t1.delete_many({'num':{'$gte':3}})

    client.close()


def update1():
    uri = "mongodb://d2:123456@127.0.0.1:27017/d2"
    client = MongoClient(uri)
    db = client.d2
    t1 = db.t1

    t1.update_one({'num':{'$gte':4}},{'$set':{'xx':300}})

    client.close()

def update2():
    uri = "mongodb://d2:123456@127.0.0.1:27017/d2"
    client = MongoClient(uri)
    db = client.d2
    t1 = db.t1

    t1.update_many({'num':{'$gte':4}},{'$set':{'num':300}})

    client.close()

if __name__ == '__main__':
    #insert1()
    #insert2()
    #delete1()
    #delete2()
    #update1()
    update2()
    select()


