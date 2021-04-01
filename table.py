from flask import Flask, render_template
app = Flask(__name__)   
@app.route('/<int:colums>/<int:rows>')         
def hello_world():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("index.html", students_name=users.first_name, students_lname=users.last_name, students_full=user.first_name +' '+ users.last_name)