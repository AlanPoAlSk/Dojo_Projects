from flask import render_template , redirect , request , session

from to_do_app import app

from to_do_app.models.user_model import User


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/registration', methods = ['POST'])
def create():
    if User.validate(request.form):
        User.register(request.form)
        logged_profile = User.login(request.form)
        
        if logged_profile:
            session['user_id'] = logged_profile.id
            return redirect('/dashboard')
    else :
        return redirect('/')
    
    
@app.route('/login' , methods = ['POST'])
def log():
    logged_profile = User.login(request.form)
    if logged_profile:
        session['user_id'] = logged_profile.id
        
        return redirect('/dashboard' )
    else :
        return redirect('/#login')
    
    
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')