import os
import json
import pandas as pd
from typing import List, Dict, Tuple
from feature_extractor import FeatureExtractor

class DatasetCreator:
    def __init__(self, raw_data_dir: str, processed_data_dir: str):
        self.raw_data_dir = raw_data_dir
        self.processed_data_dir = processed_data_dir
        self.feature_extractor = FeatureExtractor()
        self.complexity_classes = ['O(1)', 'O(n)', 'O(n^2)', 'O(2^n)']
        
        # Create directories if they don't exist
        os.makedirs(raw_data_dir, exist_ok=True)
        os.makedirs(processed_data_dir, exist_ok=True)
    
    def add_code_sample(self, code: str, complexity: str, filename: str = None):
        """Add a new code sample to the raw dataset."""
        if complexity not in self.complexity_classes:
            raise ValueError(f"Complexity must be one of {self.complexity_classes}")
        
        if filename is None:
            # Generate filename based on complexity and count
            count = len([f for f in os.listdir(self.raw_data_dir) 
                        if f.startswith(complexity.replace('(', '').replace(')', ''))])
            filename = f"{complexity.replace('(', '').replace(')', '')}_{count}.py"
        
        filepath = os.path.join(self.raw_data_dir, filename)
        
        # Save code and complexity
        data = {
            'code': code,
            'complexity': complexity
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    
    def process_dataset(self) -> pd.DataFrame:
        """Process all raw code samples into feature vectors."""
        features_list = []
        labels = []
        
        for filename in os.listdir(self.raw_data_dir):
            if filename.endswith('.py'):
                filepath = os.path.join(self.raw_data_dir, filename)
                
                with open(filepath, 'r') as f:
                    data = json.load(f)
                
                try:
                    features = self.feature_extractor.get_feature_vector(data['code'])
                    features_list.append(features)
                    labels.append(data['complexity'])
                except ValueError as e:
                    print(f"Error processing {filename}: {e}")
        
        # Create DataFrame
        df = pd.DataFrame(features_list, 
                         columns=self.feature_extractor.features.keys())
        df['complexity'] = labels
        
        # Save processed dataset
        processed_filepath = os.path.join(self.processed_data_dir, 'processed_dataset.csv')
        df.to_csv(processed_filepath, index=False)
        
        return df
    
    def get_dataset(self) -> Tuple[pd.DataFrame, pd.Series]:
        """Get the processed dataset as features and labels."""
        processed_filepath = os.path.join(self.processed_data_dir, 'processed_dataset.csv')
        
        if not os.path.exists(processed_filepath):
            df = self.process_dataset()
        else:
            df = pd.read_csv(processed_filepath)
        
        X = df.drop('complexity', axis=1)
        y = df['complexity']
        
        return X, y 