#https://ianlondon.github.io/blog/deploy-flask-docker-nginx
import psycopg2
from flask import Flask, jsonify

print(555)
app = Flask(__name__)


#ดูลิสต์สินค้าทั้งหมด
@app.route('/<code>')
def getInput(code):
    host = "productdata.postgres.database.azure.com"
    dbname = "productdata"
    user = "min"
    password = "123456789-x"
    sslmode = "require"
    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string) 
    print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    cursor.execute("SELECT * FROM Products;")
    rows = cursor.fetchall()
    NAME = code
    print(NAME)
    # Print all rows
    for row in rows:
        if str(row[0])==NAME:
                valid ={
                "code":str(row[0]),
                "NAME":str(row[1]),
                "qty":str(row[2]),
                "price":str(row[3])
                }
                print(valid)
                return jsonify(valid)
    return "not found data"
    #print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
    # Cleanupprint(thisdict) 
    conn.commit()
    cursor.close()
    conn.close()

#ตัดสต็อค
@app.route('/updateprice/<code>/<volume>')
def updatePrice(code,volume):
    host = "productdata.postgres.database.azure.com"
    dbname = "productdata"
    user = "min"
    password = "123456789-x"
    sslmode = "require"
    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string) 
    print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    cursor.execute("SELECT * FROM Products;")
    rows = cursor.fetchall()
    NAME = code
    volume = int(volume)
    # Print all rows
    for row in rows:
        if str(row[0])==NAME:
            qty =int(row[2])
            qty = qty-volume
            if qty<0:
                return "out of stock"
            #cursor.execute("SELECT * FROM Products;")
        
            cursor.execute("UPDATE Products SET qty = "+"'"+str(qty)+"'"+"WHERE code = "+"'"+str(row[0]+"'"))
            conn.commit()
            cursor.close()
            conn.close()
            return str(row[2])
    return "not found data"
    #print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
    # Cleanupprint(thisdict) 
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    #app.run(debug=True,host="0.0.0.0", port=80)
    app.run(debug=True)
