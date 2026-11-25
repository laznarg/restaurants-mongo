from fastapi import FastAPI
from database import restaurants, neighborhoods

app = FastAPI(title="Restaurants API")


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/restaurants")
def get_restaurants():
    return list(
        restaurants.find({}, {"_id": 0}).limit(100)
    )


@app.get("/neighborhoods")
def get_neighborhoods():
    return list(
        neighborhoods.find({}, {"_id": 0})
    )