from flask import current_app as app, request, jsonify
import sys
import ast

#from flask_cors import CORS
from .algorithms import dijkstra
#CORS(app)

@app.route('/solve',methods=['POST'])
def add_user():
    adj=ast.literal_eval(request.form['adj'])
    cost=ast.literal_eval(request.form['cost'])
    s = int(request.form['s'])
    t = int(request.form['t'])
    response = dijkstra.find_distance(adj, cost, s, t)
    print(response)
    return jsonify(response)

@app.route('/user/<email>',methods=['DELETE'])
def delete_user(email):
    response={'status':'succesful','message':'user deleted sucessfully'}
    return jsonify(response)

@app.route('/users',methods=['GET'])
def get_users():
    response = {'users':"Aanu",'status':'successful'}
    return jsonify (response)