from fastapi.middleware.cors import CORSMiddleware
from BackEnd import app
from BackEnd.routers import routes


app.include_router(routes.router)



origins = [
    "https://localhost:3000"
]


app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)


