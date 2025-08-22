from fastapi import FastAPI
from routers import health

app = FastAPI(
    title="CivicLens API",
    version="0.1.0",
    description="Backend for CivicLens civic issue reporting platform"
)

#include routers
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Welcome to CivicLens API"}
