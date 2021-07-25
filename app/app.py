from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'addressData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Address Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, addresses=result)


@app.route('/view/<int:address_id>', methods=['GET'])
def record_view(address_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses WHERE id=%s', address_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', addresses=result[0])


@app.route('/edit/<int:address_id>', methods=['GET'])
def form_edit_get(address_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses WHERE id=%s', address_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', addresses=result[0])


@app.route('/edit/<int:address_id>', methods=['POST'])
def form_update_post(address_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fname'), request.form.get('lname'), request.form.get('address'),
                 request.form.get('city'), request.form.get('state'),
                 request.form.get('zipcode'), address_id)
    sql_update_query = """UPDATE addresses t SET t.fname = %s, t.lname = %s, t.address = %s, t.city = 
    %s, t.state = %s, t.zipcode = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

# hereeeeee
@app.route('/address/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Address Form')

# hereeeeee
@app.route('/address/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fname'), request.form.get('lname'), request.form.get('address'),
                 request.form.get('city'), request.form.get('state'),
                 request.form.get('zipcode'))
    sql_insert_query = """INSERT INTO addresses (fname,lname,address,city,state,zipcode) VALUES (%s, %s,%s, %s,%s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:address_id>', methods=['POST'])
def form_delete_post(address_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM addresses WHERE id = %s """
    cursor.execute(sql_delete_query, address_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/addresses', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/addresses/<int:address_id>', methods=['GET'])
def api_retrieve(address_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses WHERE id=%s', address_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/addresses', methods=['POST'])
def api_add() -> str:
    content = request.json
    cursor = mysql.get_db().cursor()
    inputData = (content['fname'], content['lname'], content['address'],
                 content['city'], content['state'],
                 content['zipcode'])
    sql_insert_query = """INSERT INTO addresses (fname,lname,address,city,state,zipcode) VALUES (%s, %s,%s, %s,%s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/addresses/<int:address_id>', methods=['PUT'])
def api_edit(address_id) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['fname'], content['lname'], content['address'],
                 content['city'], content['state'],
                 content['zipcode'], address_id)
    sql_update_query = """UPDATE addresses t SET t.fname = %s, t.lname = %s, t.address = %s, t.city = 
       %s, t.state = %s, t.zipcode = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/addresses/<int:address_id>', methods=['DELETE'])
def api_delete(address_id) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM addresses WHERE id = %s """
    cursor.execute(sql_delete_query, address_id)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
