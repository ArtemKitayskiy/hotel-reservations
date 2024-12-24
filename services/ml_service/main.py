import pandas as pd
from fastapi import FastAPI, Query
from pydantic import BaseModel
from api_handler import FastAPIHandler

app = FastAPI()

model_path = "../models/model.pkl"
predictor = FastAPIHandler(model_path)

class PredictionRequest(BaseModel):
    no_of_adults: int  = 2
    no_of_children: int = 0
    no_of_weekend_nights: int = 1
    no_of_week_nights: int = 2
    type_of_meal_plan: str = 'Meal Plan 1'
    required_car_parking_space: bool = False
    room_type_reserved: str = 'Room_Type 1'
    lead_time: int = 224
    arrival_year: int = 2017
    arrival_month: str = '10'
    arrival_date: str = '02'
    market_segment_type: str = 'Offline'
    repeated_guest: bool = False
    no_of_previous_cancellations: int = 0
    no_of_previous_bookings_not_canceled: int = 0
    avg_price_per_room: float = 65.0
    no_of_special_requests: int = 0
    is_weekend: bool = False
    price_deviation: float = -29.5

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/api/prediction")
async def make_prediction(item_id: str = Query(..., description="ID объекта"), 
                          request_data: PredictionRequest = None):
    
    data_dict = {field: value for field, value in request_data.__dict__.items()}
    prediction = predictor.predict(data_dict)

    return {"item_id": item_id, "predict": prediction}