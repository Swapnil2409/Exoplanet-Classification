import sys
import os

# Add the project root directory to Python's module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from app.routes.preprocessing_routes import preprocessing_blueprint
from app.routes.classification_routes import classification_blueprint
from app.routes.habitability_routes import habitability_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(preprocessing_blueprint, url_prefix='/preprocessing')
app.register_blueprint(classification_blueprint, url_prefix='/classification')
app.register_blueprint(habitability_blueprint, url_prefix='/habitability')

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
