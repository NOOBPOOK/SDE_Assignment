from flask import Blueprint, jsonify, request
from utils.connect import Connect
from .user_services import create_user_service, get_users_service, update_user_service, delete_user_service

user_routes = Blueprint('user_routes', __name__)

instance = Connect()

@user_routes.route('/users', methods=['POST'])
def create_users():
    try:
        data = request.get_json()

        # Check whether the request has valid fields
        req_fields = ['_id', 'name', 'email', 'password']
        user_data = {}
        for field in req_fields:
            if field not in data:
                return jsonify({
                    "message": f"{field} is required"
                }), 400
            if not isinstance(data[field], str) or data[field] == "":
                return jsonify({
                    "message": f"{field} cannot be empty and must be a String"
                }), 400
            user_data[field] = data[field]
                
        return create_user_service(instance.DB, user_data)

    except Exception as e:
        return jsonify({
            "message": "An error occurred",
            "error": str(e)
        }), 500
        
@user_routes.route('/users', methods=['GET'])
def get_users():
    try:
        id = request.args.get('_id')  
        return get_users_service(instance.DB, id)
    
    except Exception as e:
        return jsonify({
            "message": "An error occurred",
            "error": str(e)
        }), 500


@user_routes.route('/users', methods=['PUT']) 
def update_user():
    try:
        data = request.get_json()

        if len(data.keys()) == 0:
            return jsonify({
                "message": "Data is required"
            }), 400

        id = request.args.get('_id')
        
        if id is None or id == "":
            return jsonify({
                "message": "_id is required"
            }), 400
        
        # Check whether the request has valid fields
        req_fields = ['name', 'email', 'password', '_id']
        for field in data:
            if field not in req_fields:
                return jsonify({
                    "message": f"{field} is not a valid field"
                }), 400
            if field == '_id':
                return jsonify({
                    "message": "Cannot update the _id field"
                }), 400
            if not isinstance(data[field], str) or data[field] == "":
                return jsonify({
                    "message": f"{field} cannot be empty and must be a String"
                }), 400
        
        return update_user_service(instance.DB, id, data)
    
    except Exception as e:
        return jsonify({
            "message": "An error occurred",
            "error": str(e)
        }), 500
        
@user_routes.route('/users', methods=['DELETE'])
def delete_user():
    try:
        id = request.args.get('_id')
        if id is None or id == "":
            return jsonify({
                "message": "_id is required"
            }), 400
        
        return delete_user_service(instance.DB, id)
    
    except Exception as e:
        return jsonify({
            "message": "An error occurred",
            "error": str(e)
        }), 500