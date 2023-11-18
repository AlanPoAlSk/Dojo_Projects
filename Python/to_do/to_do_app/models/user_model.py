from to_do_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from to_do_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.confirm_password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
        
    
    @classmethod
    def register(cls,form):
        
        hash = bcrypt.generate_password_hash(form['password'])
        data = {
            **form,
            'password': hash,
        }
        
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)
        """
        
        return connectToMySQL('todo_db').query_db(query,data)
    
    
    @classmethod
    def get_one(cls,email):
        
        data = {'email': email}
        query = """
            SELECT * FROM users
            WHERE email = %(email)s
        """
        results = connectToMySQL('todo_db').query_db(query,data)
    
        if results:
            return cls(results[0])
        else :
            return False
    
    
    @staticmethod
    def validate(form):
        
        query = 'SELECT * FROM users WHERE users.email = %(email)s'
        results= connectToMySQL('todo_db').query_db(query,form)
        is_valid = True 
        if len(form['first_name']) < 2:
            flash("<Your name must contain at least 2 characters.>", "name_err")
            is_valid = False
        if len(form['last_name']) < 2:
            flash("<Your last name must contain at least 2 characters.>","last_name_err")
            is_valid = False
        if not EMAIL_REGEX.match(form['email']):
            flash('<Invalid Email - Please Insert a Valid Email>', "email_err")
            is_valid = False
        elif len(results) >= 1:
            flash(' Email already in the system!', 'email_err')
            is_valid = False
        if len(form['password']) < 8:
            flash("<Your password must have at least 8 characters>" , "pass_err")
            is_valid = False
        if form['confirm_password'] != form['password']:
            flash("<Password and Confirm_password don't match>" , "conf_pass_err")
            is_valid = False
        return is_valid
    
    
    @classmethod
    def login(cls,form):
        
        profile_found = cls.get_one(form['email'])
        
        if profile_found:
            if bcrypt.check_password_hash(profile_found.password,form['password']):
                return profile_found
            else :
                flash('Invalid login.','login_err')
                return False
        
        else :
            flash('Invalid login.','login_err')
            return False
        
        
    @classmethod
    def show_name(cls,id):
        data = {'id': id}
        query = """
            SELECT * FROM users
            WHERE id = %(id)s
        """
        results = connectToMySQL('todo_db').query_db(query,data)
    
        if results:
            return cls(results[0])
        else :
            return False
        
        
    