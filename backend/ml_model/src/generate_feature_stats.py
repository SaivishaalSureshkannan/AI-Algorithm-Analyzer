import pandas as pd
import numpy as np
import json

# Load your training features DataFrame
features_df = pd.read_csv('../dataset/processed/processed_dataset.csv')

stats = {}
for col in features_df.select_dtypes(include=[np.number]).columns:
    stats[col] = {
        'min': float(features_df[col].min()),
        'max': float(features_df[col].max()),
        'mean': float(features_df[col].mean()),
        'std': float(features_df[col].std())
    }

with open('feature_stats.json', 'w') as f:
    json.dump(stats, f, indent=2)
