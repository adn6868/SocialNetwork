from flask import Flask, render_template , g 
from flask_restful import Resource, Api, reqparse
import markdown
import os
import shelve

# api = Api(app)
def getDB():
    db = getattr(g, '_database',None)
    if db is None:
        db = g._database = shelve.open("users.db")
    return db

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/googleSignin')
def googleSignin():
    return render_template('googleSignin.html')


@app.route('/facebookSignin')
def facebookSignin():
    return render_template('facebookSignin.html')


@app.route('/blogs')
def blogs():
    return render_template('blogs.html', blogs=blogs)

@app.teardown_appcontext
def teardownDB(exception):
    db = getattr(g, '_databse',None)
    if db is not None:
        db.close()
    pass
class UserList(Resource):
    def get(self):
        shelf = getDB()
        keys = list(shelf.keys())

        usersList = []
        for key in keys:
            usersList.append(shelf[key])
        return {'message' : '200', 'data':usersList}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required = True)
        parser.add_argument('name', required = True)
        parser.add_argument('email', required = True)
        parser.add_argument('phoneNumber', required = True)
        parser.add_argument('employment', required = True)

        args = parser.parse_args()

        shelf = getDB()
        shelf[args['identifier']] = args

        return {'message': 'New User added', 'data': args}, 201

class User(Resource):
    def get(self, id):
        shelf = getDB()

        if not (id in shelf):
            return {'message': 'User not found', 'data': {}}, 404
        return {'message': 'User found', 'data': shelf[id]}, 200

    def delete(self, id):
        shelf = getDB()

        if not (id in shelf):
            return {'message': 'User not found', 'data': {}}, 404

        del shelf[id]
        return '', 204

api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<string:identifier>')
