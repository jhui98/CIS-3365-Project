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
    itemInfo = execute_query(conn, query) # execute query in DB
    print(itemInfo)

@app.route('/api/item', methods=['GET']) # get a single user by id
def get_item_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM item ORDER BY ItemName" 
    itemInfo = execute_query(conn, query) # execute query in DB
    print(itemInfo)

@app.route('/api/brand', methods=['GET']) # get a single user by id
def get_brand_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM brand ORDER BY BrandName" 
    brandInfo = execute_query(conn, query) # execute query in DB
    print(brandInfo)

@app.route('/api/department', methods=['GET']) # get a single user by id
def get_department_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM department ORDER BY DeptName" 
    deptInfo = execute_query(conn, query) # execute query in DB
    print(deptInfo)

@app.route('/api/reseller', methods=['GET']) # get a single user by id
def get_reseller_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM reseller ORDER BY ResellerName" 
    resellerInfo = execute_query(conn, query) # execute query in DB
    print(resellerInfo)

@app.route('/api/distributor', methods=['GET']) # get a single user by id
def get_distributor_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM distributor ORDER BY DistributorName" 
    distributorInfo = execute_query(conn, query) # execute query in DB
    print(distributorInfo)

@app.route('/api/employee', methods=['GET']) # get a single user by id
def get_employee_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM employee ORDER BY EmpName" 
    employeeInfo = execute_query(conn, query) # execute query in DB
    print(employeeInfo)

@app.route('/api/emprole', methods=['GET']) # get a single user by id
def get_emprole_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM employeerole ORDER BY RoleName" 
    emproleInfo = execute_query(conn, query) # execute query in DB
    print(emproleInfo)

@app.route('/api/customer', methods=['GET']) # get a single user by id
def get_customer_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM customer ORDER BY customerLoytalty" 
    emproleInfo = execute_query(conn, query) # execute query in DB
    print(emproleInfo)

@app.route('/api/custLoyalty', methods=['GET']) # get a single user by id
def get_custLoyalty_info():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = "SELECT * FROM custLoyalty ORDER BY LoyaltyID" 
    emproleInfo = execute_query(conn, query) # execute query in DB
    print(emproleInfo)
# -- whole table pulls --


# --insert statements

@app.route('/api/brand', methods = ['POST'])
def api_brand_post():
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
def api_loyalty_post():
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
def api_customer_post():
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
def api_department_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    name = request_data['name']

    # query to insert to table
    query = "INSERT INTO department (DeptName) VALUES ('%s')" % (name)
    execute_query(conn, query)
    return 'Add request successful'

@app.route('/api/distributor', methods = ['POST'])
def api_distributor_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    name = request_data['distributorname']

    # query to insert to table
    query = "INSERT INTO distributor (DistributorName) VALUES ('%s')" % (name)
    execute_query(conn, query)
    return 'Add request successful'

@app.route('/api/employee', methods = ['POST'])
def api_employee_post():
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
def api_emprole_post():
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
def api_item_post():
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
    query = "INSERT INTO item (ItemName, BrandID, DeptID, ItemPrice, ItemRevenue, ResellerID) VALUES ('%s', %s, %s, %s, %s, %s)" % (name, brandid, deptid, price, revenue, resellerid)
    execute_query(conn, query)
    return 'Add request successful'

@app.route('/api/reseller', methods = ['POST'])
def api_reseller_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    name = request_data['name']
    email = request_data['email']
    disid = request_data['disid']

    # query to insert to table
    query = "INSERT INTO reseller (ResellerName, ResellerEmail, DistributorID) VALUES ('%s', '%s', %s)" % (name, email, disid)
    execute_query(conn, query)
    return 'Add request successful'    

@app.route('/api/transaction', methods = ['POST'])
def api_transaction_post():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # stores all columns except for id
    transnum = request_data['transnum']
    itemid = request_data['itemid']
    date = request_data['date']
    cusid = request_data['cusid']

    # query to insert to table
    query = "INSERT INTO transaction (TransNum, ItemID, date, CusID) VALUES (%s, %s, '%s', %s)" % (transnum, itemid, date, cusid)
    execute_query(conn, query)
    return 'Add request successful'

# --insert statements

# --update statements

@app.route('/api/brand', methods = ['PUT'])
def api_brand_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE brand SET %s = '%s' WHERE BrandID = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'

@app.route('/api/custLoyalty', methods = ['PUT'])
def api_loyalty_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE custLoyalty SET %s = '%s' WHERE LoyaltyID = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'

@app.route('/api/customer', methods = ['PUT'])
def api_customer_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE customer SET %s = '%s' WHERE CustID = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'
    
@app.route('/api/department', methods = ['PUT'])
def api_department_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE department SET %s = '%s' WHERE DeptID = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'

@app.route('/api/distributor', methods = ['PUT'])
def api_distributor_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE distributor SET %s = '%s' WHERE DistributorID = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'


@app.route('/api/employee', methods = ['PUT'])
def api_employee_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE employee SET %s = '%s' WHERE EmpID = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'

@app.route('/api/emprole', methods = ['PUT'])
def api_emprole_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE employeeRole SET %s = '%s' WHERE ID = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'
    
@app.route('/api/item', methods = ['PUT'])
def api_item_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE item SET %s = '%s' WHERE ItemID = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'

@app.route('/api/reseller', methods = ['PUT'])
def api_reseller_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE reseller SET %s = '%s' WHERE ResellerID = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'

@app.route('/api/transaction', methods = ['PUT'])
def api_transaction_put():
    conn = create_connection('cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com', 'admin', 'rq8s9Sk5VZfHF2C', 'cis3365spring22')
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = "UPDATE transaction SET %s = '%s' WHERE id = %s" % (key, val, idToUpdate)
        execute_query(conn, query)
    return 'Put request successful'

# -- update statements -- 


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
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM department WHERE DeptID = {id}" # delete where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"

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
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM distributor WHERE DistributorID = {id}" # delete where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"

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
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM employeeRole WHERE roleID = {id}" # delete where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"

@app.route('/api/employeeDelete', methods=['DELETE']) # get a single user by id
def delete_employee():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM employee WHERE EmpID = {id}" # delete where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"

@app.route('/api/deletecustLoyalty', methods=['DELETE']) # get a single user by id
def delete_custLoyalty():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM custLoyalty WHERE LoyaltyID = {id}" # delete where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"

@app.route('/api/deletetransac', methods=['DELETE']) # get a single user by id
def delete_transac():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    if 'id' in request.args: # check for id in request arguments
        id = request.args['id'] # save id to local var

        # query string
        query = f"DELETE FROM transac WHERE id = {id}" # where id 
        execute_query(conn, query) # execute query in DB

        return "DELETE REQUEST SUCESSFUL"
    return "ERROR NO ID PROVIDED"
# -- delete methods --

# -- reports --
@app.route('/api/itemsSoldByDistributor', methods=['GET']) # Jacob Hui
def itemsSoldByDistributor():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = """SELECT
            distributor.DistributorName AS 'Distributor',
            brand.BrandName AS 'Brand',
            item.ItemName AS 'Item Name',
            item.ItemPrice AS 'Item Cost',
            item.ItemRevenue AS 'Selling Price',
            item.ItemProfit AS 'Profit'
            FROM item
            Join brand ON item.BrandID = brand.BrandID
            Join reseller ON brand.BrandReseller = reseller.ResellerID
            Join distributor ON reseller.DistributorID = distributor.DistributorID;"""
    execute_query(conn, query) # execute query in DB

@app.route('/api/LowProfitItems', methods=['GET']) # Jacob Hui
def LowProfitItems():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = """SELECT
            brand.BrandName AS 'Brand',
            item.ItemName AS 'Item Name',
            item.ItemProfit AS 'Profit',
            item.ItemPrice AS 'Item Cost',
            item.ItemRevenue AS 'Selling Price',
            reseller.ResellerName AS 'Reseller',
            reseller.ResellerEmail AS 'Email',
            distributor.DistributorName AS 'Distributor'
            FROM item
            Join brand ON item.BrandID = brand.BrandID
            Join reseller ON brand.BrandReseller = reseller.ResellerID
            Join distributor ON reseller.DistributorID = distributor.DistributorID
            WHERE item.ItemProfit < 10
            ORDER BY item.ItemProfit ASC;"""
    execute_query(conn, query) # execute query in DB


@app.route('/api/ItemsSoldByReseller', methods=['GET']) # Zachary Arroyo
def ItemsSoldByReseller():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")
    request_data = request.get_json()

    # id for row needed to update is stored and will remain the same, but the id key from request_data is popped for next step    
    idToUpdate = request_data['id']
    request_data.pop('id')

    # for loop that repeats for each and every key in request_data, which no longer has the ID key. this allows every change wanted to be processed in one request.
    for key in request_data.keys():
        val = request_data[key]
        # key and val variables change with each for loop step
        query = f"""SELECT
            reseller.ResellerName AS 'Reseller',
            distributor.DistributorName AS 'Distributor',
            item.ItemName AS 'Product',
            brand.BrandName AS 'Brand',
            department.DeptName AS 'Department',
            item.ItemPrice AS 'Buying Price',
            item.ItemRevenue AS 'Selling Price',
            item.ItemProfit AS 'Profit'
            FROM item
            Join brand ON item.BrandID = brand.BrandID
            Join department ON item.DeptID = department.DeptID
            Join reseller ON brand.BrandReseller = reseller.ResellerID
            Join distributor ON reseller.DistributorID = distributor.DistributorID
            WHERE reseller.{key} = '{val}'"""
        execute_query(conn, query)
    return 'request successful'

@app.route('/api/ItemsSoldWithinAWeek', methods=['GET']) # Zachary Arroyo
def ItemsSoldWithinAWeek():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = """SELECT
            transac.TransNum As 'Transaction #',
            transac.date As 'Date',
            item.itemID AS 'Item ID',
            item.ItemName AS 'Product',
            brand.BrandName AS 'Brand',
            department.DeptName AS 'Department',
            item.ItemPrice AS 'Buying Price',
            item.ItemRevenue AS 'Selling Price',
            item.ItemProfit AS 'Profit'
            FROM transac
            Join item ON transac.ItemID = item.ItemID
            Join brand ON item.BrandID = brand.BrandID
            Join department ON item.DeptID = department.DeptID
            WHERE DATE BETWEEN DATEADD(DAY, -7, CURRENT_TIMESTAMP) AND CURRENT_TIMESTAMP
            ORDER BY transac.date DESC"""
    execute_query(conn, query) # execute query in DB

@app.route('/api/MostProfit', methods=['GET']) # Adedeji Akingbola
def MostProfit():
    #  establish databse connection
    conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

    # query string
    query = """SELECT
            transac.date As 'Date',
            item.itemID AS 'Item ID',
            item.ItemName AS 'Product',
            brand.BrandName AS 'Brand',
            department.DeptName AS 'Department',
            item.ItemProfit AS 'Profit'
            FROM transac
            Join item ON transac.ItemID = item.ItemID
            Join brand ON item.BrandID = brand.BrandID
            Join department ON item.DeptID = department.DeptID
            ORDER BY item.ItemProfit DESC"""
    execute_query(conn, query) # execute query in DB

# @app.route('/api/', methods=['GET']) # Zachary Arroyo
# def ():
#     #  establish databse connection
#     conn = create_connection("cis3368.cwakmughsmpu.us-east-2.rds.amazonaws.com", "admin", "rq8s9Sk5VZfHF2C", "cis3365spring22")

#     # query string
#     query = """"""
#     execute_query(conn, query) # execute query in DB

# -- reports --



app.run()