import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple, Dict

class ComplexityPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.complexity_classes = ['O(1)', 'O(n)', 'O(n^2)', 'O(2^n)']
    
    def train(self, X: np.ndarray, y: np.ndarray, test_size: float = 0.2) -> Dict:
        """Train the model and return evaluation metrics."""
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        
        # Train the model
        self.model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred, labels=self.complexity_classes)
        
        # Plot confusion matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
                   xticklabels=self.complexity_classes,
                   yticklabels=self.complexity_classes)
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.savefig('confusion_matrix.png')
        plt.close()
        
        return {
            'accuracy': accuracy,
            'confusion_matrix': conf_matrix
        }
    
    def predict(self, features: np.ndarray) -> str:
        """Predict complexity class for given features."""
        return self.model.predict(features.reshape(1, -1))[0]
    
    def save_model(self, filepath: str):
        """Save the trained model to disk."""
        joblib.dump(self.model, filepath)
    
    @classmethod
    def load_model(cls, filepath: str) -> 'ComplexityPredictor':
        """Load a trained model from disk."""
        predictor = cls()
        predictor.model = joblib.load(filepath)
        return predictor 