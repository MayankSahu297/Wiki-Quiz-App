from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import router

app = FastAPI(title="Wiki Quiz API", version="0.1.0")

# Allow all origins for simple prototype
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Wiki Quiz API is running. Visit /docs for Swagger UI."}

# Include API router
app.include_router(router)
