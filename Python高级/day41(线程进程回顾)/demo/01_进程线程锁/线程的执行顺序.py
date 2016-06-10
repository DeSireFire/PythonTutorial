import  threading
import time

class a(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I am"+self.name+" @ "+str(i)
            print(msg)
def test():
    for i in range(8):
        t = a()
        t.start()

if __name__ == '__main__':
    test()