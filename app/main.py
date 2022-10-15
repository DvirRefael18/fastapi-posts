from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from . import models
from .database import engine
from .routers import post, user, auth, vote

# models.Base.metadata.create_all(bind=engine) # To use sqlalchemy

app = FastAPI()

# origins = ["https://www.google.com", "https://www.youtube.com"] # for example
origins = [" * "] # all domains

app.add_middleware(
    CORSMiddleware, #function that runs before every request.
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
 
# request Get method url: "/"
@app.get("/")
def root():
    return {"message": "Welcome to my API! Hello developers."}




