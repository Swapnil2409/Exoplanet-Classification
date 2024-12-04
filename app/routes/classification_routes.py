from flask import Blueprint, jsonify
from app.services.classification_service import train_model

classification_blueprint = Blueprint('classification', __name__)

@classification_blueprint.route("/train", methods=["GET"])
def train():
    """
    Train the classification model.
    Returns:
        JSON: Training results including accuracy and classification report.
    """
    try:
        file_path = "data/exoplanets.csv"  # Path to your dataset
        model_save_path = "data/trained_model.pkl"  # Path to save the trained model
        results = train_model(file_path, model_save_path)
        return jsonify({
            "message": "Model trained successfully!",
            "accuracy": results["accuracy"],
            "classification_report": results["classification_report"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
