# Interactive Unsupervised Machine Learning Explorer

## Project Overview
This project is an interactive web application built using Streamlit that allows users to explore unsupervised machine learning techniques. Users can upload their own datasets or use a sample dataset, select features, adjust clustering parameters, and visualize how the model groups data. The app focuses on K-Means clustering and provides tools such as the Elbow Method, Silhouette Score, and PCA visualization to help users understand clustering performance and structure. The goal is to create an intuitive, hands-on learning experience for experimenting with unsupervised models.

## Instructions

### Running Locally
1. **Download Necessary Packages**
    pip install streamlit pandas numpy scikit-learn matplotlib seaborn
2. **Run the Application**
    streamlit run app.py
3. **Use the Deployed Version**
    ____

## App Features

### Datasets
- Sample datasets: Iris, loaded directly from scikit-learn.
- Custom dataset upload: Users can upload their own CSV files.

### Model
- K-Means Clustering: Groups data into clusters based on similarity

### Hyperparameters
- Controlled through sidebar sliders: Number of Clusters
- Adjustable between 2 and 10

### Feature Selection
- Select which numeric features to include in clustering
- Must select at least two features

### Metrics & Visualizations
- Elbow Plot: Shows inertia for different values of k
- Silhouette Score: Measures how well each data point fits within its cluster
- PCA Visualization: Reduces high-dimensional data into 2D
- Clustered Dataset View: Displays the dataset with assigned cluster labels

### Additional Features
- Download Option: Users can download the clustered dataset as a CSV file

