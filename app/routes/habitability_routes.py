from flask import Blueprint, request, jsonify
import pandas as pd
from app.services.habitability_service import predict_habitability

habitability_blueprint = Blueprint('habitability', __name__)

@habitability_blueprint.route("/predict", methods=["POST"])
def predict():
    """
    Predict habitability scores for user-provided data.
    Returns:
        JSON: Predicted habitability scores.
    """
    try:
        # Load user data from request
        user_data = pd.DataFrame(request.json)

        # Path to the trained model
        model_path = "data/trained_model.pkl"

        # Predict habitability
        predictions = predict_habitability(model_path, user_data)

        return jsonify({
            "message": "Prediction successful!",
            "predictions": predictions.tolist()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
