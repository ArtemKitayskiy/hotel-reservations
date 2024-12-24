import pickle
import pandas as pd

class FastAPIHandler():
    def __init__(self, model_path: str):
        try:
            with open(model_path, 'rb') as model_file:
                self.model = pickle.load(model_file)
            print(f"Model loaded successfully from {model_path}")
        except Exception as e:
            print(f"Error: {e}")
            
    def predict(self, data: dict):
        try:
            x_test = pd.DataFrame([data])
            prediction = self.model.predict(x_test)
            return int(prediction[0])
        except Exception as e:
            print(f"Error: {e}")
            return None