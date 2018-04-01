import datetime
import MySQLdb
from os.path import curdir
import json


def updateDevice(name=None, status=None):
    # Open database connection
    db = MySQLdb.connect("192.168.0.17", "ha", "password", "nanihome")
    name = 'Mohan'
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "select * from devices where name like '%" + str(name) + "%'"
    try:
        # Execute the SQL command
        print(sql)
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row[0], " ", row[1])

        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def toggel_state(device_name = None):
    try:
        db = MySQLdb.connect("192.168.0.17", "ha", "password", "nanihome")
        cursor = db.cursor()
        sql = "select status from devices where name like '%" + str(device_name) + "%'"
        print(sql)
        cursor.execute(sql)
        device_status = None
        for row in cursor.fetchall():
            device_status = json.loads(row[0])

        curr_state = device_status.get("state", None)
        new_state = "on"

        if("on" in curr_state):
            device_status['state'] = "off"
        else:
            device_status['state'] = "on"
        update_sql = """UPDATE devices SET status=%s WHERE name=%s""", (json.dumps(device_status), device_name)

        print(update_sql)
        cursor.execute( """UPDATE devices SET status=%s WHERE name=%s""", (json.dumps(device_status), device_name))
        db.commit()
        db.close()
    except:
        print("ERROR UPDATING THE STATE OF " + device_name)