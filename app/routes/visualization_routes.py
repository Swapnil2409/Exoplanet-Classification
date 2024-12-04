from flask import Blueprint, render_template
from app.services.visualization_service import create_visualizations

visualization_blueprint = Blueprint('visualizations', __name__)

@visualization_blueprint.route("/", methods=["GET"])
def visualize():
    """Render visualizations."""
    try:
        visualizations = create_visualizations()
        return render_template("visualization.html", visualizations=visualizations)
    except Exception as e:
        return str(e), 500
