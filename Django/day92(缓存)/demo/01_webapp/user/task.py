import time
from celery import task

@task
def hello_world():
    print('hello')
    time.sleep(10)
    print('world')
