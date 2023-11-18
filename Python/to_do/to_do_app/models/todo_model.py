from to_do_app.config.mysqlconnection import connectToMySQL
from flask import flash
from to_do_app import app
from to_do_app.models import user_model


class Todo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.priority = data['priority']
        self.due_to = data['due_to']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        
        
        
    @classmethod
    def create(cls,form):
        
        
        query = """
            INSERT INTO todos (name,priority,due_to, user_id)
            VALUES (%(name)s,%(priority)s,%(due_to)s,%(user_id)s);
        """
        
        return connectToMySQL('todo_db').query_db(query,form)
    
    
    @classmethod
    def get_one(cls,data):
        
        
        
        query = """
            SELECT * FROM todos JOIN users ON todos.user_id = users.id
            WHERE todos.id = %(id)s;
        """

        results = connectToMySQL('todo_db').query_db(query,data)
        if results:
            row = results[0]
            this_todo= cls(row)
            user_data = {
                **row,
                'id' :row['users.id'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
            }
            this_user = user_model.User(user_data)
            this_todo.post = this_user
            return this_todo
        return False
        
    @classmethod
    def show_all(cls):
        
        query = """
            SELECT * FROM todos 
            JOIN users ON  todos.user_id = users.id
            ORDER BY todos.due_to ASC; 
        """
        results = connectToMySQL('todo_db').query_db(query)
        all_todos = []
        
        if results:
            for row in results :
                this_todo = cls(row)
                user_data = {
                    **row,
                    'id' :row['users.id'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
                
                this_user = user_model.User(user_data)
                this_todo.post = this_user
                all_todos.append(this_todo)
        return all_todos
    
    # @classmethod
    # def api_show_all(cls):
        
    #     query = """
    #         SELECT * FROM todos 
    #         JOIN users ON  todos.user_id = users.id; 
    #     """
    #     results = connectToMySQL('todo_db').query_db(query)
        
    #     return results
    
    @staticmethod
    def is_valid(data):
        valid = True
        if len(data['name']) < 2:
            flash('name is required', 'name_err')
        if len(data['priority']) < 1:
            flash('priority is required', 'pri_err')
            valid = False
        if len(data['due_to']) < 1:
            flash('date is required', 'due_err')
        return valid    
            
    @classmethod
    def delete(cls,data):
        
        query = """
            DELETE FROM todos
            WHERE id = %(id)s
        """
        return connectToMySQL('todo_db').query_db(query,data)
    
    
    @classmethod
    def save(cls,data):
        
        
        query = """
            UPDATE todos 
            SET name = %(name)s, priority = %(priority)s, due_to = %(due_to)s
            WHERE id = %(id)s;
        """
        
        return connectToMySQL('todo_db').query_db(query,data)
    
    