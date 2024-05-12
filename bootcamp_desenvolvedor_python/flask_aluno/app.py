from flask import Flask, render_template, send_from_directory
from flask import Response, request
from flask import jsonify
from flask_migrate import Migrate
from config import DevelopmentConfig
from models.user import db, User

import json

app = Flask(__name__, static_folder='public')
# app = Flask(__name__)
app.config.from_object(DevelopmentConfig())
db.init_app(app)
migrate = Migrate(app, db) #que disponibiliza o serviço de migração.


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/create')
def create():
    return send_from_directory(app.static_folder, 'create.html')

@app.route('/update')
def update():
    return send_from_directory(app.static_folder, 'update.html')

@app.route('/view')
def view():
    return send_from_directory(app.static_folder, 'user.html')

@app.route('/edit')
def edit():
    return send_from_directory(app.static_folder, 'update.html')


# @app.route('/users', methods=['GET'])
# def list_users():
#     users = User.query.all()
#     user_list = [{'id': user.id, 'name': user.name, 'phone': user.phone, 'address': user.address, 'cpf': user.cpf} for user in users]
#     return jsonify(user_list)

@app.route('/users', methods=['GET'])
def list_users():
    session = db.session()
    users = session.query(User).all()
    users_json = [user.serialize() for user in users]
    session.close()
    return Response(json.dumps(users_json))

# @app.route('/user', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     new_user = User(name=data['name'], phone=data['phone'], address=data['address'], cpf=data['cpf'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'id': new_user.id}), 201


# @app.route('/user/create', methods=['POST'])
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    session = db.session()
    try:
        user = User(name=data['name'], phone=data['phone'], address=data['address'], cpf=data['cpf'])
        session.add(user)
        session.commit()
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        print(e)
        session.rollback()
        return {"erro":"não conseguimos gravar o usuário"}
    finally:
        session.close()

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {'id': user.id, 'name': user.name, 'phone': user.phone, 'address': user.address, 'cpf': user.cpf}
        return jsonify(user_data)
    return jsonify({'error': 'User not found'}), 404

# @app.route('/user/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     user = User.query.get(user_id)
#     if user:
#         data = request.get_json()
#         user.name = data.get('name', user.name)
#         user.phone = data.get('phone', user.phone)
#         user.address = data.get('address', user.address)
#         user.cpf = data.get('cpf', user.cpf)
#         db.session.commit()
#         return jsonify({'message': 'User updated successfully'})
#     return jsonify({'error': 'User not found'}), 404

# @app.route('/user/update/<int:user_id>', methods=['PUT'])
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        if user:
            data = request.get_json()
            user.name = data.get('name', user.name)
            user.phone = data.get('phone', user.phone)
            user.address = data.get('address', user.address)
            user.cpf = data.get('cpf', user.cpf)
            session.commit()
            return {"message":"Usuário atualizado com sucesso"}
    except Exception as e:
        session.rollback()
        return {"erro":"Falha ao atualizar o usuário"}
    finally:
        session.close()

# @app.route('/user/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     user = User.query.get(user_id)
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify({'message': 'User deleted successfully'})
#     return jsonify({'error': 'User not found'}), 404

# @app.route('/user/delete/<int:user_id>', methods=['DELETE'])
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            return {"message":"Usuário excluído com sucesso"}
    except Exception as e:
        session.rollback()
        return {"erro":"Falha ao excluir o usuário"}
    finally:
        session.close()

if __name__ == "__main__":
    app.run(debug=DevelopmentConfig.DEBUG, port=DevelopmentConfig.PORT_HOST)
