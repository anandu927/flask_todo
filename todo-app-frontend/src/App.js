import React, { useState, useEffect } from 'react';
import './App.css';
import { API_URL } from './env';

function App() {

  console.log(process.env.REACT_APP_FLASK_APP_API_URL);
  
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
 
  useEffect(() => {
    fetch(API_URL+'/todos')
      .then(response => response.json())
      .then(data => setTodos(data.todos));
  }, []);

  const addTodo = () => {
    if (newTodo.trim() !== '') {
      fetch(API_URL+'/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ todo: newTodo })
      })
        .then(response => response.json())
        .then(data => {
          setTodos([...todos, data.todo]);
          setNewTodo('');
        });
    }
  };

  const deleteTodo = todo => {
    fetch(API_URL+'/delete', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ todo })
    })
      .then(() => {
        const updatedTodos = todos.filter(item => item !== todo);
        setTodos(updatedTodos);
      });
  };

  return (
    <div className="App">
      <h1>Todo List</h1>
      <div className="input-container">
        <input
          type="text"
          placeholder="Add Todo"
          value={newTodo}
          onChange={e => setNewTodo(e.target.value)}
        />
        <button onClick={addTodo}>Add</button>
      </div>
      <ul className="todo-list">
        {todos.map((todo, index) => (
          <li key={index}>
            {todo}
            <button onClick={() => deleteTodo(todo)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
