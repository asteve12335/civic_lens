# Backend - Python (FastAPI, Django, Flask, etc.)
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY backend/ .

# Expose API port
EXPOSE 8000

# Start app (replace with your backend entrypoint)
CMD ["python", "main.py"]
