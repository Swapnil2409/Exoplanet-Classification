from flask import Blueprint, jsonify
from app.services.data_preprocessing import preprocess_data

preprocessing_blueprint = Blueprint('preprocessing', __name__)

@preprocessing_blueprint.route("/", methods=["GET"])
def preprocess():
    """Preprocess the dataset."""
    file_path = "data/exoplanets.csv"  # Path to the dataset
    try:
        preprocessed_data = preprocess_data(file_path)
        return jsonify({
            "message": "Data preprocessing successful!",
            "columns": preprocessed_data.columns.tolist(),
            "sample_data": preprocessed_data.head().to_dict(orient="records")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
