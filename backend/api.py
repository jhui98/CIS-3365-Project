# Jacob Hui - 1664245
# CIS 3368 - 16242 - Dobretsberger
# Final Project - API - Fall 2021

import flask
from flask import jsonify
from flask import request, make_response
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

# setting up an application name
app = flask.Flask(__name__) #  sets up the application
app.config["DEBUG"] = True # allow to show errors in browser

# -- whole table pulls --
@app.route('/', methods=['GET']) # goes home and determine if server exists
def home():
    return "<h1> Welcome our CIS 3365 Project API!</h1>"

@app.route('/api/item', methods=['GET']) # get a single user by id
def get_item_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM item ORDER BY ItemName" 
    itemInfo = execute_read_query(conn, query) # execute query in DB
    print(itemInfo)

    return jsonify(itemInfo)

@app.route('/api/brand', methods=['GET']) # get a single user by id
def get_brand_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM brand ORDER BY BrandName" 
    brandInfo = execute_read_query(conn, query) # execute query in DB
    print(brandInfo)

    return jsonify(brandInfo)

@app.route('/api/department', methods=['GET']) # get a single user by id
def get_department_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM department ORDER BY DeptName" 
    deptInfo = execute_read_query(conn, query) # execute query in DB
    print(deptInfo)

    return jsonify(deptInfo)

@app.route('/api/reseller', methods=['GET']) # get a single user by id
def get_reseller_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM reseller ORDER BY ResellerName" 
    resellerInfo = execute_read_query(conn, query) # execute query in DB
    print(resellerInfo)

    return jsonify(resellerInfo)

@app.route('/api/distributor', methods=['GET']) # get a single user by id
def get_distributor_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM distributor ORDER BY DistributorName" 
    distributorInfo = execute_read_query(conn, query) # execute query in DB
    print(distributorInfo)

    return jsonify(distributorInfo)

@app.route('/api/customer', methods=['GET']) # get a single user by id
def get_customer_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM customer ORDER BY CustName" 
    customerInfo = execute_read_query(conn, query) # execute query in DB
    print(customerInfo)

    return jsonify(customerInfo)

@app.route('/api/employee', methods=['GET']) # get a single user by id
def get_employee_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM employee ORDER BY EmpName" 
    employeeInfo = execute_read_query(conn, query) # execute query in DB
    print(employeeInfo)

    return jsonify(employeeInfo)

@app.route('/api/emprole', methods=['GET']) # get a single user by id
def get_emprole_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM employeerole ORDER BY RoleName" 
    emproleInfo = execute_read_query(conn, query) # execute query in DB
    print(emproleInfo)

    return jsonify(emproleInfo)
# -- whole table pulls --




app.run()