import React from 'react';
import { render, fireEvent, waitFor, screen, getByText } from '@testing-library/react';
import App from './App';

test('renders todo list correctly', async () => {
  // Mock the API response
  const mockTodos = ['Todo 1', 'Todo 2'];
  global.fetch = jest.fn().mockResolvedValueOnce({
    json: () => Promise.resolve({ todos: mockTodos }),
  });

  render(<App />);

  // Check if the title is rendered correctly
  expect(screen.getByText('Todo List')).toBeInTheDocument();

  // Check if the initial todos are rendered correctly
  await waitFor(() => {
    expect(screen.getByText('Todo 1')).toBeInTheDocument();
    expect(screen.getByText('Todo 2')).toBeInTheDocument();
  });
});

test('adds a new todo', async () => {
  // Mock the API response for fetching todos
  const mockTodos = ['Todo 1', 'Todo 2'];
  global.fetch = jest.fn()
    .mockResolvedValueOnce({ json: () => Promise.resolve({ todos: mockTodos }) })
    .mockResolvedValueOnce({ json: () => Promise.resolve({ todo: 'New Todo' }) });

  render(<App />);

  // Fill the input and click "Add" button
  const input = screen.getByPlaceholderText('Add Todo');
  fireEvent.change(input, { target: { value: 'New Todo' } });
  fireEvent.click(screen.getByText('Add'));

  // Check if the new todo is added
  await waitFor(() => {
    expect(screen.getByText('New Todo')).toBeInTheDocument();
  });
});
