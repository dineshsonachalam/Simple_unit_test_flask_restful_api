from flask import Flask
from routes.authentication import auth_blueprint
app = Flask(__name__)
app.register_blueprint(auth_blueprint)


if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=True)
