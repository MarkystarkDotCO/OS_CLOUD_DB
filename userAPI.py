import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<uid>/<upassword>')
def getInput(uid, upassword):
    host = "userdata.postgres.database.azure.com"
    dbname = "userdata"
    user = "max"
    password = "123456789-x"
    sslmode = "require"
    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string) 
    print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    cursor.execute("SELECT * FROM Persons;")
    rows = cursor.fetchall()
    NAME = uid
    print(NAME)
    PASSWORD = upassword
    print(PASSWORD)
    # Print all rows
    for row in rows:
        if str(row[1])==NAME:
            if str(row[2])==PASSWORD:
                valid ={
                "ID":str(row[0]),
                "NAME":str(row[1])
                }
                print(valid)
                return jsonify(valid)
            else:
                err={"ID":"OR",
                "password":"invalid"}
                print("ID or PASSWORD invalid")
                #print(valid)
                return err
            
    #print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
    # Cleanupprint(thisdict) 
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True,port=80, host="0.0.0.0")
