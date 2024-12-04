import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

def preprocess_data(file_path):
    """
    Load and preprocess the exoplanet dataset.
    Args:
        file_path (str): Path to the dataset file.
    Returns:
        tuple: Features (X) and target (y) DataFrames.
    """
    # Load dataset
    data = pd.read_csv(file_path)

    # Drop irrelevant columns
    columns_to_drop = ['kepid', 'kepoi_name', 'kepler_name', 'koi_pdisposition']
    data = data.drop(columns=columns_to_drop, axis=1)

    # Handle missing values
    data = data.fillna(data.median(numeric_only=True))

    # Encode the target variable
    data['koi_disposition'] = data['koi_disposition'].map({
        'CONFIRMED': 1,
        'FALSE POSITIVE': 0,
        'CANDIDATE': 2
    })

    # Drop rows with missing target values
    data = data.dropna(subset=['koi_disposition'])

    # Separate features and target
    X = data.drop(columns=['koi_disposition'], axis=1)
    y = data['koi_disposition']

    return X, y

def train_model(file_path, model_save_path):
    """
    Train a Random Forest model on the dataset.
    Args:
        file_path (str): Path to the dataset file.
        model_save_path (str): Path to save the trained model.
    Returns:
        dict: Model accuracy and classification report.
    """
    # Preprocess data
    X, y = preprocess_data(file_path)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest Classifier
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=['False Positive', 'Confirmed', 'Candidate'])

    # Save the trained model
    joblib.dump(model, model_save_path)

    return {
        "accuracy": accuracy,
        "classification_report": report
    }
