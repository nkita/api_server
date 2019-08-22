# Overview
 This Repository is REST API using flask.
 
 CentOS + Apache + WSGI + Python(flask) + postgreSQL
 
# Installation
1. OS	

	CentOS 7
2. yum 
	```
	yum -y install httpd mod_wsgi
	yum -y install epel-release
	yum -y install git
	yum -y install python36 python36-pip
	wget https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
	rpm -ivh pgdg-centos96-9.6-3.noarch.rpm
	yum -y install postgresql96-server postgresql96-devel postgresql96-contrib
	```
	
3. pip install
	```
	pip3.6 install flask flask_cors peewee psycopg2 psycopg2-binary configparser
	```
	
