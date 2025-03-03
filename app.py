from flask import Flask,request,jsonify
from database import Database
from bson import json_util, ObjectId

app = Flask(__name__)
DataBase = Database()
print("serverrunnning")
@app.route("/", methods=["GET"])
def start():
    if request.method == 'GET':
        a = DataBase.getAllUser()
        return (json_util.dumps("server running"))
   
@app.route("/users", methods=["GET","POST"])
def users():
    if request.method == 'GET':
        a = DataBase.getAllUser()
        return (json_util.dumps(list(a)))
    if request.method == 'POST':
        data = json_util.loads(request.get_data())['data']
        res = DataBase.addUser(data)
        return(json_util.dumps(res))

@app.route("/users/<user_id>" ,methods=["GET","PUT","DELETE"])
def UsersByID(user_id):
    if request.method == 'GET':
        res = DataBase.getUserByID(user_id)
        return (json_util.dumps(res))
    elif request.method == 'PUT':
        data = json_util.loads(request.get_data())['data']
        res = DataBase.updateById(user_id,data)
        return(json_util.dumps(res))
    elif request.method == 'DELETE':
        res = DataBase.deleteUserById(user_id)
        return (json_util.dumps(res))
        


if __name__ == '__main__':
    app.run(debug=True,port=int("4000"))