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

print('CORS Set to :', os.getenv("ALLOWED_ORIGIN"))

CORS(app,
resources={
    r"/todos": {"origins": os.getenv("ALLOWED_ORIGIN")},
    r"/add": {"origins": os.getenv("ALLOWED_ORIGIN")},
    r"/delete": {"origins": os.getenv("ALLOWED_ORIGIN")}
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
