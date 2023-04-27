""" This is the module with all the mysql stuff """

import pymysql

DATABASE = pymysql.connect("localhost", "testuser", "testpassword", "testscheme")
