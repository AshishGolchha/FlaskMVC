from User import User
from flask import jsonify, request, render_template
from database import db

class UserController:
    def index():
        return render_template('users/index.html',users =User.query.all())
        # return jsonify([i.getData() for i in User.query.all()])

    def create():
        return "This is users create"

    def store():
        User().create(request.json)
        return jsonify({'Message':f'User has been created'})


    def show(id):
        return jsonify(User.query.get(id))

    def edit(id):
        return jsonify(User.query.get(id))

    def update(id):
        User.query.get(id).update(request.json)
        return jsonify({'Message':f'User has been updated with id {id}'})
    
    def delete(id):
        User.query.get(id).delete()
        return jsonify({'Message':f'User has been deleted with id {id}'})
