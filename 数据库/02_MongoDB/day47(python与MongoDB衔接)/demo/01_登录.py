from pymongo import *

# uri = "mongodb://%s" % ('localhost:10001')
uri = "mongodb://127.0.0.1:10001"

#客户端对象
client = MongoClient(uri)
#连接的数据库
db = client.laowang
#操作的数据库中的集合
t1 = db.t1
print(t1.find_one())
client.close()



client = MongoClient('127.0.0.1',10001)
db = client.laowang
t1 = db.t1
print(t1.find_one())
client.close()



uri = "mongodb://d2:123456@127.0.0.1:27017/d2"
client = MongoClient(uri)
db = client.d2
t1 = db.t1
print(t1.find_one())
client.close()


client = MongoClient('127.0.0.1',27017)
db = client.d2
#认证
db.authenticate('d2','123456')

t1 = db.t1
print(t1.find_one())
client.close()