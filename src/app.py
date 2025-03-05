from flask import Flask, jsonify
from api.user_api import user_routes

app = Flask(__name__)


app.register_blueprint(user_routes)


@app.route('/')
def affirmation():
    return jsonify({
        "message": "The server is up and running!"
    })

if __name__ == "__main__":

    print("This file executes the Flask application.")

    app.run(host='0.0.0.0', port=8080, debug=True)