# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from movies import router as movies_router  # import your router

app = FastAPI()

origins = [ 
    "http://localhost:5173", 
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, etc.
    allow_headers=["*"],
)
# Include the movies router
app.include_router(movies_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Movie API"}
