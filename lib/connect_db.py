# coding:utf-8
import psycopg2
from configparser import ConfigParser
config = ConfigParser()
#config.read('~/Desktop/work/Flask/api_server/ini/config.ini')
config.read('../ini/config.ini')


connection = psycopg2.connect("host=localhost port=5432 dbname=test user=postgres password=postgres")

cur = connection.cursor()

cur.execute("select * from test")
for row  in cur:
     title = row[1]
    
cur.close()

print title
