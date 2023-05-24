# Base image
FROM ubuntu:20.04

# Install system dependencies
RUN apt-get update && apt-get install -y curl build-essential

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_19.x | bash -
RUN apt-get install -y nodejs

# Install Python and pip
RUN apt-get install -y python3 python3-pip

# Set a working directory
WORKDIR /app

# Create a non-root user
RUN useradd -ms /bin/bash appuser

RUN mkdir /app/todo-app-backend && mkdir /app/todo-app-frontend

# Set the ownership and permissions
RUN chown -R appuser:appuser /app && \
    chmod -R 755 /app

USER appuser

# Set ENV
ENV REACT_APP_FLASK_APP_API_URL=http://localhost:5000
ENV ALLOWED_ORIGIN=http://localhost:3000


# Copy the Flask Backend
COPY todo-app-backend/ /app/todo-app-backend/

# Set a working directory
WORKDIR /app/todo-app-backend/

RUN pip3 install --no-cache-dir -r requirements.txt

RUN python3 -m pytest

# Copy the React Frontend
COPY todo-app-frontend/ /app/todo-app-frontend/

# Set a working directory
WORKDIR /app/todo-app-frontend/

# Install dependencies
RUN npm ci --quiet --production

#Unit Test
RUN CI=true npm test

# Build the app
RUN npm run build

# Expose the react's port
EXPOSE 3000

# Expose the flask's port
EXPOSE 5000

# Copy entrypoint script
COPY entrypoint.sh /app

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]