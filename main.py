from BackEnd import create_app
from BackEnd.database import Base, engine

app = create_app()
Base.metadata.create_all(bind=engine)



