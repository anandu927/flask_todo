# Base image
FROM node:latest

# Set a working directory
WORKDIR /app

# Create a non-root user
RUN addgroup --gid 1001 appuser && \
    adduser --disabled-password --gecos "" --uid 1001 --gid 1001 appuser

# Set the ownership and permissions
RUN chown -R appuser:appuser /app && \
    chmod -R 755 /app

# Set the user and group to the non-root user
USER appuser


# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci --quiet --production

# Copy the rest of the app's source code
COPY . .

#Unit Test
RUN CI=true npm test

# Build the app
RUN npm run build

# Expose the app's port
EXPOSE 3000

# Run the app
CMD ["npm", "start"]
