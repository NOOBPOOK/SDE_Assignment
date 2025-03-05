import bcrypt
from flask import jsonify

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def compare_passwords(password, hashed_password):
    return bcrypt.checkpw(password, hashed_password)

def create_user_service(db, data):
    # Hash the password before storing 
    data["password"] = hash_password(data["password"])
    resp = db.users.insert_one(data)

    if resp.acknowledged:
        return jsonify({
            'message': 'User created successfully',
            'user_id': str(resp.inserted_id),
        }), 201

    else:
        return jsonify({
            'message': 'User creation failed'
        }), 500
    
def get_users_service(db, query_id):
    query = {}
    if query_id != "" and query_id is not None:
        query['_id'] = query_id

    result = db.users.find(query, {"password": 0})

    users = []

    # For ObjectId to be json serializable
    for i in result:
        i['_id'] = str(i['_id'])
        users.append(i)

    return jsonify({
        'users': users,
        'count': len(users),
    }),200

def update_user_service(db, id, data):

    # Hash the password before storing
    if "password" in data:
        data["password"] = hash_password(data["password"])

    resp = db.users.update_one({"_id": id}, {"$set": data})

    return jsonify({
        'message': 'User updated successfully',
        'modified_count': resp.modified_count,
        '_id': str(resp.upserted_id),
    }), 200

def delete_user_service(db, id):

    resp = db.users.delete_one({"_id": id})

    if resp.acknowledged:
        return jsonify({
            'message': 'User deleted successfully',
            'deleted_count': resp.deleted_count,
        }), 200
    else:
        return jsonify({
            'message': 'User deletion failed'
        }), 500