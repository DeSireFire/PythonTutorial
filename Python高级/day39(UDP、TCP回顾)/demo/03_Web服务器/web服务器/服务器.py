#-*- coding:utf-8 -*-
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
class MyHandler(BaseHTTPRequestHandler):    #继承BaseHTTPRequestHandler类里面所有的方法    
	def do_GET(self):        
	try:           
	 #当服务器接收到GET请求后调用此方法并尝试打开客户端传来的路径
	 #('移除前导"/"') 如果一切正常就会return一个ok            
	 ##比如我的url是 127.0.0.1/cehsi.html (第八行)会读取当前路径下面的ceshi.html
		files = open(self.path[1:],'r')            
		self.send_response(200)            
		#如果找到了就返回一个200            
		self.send_header('Content-type', 'text/html')            
		#这个是数据的头部文件            
		self.wfile.write(files.read())            
		#读取html文件并返回给用户            
		files.close()            
		#释放文件占用的系统资源        
	except:            
		self.send_error(404, 'File not found: %s '% self.path)            
		#如果报错就提示404 没有找到文件
def main():    
	try:        
		server = HTTPServer(('', 8088), MyHandler)        
		#实例化对象server调用HTTPServer类 并传进去一个8088(socket服务监听的端口) 
		#并把我们自己写的类传进去        
		print 'welcome to the machine...'        
		#打印欢迎信息        
		print 'ctrl+c quit' #退出方法        
		server.serve_forever() #调用serve_forver方法让程序一直监听8088端口并循环等待用户请求    
	except KeyboardInterrupt:        
		print 'ctrl+c received, shuttingdow server'#如果监听到键盘输入crtl+c就停止程序        
		server.socket.close()
if __name__ == '__main__':    
	main()
