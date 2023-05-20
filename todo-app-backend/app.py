# from flask import Flask, render_template, request, redirect

# app = Flask(__name__)
# todos = []

# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html', todos=todos)

# @app.route('/add', methods=['POST'])
# def add():
#     todo = request.form['todo']
#     todos.append(todo)
#     return redirect('/')

# @app.route('/delete', methods=['POST'])
# def delete():
#     todo = request.form['todo']
#     todos.remove(todo)
#     return redirect('/') 

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


from flask import Flask, jsonify, request
from flask_cors import CORS
import os


app = Flask(__name__)

allowed_origin = "http://localhost:8000"

if(os.getenv("ALLOWED_ORIGIN") != None):
  allowed_origin = os.getenv("ALLOWED_ORIGIN")


print('CORS Set to :', allowed_origin)

CORS(app,
resources={
    r"/todos": {"origins": allowed_origin},
    r"/add": {"origins": allowed_origin},
    r"/delete": {"origins": allowed_origin}
})       

todos = []


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})


@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.json.get('todo')
    todos.append(todo)
    return jsonify({'todo': todo})


@app.route('/delete', methods=['POST'])
def delete_todo():
    todo = request.json.get('todo')
    todos.remove(todo)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
