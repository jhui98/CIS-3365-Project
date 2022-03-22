# Jacob Hui - 1664245
# CIS 3368 - 16242 - Dobretsberger
# Final Project Methods - Fall 2021

from sql import create_connection
from sql import execute_query
from sql import execute_read_query

def count_user_restaurants(userid, connection): 
    """Takes input userid and connection; counts amount of appearances in restaurants table, returns int"""
    # query string # count from https://www.mysqltutorial.org/mysql-find-duplicate-values/
    query = "SELECT COUNT(*) FROM restaurants WHERE userid = '%s'" % (userid) # determines count for current user in table

    count = execute_read_query(connection, query) # execute query in DB
    num = int(count[0]["COUNT(*)"])
    return num