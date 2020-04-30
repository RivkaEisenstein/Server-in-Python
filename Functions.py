import sqlite3
from sqlite3 import Error
from flask import jsonify, app
___author__='Rivka Eisenstein'


def get(item1,item2):
    #try connect to the database
    try:
     conn = sqlite3.connect(r"C:\Users\Guest123\Music\Messages.db")
     cc = conn.cursor()
    except Error as e:
        print(e)
        response = jsonify("Error")
        response.status_code = 400
        return response
    try:
        qq = []
        if item1=='application_id':
          for row in cc.execute("SELECT * FROM AllTheMessages WHERE application_id = '%s'" % item2):
             qq.append(row)
          rr = jsonify({'data': qq})
        elif item1=='session_id':
          for row in cc.execute("SELECT * FROM AllTheMessages WHERE session_id = '%s'" % item2):
             qq.append(row)
          rr = jsonify({'data': qq})
        elif item1 == 'message_id':
          jsonn={}
          for row in cc.execute("SELECT * FROM AllTheMessages WHERE message_id = '%s'" % item2):
                 jsonn=row
          rr = jsonify({'data': jsonn})
        rr.status_code = 201
        return rr
    # return error if the url was wrong
    except Error as e:
        print(e)
        response = jsonify({'Error': 'Dont found items'})
        response.status_code = 400
        return response
    finally:
        if conn:
            conn.close()
def delete(item1,item2):
    #try connect to the database
    try:
      conn = sqlite3.connect(r"C:\Users\Guest123\Music\Messages.db")
      cc = conn.cursor()
    except Error as e:
        print(e)
        response = jsonify({'message': 'cant connect database'})
        response.status_code = 400
        return response
    try:
        qq = []
        if item1 == 'application_id':
            #check if have items to delete
            for row in cc.execute("SELECT * FROM AllTheMessages WHERE application_id = '%s'" % item2):
                qq.append(row)
            print(qq)
            if qq   != []:
                cc.execute("DELETE FROM AllTheMessages WHERE application_id = '%s'" % item2)
            else:
                response = jsonify({'message': 'dont have items to delete'})
                response.status_code = 400
                return response

        qq = []
        if item1 == 'session_id':
            # check if have items to delete
            for row in cc.execute("SELECT * FROM AllTheMessages WHERE session_id = '%s'" % item2):
                qq.append(row)
            print(qq)
            if qq != []:
                cc.execute("DELETE FROM AllTheMessages WHERE session_id = '%s'" % item2)
            else:
             response = jsonify({'message': 'dont have items to delete'})
             response.status_code = 400
             return response

        qq = []
        if item1 == 'message_id':
            # check if have items to delete
            for row in cc.execute("SELECT * FROM AllTheMessages WHERE message_id = '%s'" % item2):
                qq.append(row)
            if qq == []:
                response = jsonify({'message': 'dont have items to delete'})
                response.status_code = 400
                return response
            else:
             cc.execute("DELETE FROM AllTheMessages WHERE message_id = '%s'" % item2)
        bb=[]
        for row in cc.execute("SELECT * FROM AllTheMessages"):
            bb.append(row)
        rr=jsonify('data after delete',bb)
        rr.status_code=200
        return rr

    except Error as e:
        print(e)
        response = jsonify({'Error': 'not found'})
        response.status_code = 400
        return response
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
      app.run()