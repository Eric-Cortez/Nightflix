# stuff
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hi_man():
    return {"message": "Hey there Mr. Eric, Hi Man."}


@app.get("/movies")
async def get_movies():
    return {"message": "Here are all the movies."}


@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int):
    return {"message": f"Here is the movie with id {movie_id}"}


@app.delete("/movies/delete/{movie_id}")
async def delete_movie(movie_id: int):
    return {"message": f"Delete movie with id {movie_id}"}


@app.post("/movies/new")
async def create_movie():
    return {"message": "This will create a new movie. It's called hi man."}
