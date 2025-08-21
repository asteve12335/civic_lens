# Use official Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy frontend code
COPY . .

# Expose React dev server port
EXPOSE 3000

# Start development server
CMD ["npm", "start"]
