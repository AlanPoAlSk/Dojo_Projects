from flask import render_template , redirect , request , session

from to_do_app import app

from to_do_app.models.user_model import User
from to_do_app.models.todo_model import Todo





@app.route('/dashboard')
def welcome():
    if not 'user_id' in session:
        return redirect('/')
    user = User.show_name(session['user_id'])
    all_todos = Todo.show_all()
    return render_template('dashboard.html' , user = user, all_todos = all_todos )


# @app.route('/todo/new')
# def new_todo():
#     if 'user_id' not in session:
#         return redirect('/')
#     return render_template('dashboard.html')

@app.route('/todo/create', methods = ['POST'])
def create_todo():
    if 'user_id' not in session:
        return redirect('/')
    if not Todo.is_valid(request.form):
        return redirect('/dashboard')
    todo_data = {
        **request.form,
        'user_id': session['user_id']
    }
    
    Todo.create(todo_data)
    return redirect('/dashboard')

@app.route('/todo/<int:id>/delete')
def delete_todo(id):
    data = {
        ** request.form,
        'id' : id
    }
    Todo.delete(data)
    return redirect('/dashboard')

@app.route('/todo/<int:id>/edit')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        'id' :id  
    }
    user = User.show_name(session['user_id'])
    
    return render_template('dashboard_edit.html', todo = Todo.get_one(data), all_todos = Todo.show_all() , user = user)

@app.route('/todo/<int:id>/update', methods=['POST'])
def edit_show(id):
    data = {
        **request.form,
        'id' : id
    }
    if not Todo.is_valid(request.form):
        return redirect(f'/todo/{id}/edit')
        
    Todo.save(data)
    
    return redirect('/dashboard')



@app.route('/todo/<int:id>/view')
def view(id):
    if 'user_id' not in session:
        return redirect('/dashboard')
    
    data = {
        'id' : id
    }
    user = User.show_name(session['user_id'])
    todo = Todo.get_one(data)
    return render_template('show_view.html',todo = todo , user = user)