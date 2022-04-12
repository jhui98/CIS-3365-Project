# Jacob Hui - 1664245
# CIS 3365 - 192925 - Amirpanahi
# Final Project - API - Fall 2021are u 

import flask
from flask import jsonify
from flask import request, make_response
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

# setting up an application name
app = flask.Flask(__name__) #  sets up the application
app.config["DEBUG"] = True # allow to show errors in browser

@app.route('/', methods=['GET']) # goes home and determine if server exists
def home():
    return "<h1> Welcome our CIS 3365 Project API!</h1>"

# -- whole table pulls --
@app.route('/api/transaction', methods=['GET']) # get a single user by id
def get_transaction_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM transaction ORDER BY TransNum" 
    itemInfo = execute_read_query(conn, query) # execute query in DB
    print(itemInfo)

    return jsonify(itemInfo)

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

@app.route('/api/customer', methods=['GET']) # get a single user by id
def get_customer_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM customer ORDER BY customerLoytalty" 
    emproleInfo = execute_read_query(conn, query) # execute query in DB
    print(emproleInfo)

    return jsonify(emproleInfo)

@app.route('/api/custLoyalty', methods=['GET']) # get a single user by id
def get_custLoyalty_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM custLoyalty ORDER BY LoyaltyID" 
    emproleInfo = execute_read_query(conn, query) # execute query in DB
    print(emproleInfo)

    return jsonify(emproleInfo)
# -- whole table pulls --

# --insert statements

@app.route('/api/brand', methods = ['POST'])
def api_animal_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    brandname = request_data['brandname']
    resellerid = request_data['resellerid']

    # query to insert to table
    query = "INSERT INTO brand (BrandName, BrandReseller) VALUES ('%s', %s)" % (brandname, resellerid)
    execute_query(conn, query)
    return 'Add request successful'

@app.route('/api/custLoyalty', methods = ['POST'])
def api_animal_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    loyaltyname = request_data['loyaltyname']
    discountp = request_data['discountp']

    # query to insert to table
    query = "INSERT INTO custLoyalty (LoyaltyName, DiscountP) VALUES ('%s', %s)" % (loyaltyname, discountp)
    execute_query(conn, query)
    return 'Add request successful'

@app.route('/api/customer', methods = ['POST'])
def api_animal_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    name = request_data['name']
    loyalty = request_data['loyalty']
    email = request_data['email']
    phone = request_data['phone']
    address = request_data['address']
    city = request_data['city']
    state = request_data['state']
    zip = request_data['zip']

    # query to insert to table
    query = "INSERT INTO customer (CustName, customerLoyalty, CustEmail, CustPhone, CustAddress, CustCity, CustState, CustZip) VALUES ('%s', %s, '%s', '%s', '%s', '%s', '%s', %s)" % (name, loyalty, email, phone, address, city, state, zip)
    execute_query(conn, query)
    return 'Add request successful'
    
@app.route('/api/department', methods = ['POST'])
def api_animal_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    name = request_data['name']

    # query to insert to table
    query = "INSERT INTO department (DeptName) VALUES ('%s')" % (name)
    execute_query(conn, query)
    return 'Add request successful'

@app.route('/api/distributor', methods = ['POST'])
def api_animal_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    name = request_data['distributorname']

    # query to insert to table
    query = "INSERT INTO distributor (DistributorName) VALUES ('%s')" % (name)
    execute_query(conn, query)
    return 'Add request successful'

@app.route('/api/employee', methods = ['POST'])
def api_animal_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    active = request_data['active']
    name = request_data['name']
    email = request_data['email']
    phone = request_data['phone']
    address = request_data['address']
    city = request_data['city']
    state = request_data['state']
    zip = request_data['zip']

    # query to insert to table
    query = "INSERT INTO employee (ActiveEmp, EmpName, EmpEmail, EmpPhone, EmpAddress, EmpCity, EmpState, EmpZip) VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', %s)" % (active, name, email, phone, address, city, state, zip)
    execute_query(conn, query)
    return 'Add request successful'

@app.route('/api/emprole', methods = ['POST'])
def api_animal_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    roleid = request_data['roleid']
    rolename = request_data['rolename']
    empid = request_data['empid']


    # query to insert to table
    query = "INSERT INTO employeeRole (RoleID, RoleName, EmpID) VALUES (%s, '%s', %s)" % (roleid, rolename, empid)
    execute_query(conn, query)
    return 'Add request successful'
    
@app.route('/api/item', methods = ['POST'])
def api_animal_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    name = request_data['name']
    brandid = request_data['brandid']
    deptid = request_data['deptid']
    price = request_data['price']
    revenue = request_data['revenue']
    resellerid = request_data['resellerid']

    # query to insert to table
    query = "INSERT INTO item (ItemName, BrandID, DeptID, ItemPrice, ItemRevenue, ItemProfit, ResellerID) VALUES ('%s', %s, %s, %s, %s, %s)" % (name, brandid, deptid, price, revenue, resellerid)
    execute_query(conn, query)
    return 'Add request successful'

@app.route('/api/transaction', methods = ['POST'])
def api_animal_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    transnum = request_data['transnum']
    itemid = request_data['itemid']
    date = request_data['date']
    cusid = request_data['cusid']

    # query to insert to table
    query = "INSERT INTO transaction (TransNum, ItemID, date, CusID) VALUES (%s, %s, '%s', %s)" % (transnum, itemid, date,)
    execute_query(conn, query)
    return 'Add request successful'

# --insert statements


# -- delete statements --
@app.route('/api/deleteItem', methods=['DELETE']) # get a single user by id
def delete_item():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM item WHERE ItemID = {id}" # delete where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"

@app.route('/api/deleteBrand', methods=['DELETE']) # get a single user by id
def delete_brand():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM brand WHERE BrandID = {id}" # delete where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"

@app.route('/api/deleteDepartment', methods=['DELETE']) # get a single user by id
def delete_department():
    # TODO: department delete
    pass

@app.route('/api/deleteReseller', methods=['DELETE']) # get a single user by id
def delete_reseller():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM reseller WHERE ResellerID = {id}" # delete where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"

@app.route('/api/deleteDistrubutor', methods=['DELETE']) # get a single user by id
def delete_distributor():
    # TODO: distributor delete
    pass

@app.route('/api/deleteCustomer', methods=['DELETE']) # get a single user by id
def delete_customer():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM customer WHERE CustID = {id}" # delete where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"



@app.route('/api/deleteEmpRole', methods=['DELETE']) # get a single user by id
def delete_emprole():
    # TODO: emprole delete
    pass

# TODO: customer delete
# TODO:  custLoyalty delete
# TODO:  transaction delete

# -- delete methods --




app.run()