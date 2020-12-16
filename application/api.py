from flask import current_app as app, request, jsonify
import sys
import ast

#from flask_cors import CORS
from .algorithms import dijkstra, a_star
#CORS(app)

@app.route('/solve/<algo>',methods=['POST'])
def solve(algo):
    if not all([(val in request.form) for val in ['adj', 'cost', 's', 't']]):
        return jsonify("Incomplete Parameters")
    adj = ast.literal_eval(request.form['adj'])
    cost = ast.literal_eval(request.form['cost'])
    s = int(request.form['s'])
    t = int(request.form['t'])
    if algo == 'dijkstra':
        response = solve_dijstra(adj, cost, s, t)    
    elif algo == 'a_star':
        if not all([(val in request.form) for val in ['x_coord', 'y_coord']]):
            return jsonify("Incomplete Parameters for A-Star Algorithm")
        x = ast.literal_eval(request.form['x_coord'])
        y = ast.literal_eval(request.form['y_coord'])
        response = solve_Astar(adj, cost, x, y, s, t)
    return jsonify(response)

@app.route('/user/<email>',methods=['DELETE'])
def delete_user(email):
    response={'status':'succesful','message':'user deleted sucessfully'}
    return jsonify(response)

@app.route('/users',methods=['GET'])
def get_users():
    response = {'users':"Aanu",'status':'successful'}
    return jsonify (response)

def solve_dijstra(adj, cost, s, t):
    return dijkstra.find_distance(adj, cost, s, t)

def solve_Astar(adj, cost, x, y, s, t):
    graph = a_star.AStar(len(x), adj, cost, x, y)
    return graph.query(s, t)