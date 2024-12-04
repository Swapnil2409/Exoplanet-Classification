import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(file_path):
    """Load dataset from the given file path."""
    return pd.read_csv(file_path)

def handle_missing_values(df):
    """Handle missing values in the dataset."""
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

def normalize_data(df, columns):
    """Normalize numerical data."""
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def encode_categorical_data(df, columns):
    """Encode categorical variables."""
    encoder = LabelEncoder()
    for col in columns:
        df[col] = encoder.fit_transform(df[col])
    return df

def preprocess_data(file_path):
    """Complete preprocessing pipeline."""
    df = load_data(file_path)
    df = handle_missing_values(df)
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    df = normalize_data(df, numerical_cols)
    df = encode_categorical_data(df, categorical_cols)
    return df
