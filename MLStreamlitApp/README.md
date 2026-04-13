# Interactive Machine Learning Explorer

## Project Overview
This project provides an interactive web app built with Streamlit that allows users to explore and compare classification models on sample datasets. Users can choose between Iris and Wine datasets or upload their own CSV files, select hyperparameters, and see how the models perform in terms of accuracy and ROC curves. The app demonstrates how logistic regression and decision trees work, along with key metrics to evaluate model performance.

## Instructions

### Running Locally
1. **Clone the repository** (or copy the code into a Python file):
   ```bash
   git clone <repository_url>
   cd <repository_directory>
2. **Download Necessary Packages**
    pip install streamlit pandas scikit-learn matplotlib
3. **Accessing the App**
    Using the Deployed Version: http://10.24.219.83:8501
# App Features

## Datasets
- Sample datasets: Iris and Wine, loaded directly from scikit-learn.
- Custom dataset upload: Users can upload their own CSV files.

## Models
- **Logistic Regression**: A model suitable for binary and multi-class classification. Users can tune:
  - `C`: Inverse regularization strength (smaller values = stronger regularization).
  - `Max Iterations`: Max number of training iterations.
- **Decision Tree**: A tree-based model. Users can tune:
  - `Max Depth`: Limits tree depth.
  - `Min Samples Split`: Minimum samples for a split.

## Hyperparameters
- Set via sliders and selection boxes in the sidebar.
- Hyperparameters influence model training and performance.

## Metrics & Visualizations
- **Accuracy**: Proportion of correct predictions.
- **ROC Curve**:
  - For binary classification, a single ROC curve with AUC.
  - For multi-class classification, ROC curves for each class (OvR approach) with individual AUC scores.

## Notes
- Multi-class ROC curves are plotted for each class with AUC scores.
- The app provides explanations for metrics and hyperparameters for educational purposes.
