
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import health


app = FastAPI(
    title="CivicLens API",
    version="0.1.0",
    description="Backend for CivicLens civic issue reporting platform"
)

# Allow CORS for frontend (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:5173"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#include routers
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Welcome to CivicLens API"}
