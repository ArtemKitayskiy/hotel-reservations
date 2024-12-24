import os
import pickle
import mlflow

def download_model(run_id: str, output_path: str):
    """Загружает модель из MLflow по run_id и сохраняет в файл"""

    try:
        model_uri = f"runs:/{run_id}/best_model"
        model = mlflow.sklearn.load_model(model_uri)
        print(f"Model loaded successfully from run_id: {run_id}")

        with open(output_path, "wb") as f:
            pickle.dump(model, f)
        print(f"Model saved to {output_path}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_id = 'f1e402c95cd04b429cc8ec80e1311352'
    output_path = os.path.join(os.path.dirname(__file__), "model.pkl")

    mlflow.set_tracking_uri(uri="http://localhost:5000")

    download_model(run_id, output_path)