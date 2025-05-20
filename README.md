# AI Algorithm Complexity Analyzer

## Overview
An intelligent web application that analyzes Python code from user to predict and visualize algorithmic time complexity using machine learning. The system combines traditional static analysis with ML-based predictions to provide accurate complexity assessments and interactive visualizations.

## Features
- **Dual Analysis System**
  - Traditional static code analysis
  - ML-based complexity prediction with confidence scoring
- **Interactive Visualization**
  - Real-time D3.js graphs showing complexity growth patterns
  - Support for O(1), O(n), O(n²), and O(2ⁿ) complexities
- **Code Analysis Features**
  - Loop detection (for/while loops)
  - Recursion identification
  - Nested structure analysis
  - Feature extraction for ML prediction
- **Performance Optimization**
  - Algorithmic improvement suggestions
  - Code optimization recommendations
  - Confidence-based fallback system

## Tech Stack
### Frontend
- **React** with Vite for fast development and building
- **Tailwind CSS** for modern, responsive styling
- **D3.js** for interactive complexity visualizations
- Modern JavaScript (ES6+) features

### Backend
- **FastAPI** for high-performance API endpoints
- **Python AST** for code analysis
- **Machine Learning Pipeline**
  - scikit-learn for model training and prediction
  - Custom feature extraction system
  - Trained on diverse algorithm datasets

### ML/Data Science
- **Feature Engineering** for code pattern recognition
- **Supervised Learning Model** for complexity classification
- **Statistical Analysis** for outlier detection
- **Model Confidence Scoring** for reliability assessment

## Machine Learning Approach
- **Feature Extraction**: Analysis of code structure, loops, recursion patterns
- **Model Training**: Supervised learning on labeled algorithm examples
- **Prediction Pipeline**: Real-time code analysis and complexity classification
- **Confidence Scoring**: Reliability assessment of predictions

## Getting Started
1. Clone the repository
```bash
git clone https://github.com/yourusername/AI-Algorithm-Analyzer.git
```

2. Install frontend dependencies
```bash
cd frontend
npm install
```

3. Install backend dependencies
```bash
cd backend
pip install -r requirements.txt
```

4. Start the development servers
```bash
# Frontend (in frontend directory)
npm run dev

# Backend (in backend directory)
uvicorn app.main:app --reload
```

## Demo
Visit `http://localhost:5173` to try the analyzer:
1. Paste your Python code
2. Click "Analyze"
3. View complexity prediction and visualization
4. Check optimization suggestions
