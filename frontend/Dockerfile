# Frontend - React, Next.js, Vite, etc.
FROM node:20

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install --legacy-peer-deps

COPY frontend/ .

# Expose frontend port
EXPOSE 3000

CMD ["npm", "start"]
