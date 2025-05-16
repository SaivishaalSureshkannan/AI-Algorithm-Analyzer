import os
from dataset_creator import DatasetCreator
from model import ComplexityPredictor

def main():
    # Initialize paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_dir = os.path.join(current_dir, '..', 'dataset', 'raw')
    processed_data_dir = os.path.join(current_dir, '..', 'dataset', 'processed')
    model_dir = os.path.join(current_dir, '..', 'models')
    
    # Create model directory if it doesn't exist
    os.makedirs(model_dir, exist_ok=True)
    
    # Initialize dataset creator
    creator = DatasetCreator(raw_data_dir, processed_data_dir)
    
    # Process the dataset
    print("Processing dataset...")
    X, y = creator.get_dataset()
    print(f"Dataset processed. Features shape: {X.shape}")
    
    # Initialize and train the model
    print("\nTraining model...")
    predictor = ComplexityPredictor()
    metrics = predictor.train(X, y)
    
    # Print results
    print(f"\nModel accuracy: {metrics['accuracy']:.2f}")
    print("\nConfusion Matrix:")
    print(metrics['confusion_matrix'])
    
    # Save the model
    model_path = os.path.join(model_dir, 'complexity_predictor.joblib')
    predictor.save_model(model_path)
    print(f"\nModel saved to: {model_path}")

if __name__ == "__main__":
    main() 