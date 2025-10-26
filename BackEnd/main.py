from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from BackEnd.routers import routes  # adjust if needed

app = FastAPI()

# Allowed origins
origins = [
    "http://localhost:5173",  # React dev server
]

# Add CORS middleware BEFORE including routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # ["*"] works temporarily
    allow_credentials=True,
    allow_methods=["*"],       # must include OPTIONS for preflight
    allow_headers=["*"],       # allow Content-Type, etc.
)

app.include_router(routes.router)
