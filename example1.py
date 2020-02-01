#!/home/murtaza/PycharmProjects/BugBox/venv/bin/python

from datetime import datetime
from flask import Flask

myFile = open('/home/murtaza/PycharmProjects/BugBox/append.txt', 'a+')
myFile.write('\nAccessed on ' + str(datetime.now()))

print("hello")