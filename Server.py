from flask import Flask
from flask import jsonify
from flask import request
import sqlite3
from sqlite3 import Error
app = Flask(__name__)
import Functions as functions
___author__='Rivka Eisenstein'

@app.route('/', methods=['GET'])
def Rout():
    return jsonify({'message' : 'try another url'})
@app.route('/GetMessage', methods=['GET'])
def GetMessages():
    if 'application_id' in request.args:
      id = (request.args['application_id'])
      return functions.get('application_id', id)

    elif 'session_id' in request.args:
      id = (request.args['session_id'])

      return functions.get('session_id',id)
    elif 'message_id' in request.args:
      id = (request.args['message_id'])

      return functions.get('message_id',id)
    else:
        rr= jsonify({'message': 'please check the url'})
        rr.status_code = 400
        return rr

@app.route('/AddMessage', methods=['POST'])
def AddMessage():
    try:
        conn = sqlite3.connect(r"C:\Users\Guest123\Music\Messages.db")
        cc = conn.cursor()
    except Error as e:
        print(e)
        response = jsonify({'message': 'cant connect database'})
        response.status_code = 400
        return response
    try:
      aa = request.json
      print(aa)
      if aa !=None:
       a = request.json.get('application_id')
       s = request.json.get('session_id')
       m = request.json.get('message_id')
       p = request.json.get('partipants')
       c = request.json.get('contect')
      else:
          response = jsonify({'message': 'please give a json'})
          response.status_code = 400
          return response
    except Error as e:
        print(e)
        response = jsonify({'message': 'cant connect database'})
        response.status_code = 400
        return response
    #check if the application_id is number
    try:
        if type(a)==int:
         cc.execute('INSERT INTO AllTheMessages VALUES(?,?,?,?,?)', (int(a),s,m,p,c))
        else:
            response = jsonify({'message': 'application_id must be integer'})
            response.status_code = 400
            return response
    except Error as e:
        print(e)
        response = jsonify({'message': 'cant add the new message'})
        response.status_code = 400
        return response
    qq=[]
    #return all the messages with the new message
    for row in cc.execute('SELECT * FROM AllTheMessages '):
        qq.append(row)
    cc.close()
    conn.close()
    rr= jsonify({'data': qq})
    rr.status_code = 201
    return rr

@app.route('/DeleteMessage', methods=['DELETE'])
def deleteMessage():
    if 'application_id' in request.args:
        id = (request.args['application_id'])
        return functions.delete('application_id',id)
    elif 'session_id' in request.args:
        id = (request.args['session_id'])
        return functions.delete('session_id',id)
    elif 'message_id' in request.args:
        id = (request.args['message_id'])
        return functions.delete('message_id',id)
    else:
        return 'please check the url'


if __name__ == "__main__":
    app.run(debug=True)