import os

'''
os.mkdir(r'C:\Users\Administrator\Desktop\老王')
'''

'''
os.chdir(r'C:\Users\Administrator\Desktop')
os.mkdir('老王')
'''

'''
os.chdir(r'C:\Users\Administrator\Desktop')
os.makedirs(r'a\b')
'''

'''
print(os.getcwd())
'''

'''
os.listdir('./')
'''

'''
os.chdir(r'C:\Users\Administrator\Desktop')
os.rmdir('abc')
'''

import shutil

shutil.rmtree('abc')