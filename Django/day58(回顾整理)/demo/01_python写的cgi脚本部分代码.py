'''
什么是Web框架?

Django是一个卓越的新一代Web框架，而使用Django 这个web框架的意义是什么呢？

要回答这个问题，让我们来看看通过编写标准的CGI程序来开发Web应用，这在大约1998年的时候非常流行。
编写CGI Web应用时，你需要自己处理所有的操作，就像你想烤面包，但是都需要自己生火一样。
下面是实例，一个简单的CGI脚本，用Python写的，读取数据库并显示最新发布的十本书：
'''


#!/usr/bin/python

import MySQLdb

print "Content-Type: text/html"
print
print "<html><head><title>Books</title></head>"
print "<body>"
print "<h1>Books</h1>"
print "<ul>"

connection = MySQLdb.connect(user='me', passwd='letmein', db='my_db')
cursor = connection.cursor()
#从数据库查询所有书的名字
cursor.execute("SELECT name FROM books ORDER BY pub_date DESC LIMIT 10")
#遍历所有的书
for row in cursor.fetchall():
    print "<li>%s</li>" % row[0]

print "</ul>"
print "</body></html>"

connection.close()


'''
代码十分简单。首先，根据CGI的要求输出一行Content-Type，接下来是一个空行。
再接下来是一些HTML的起始标签，然后连接数据库并执行一些查询操作，获取最新的十本书。
遍历这些书，同时生成一个HTML的无序序列。
最后，输出HTML的结束标签并且关闭数据库连接。3Matty

类似这样的一次性动态页面，从头写起并不是最好的办法。
其中一点，这些代码简单易懂，就算是一个开发初学者都能理解这16行代码从开始到结束做了些什么，不需要阅读额外的代码。
同样这16行代码也很容易部署：只需要将它保存在名为“latestbooks.cgi”的文件里，上传至网络服务器，通过浏览器访问即可。

但是Web应用远远要复杂很多，这种方法就不再适用，而且你将会要面对很多问题：
	
	1、当多个动态页面需要同时连接数据库时，将会发生什么？
	   当然，连接数据库的代码不应该同时存在于各个独立的CGI脚本中，所以最踏实的做法是把这些代码重新组织到一个公共函数里面。


	2、一个开发人员真的需要去关注如何输出Content-Type以及完成所有操作后去关闭数据库么？
	   此类问题只会降低开发人员的工作效率，增加犯错误的几率。那些初始化和释放相关的工作应该交给一些通用的框架来完成。


	3、如果这样的代码被重用到一个复合的环境中会发生什么？
	   每个页面都分别对应独立的数据库和密码吗？从这点看来，就需要一些环境相关的配置文件。


	4、如果一个Web设计师，完全没有Python开发经验，但是又需要重新设计页面的话，又将 发生什么呢？
	   理想的情况是，页面显示的逻辑与从数据库中读取书本记录分隔开，这样 Web设计师的重新设计不会影响到之前的业务逻辑。



以上正是Web框架致力于解决的问题。
Web框架为应用程序提供了一套程序框架， 这样你可以专注于编写清晰、易维护的代码，而无需从头做起。简单来说，
这就是Django所能做的。
'''