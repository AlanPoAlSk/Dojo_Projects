from to_do_app import app

from to_do_app.controllers import users_controller
from to_do_app.controllers import todos_controller

if __name__=="__main__":  
    app.run(debug=True, port=8000)