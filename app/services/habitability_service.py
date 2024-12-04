import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess_user_data(user_data):
    """
    Preprocess user-uploaded data for habitability prediction.
    Args:
        user_data (pd.DataFrame): User-provided data.
    Returns:
        pd.DataFrame: Processed data ready for prediction.
    """
    # Scale numerical features
    scaler = StandardScaler()
    user_data_scaled = scaler.fit_transform(user_data)
    return user_data_scaled

def predict_habitability(model_path, user_data):
    """
    Predict habitability based on user-uploaded data.
    Args:
        model_path (str): Path to the trained model file.
        user_data (pd.DataFrame): User-provided data for prediction.
    Returns:
        list: Predicted habitability scores.
    """
    # Load the trained model
    model = joblib.load(model_path)

    # Preprocess the data
    processed_data = preprocess_user_data(user_data)

    # Make predictions
    predictions = model.predict(processed_data)
    return predictions
