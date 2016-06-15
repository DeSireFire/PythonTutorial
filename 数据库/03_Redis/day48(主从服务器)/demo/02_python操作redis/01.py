#推荐网站
#http://python.jobbole.com/87305/





import redis

#获取连接对象 当我们用Redis和StrictRedis创建连接时，其实内部实现并没有主动给我创建一个连接，我们获得的连接是连接池提供的连接，这个连接由连接池管理，所以我们无需关注连接是否需要主动释放关闭的问题。另外连接池有自己的关闭连接的接口，一旦调用该接口，所有连接都将被关闭，连接池的操作不需要程序员管理，系统redis模块自动管理好了。
conn = redis.StrictRedis('127.0.0.1',6379,password=123456)
#如果是多个增删改，使用管道对象，默认先存在管道中，当execute时候，保存到数据库文件中
pip = conn.pipeline()
pip.set('a',1)
pip.set('b',2)
pip.set('c',3)
#提交
pip.execute()


#查询的时候，可以使用pip，也可以使用conn对象
print(conn.get('a'))


print('哦了')

