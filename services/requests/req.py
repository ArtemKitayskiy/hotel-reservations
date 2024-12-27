import time
import random
import requests

url = 'http://ml_service:8000/api/prediction'

example_data = {
    'no_of_adults': random.randint(1,4),
    'no_of_children': random.randint(1,4),
    'no_of_weekend_nights': random.randint(0,4),
    'no_of_week_nights': random.randint(0,10),
    'type_of_meal_plan': random.choice(['Meal Plan 1', 'Meal Plan 2', 'Meal Plan 3']),
    'required_car_parking_space': random.choice([False, True]),
    'room_type_reserved': f"Room_Type {random.randint(1,7)}",
    'lead_time': random.randint(0, 365),
    'arrival_year': random.choice([2017, 2018]),
    'arrival_month': str(random.choice(range(0,13))).rjust(2,'0'),
    'arrival_date': str(random.choice(range(0,29))).rjust(2,'0'),
    'market_segment_type': random.choice(['Offline', 'Online']),
    'repeated_guest': random.choice([False, True]),
    'no_of_previous_cancellations': random.randint(0,5),
    'no_of_previous_bookings_not_canceled': random.randint(0,30),
    'avg_price_per_room': random.uniform(10,500),
    'no_of_special_requests': random.randint(0,5),
    'is_weekend': random.choice([False, True]),
    'price_deviation': random.uniform(-50,50)
}

def send_requests(item_id: str, request_data: dict):
    try:
        response = requests.post(url, 
                                params={"item_id": item_id}, 
                                json=request_data)
        
        if response.status_code == 200:
            print(response.json())
        else:
            print(f'Error: {response.status_code}')

    except Exception as e:
        print(f"Error: {e}")

def main():
    cnt = 0
    while True:
        item_id = cnt
        send_requests(item_id, example_data)
        time.sleep(5)
        cnt += 1
    
if __name__ == "__main__":
    main()
