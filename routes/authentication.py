from flask import Blueprint,request,jsonify
from utility.auth_crud import crud_operation
auth_blueprint = Blueprint('authentication',__name__)
auth = crud_operation()


@auth_blueprint.route('/register',methods=['POST'],endpoint='register')
def register():
    content = request.get_json()
    username = content['username']
    password = content['password']
    result = auth.register_users(username,password)
    return jsonify(result)



@auth_blueprint.route('/login',methods=['POST'],endpoint='login')
def login():
    content = request.get_json()
    username = content['username']
    password = content['password']
    result = auth.login_users(username,password)
    return jsonify(result)

# Get all posts created by all users
@auth_blueprint.route('/',methods=['GET'],endpoint='index')
def index():
    return "Hello world"

@auth_blueprint.route('/logout',methods=['GET'],endpoint='logout')
def logout():
    pass


#@todo_blueprint.route('/',methods=['GET'],endpoint='read_all')