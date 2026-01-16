from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import secrets
from werkzeug.security import generate_password_hash, check_password_hash

database = SQLAlchemy()

class Login(database.Model):
    emp_id = database.Column(database.Integer, primary_key = True)
    emp_name = database.Column(database.String(50), unique = True)
    password = database.Column(database.String(255), nullable = False)
    token = database.Column(database.String(255), unique=True, nullable=True)

    def set_password(self,pwd):
        self.password = generate_password_hash(pwd)

    def check_password(self,pwd):
        return check_password_hash(self.password,pwd)
    
    def generate_token(self):
        self.token = secrets.token_hex(32)
        return self.token





class Employees(database.Model):
    id = database.Column(database.Integer, primary_key = True, autoincrement = True)
    name = database.Column(database.String(50), nullable = False)
    email = database.Column(database.String(100), nullable = False, unique = True)
    department = database.Column(database.String(100))
    role = database.Column(database.String(100))
    date_joined = database.Column(database.DateTime, default = datetime.now)

    def data(self):
        return{
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'department':self.department,
            'role':self.role,
            'date_joined':self.date_joined
        }




