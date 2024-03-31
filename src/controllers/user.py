from flask import Blueprint, request
from models.user_model import UserModel 
import bcrypt

user = Blueprint('user', __name__)

path = '/home/diego/Documents/python/simple_login/src/models/database/users.db'

@user.route('/user/register', methods=['POST'])
def register():
  email = request.headers['email']
  password = request.headers['password']
  password = password.encode('utf-8')
  # password = b"password"
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  print(hashed)
  db = UserModel(path)
  db.insert_user(email, hashed)
  return 'User registered'

@user.route('/user/login', methods=['POST'])
def login():
  email = request.headers['email']
  password = request.headers['password']
  password_bytes = password.encode('utf-8') 
  db = UserModel(path)
  find_user = db.select_user(email)

  if bcrypt.checkpw(password_bytes, find_user[0][2]):
    return "It Matches!"
  else:
    return "It Does not Match :("

  # return str(find_user[0][2])
