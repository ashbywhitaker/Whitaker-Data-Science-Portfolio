import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.datasets import load_iris

# Main title displayed at the top of the app
st.title("Interactive Unsupervised Machine Learning Explorer")

# Brief explanation of K-Means clustering for the user
st.write("K-Means Clustering: An unsupervised learning algorithm that groups data into clusters based on similarity. It works by minimizing the distance between data points and their assigned cluster center.")

# Explanation of the Elbow Method
st.write("Elbow Method: A technique used to determine the optimal number of clusters (k) by plotting inertia. The 'elbow' point indicates diminishing returns in clustering performance.")

# Explanation of the Silhouette Score
st.write("Silhouette Score: A metric that measures how well data points fit within their assigned clusters. Values range from -1 to 1, where higher values indicate better clustering.")

# Explanation of PCA
st.write("PCA (Principal Component Analysis): A dimensionality reduction technique used to project high-dimensional data into 2D for visualization.")

# Choosing a dataset
st.sidebar.header("Dataset Selection")

dataset_option = st.sidebar.selectbox(
    "Choose Dataset",
    ["Upload your own", "Iris Sample Dataset"]
)

# Manipulating Data Based on User Decision with Dataset
if dataset_option == "Upload your own":
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Dataset Preview:", df.head())
    else:
        st.warning("Please upload a dataset to proceed.")
        df = None

elif dataset_option == "Iris Sample Dataset":
    iris = load_iris(as_frame=True)
    df = iris.frame
    st.write("Iris Dataset: Contains measurements of iris flowers including sepal and petal dimensions.")
    st.write(df.head())

# If the User chooses a dataset or uploads their own
if df is not None:

    # Select features for clustering
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    st.sidebar.header("Feature Selection")

    selected_features = st.sidebar.multiselect(
        "Select features for clustering",
        numeric_cols,
        default=numeric_cols[:2]
    )

    # Ensure at least two features are selected
    if len(selected_features) < 2:
        st.warning("Please select at least two features.")
        st.stop()

    X = df[selected_features]

    # Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Model hyperparameters
    st.sidebar.header("Model Hyperparameters")
    k = st.sidebar.slider("Number of Clusters (k)", 2, 10, 3)

    # Elbow Method
    st.subheader("Elbow Method (Finding Optimal K)")

    inertia = []
    K_range = range(1, 11)

    for i in K_range:
        km = KMeans(n_clusters=i, random_state=42, n_init=10)
        km.fit(X_scaled)
        inertia.append(km.inertia_)

    fig1, ax1 = plt.subplots()
    ax1.plot(K_range, inertia, marker='o')
    ax1.set_xlabel("Number of Clusters (k)")
    ax1.set_ylabel("Inertia")
    ax1.set_title("Elbow Plot")
    st.pyplot(fig1)

    # Train final model
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = model.fit_predict(X_scaled)

    # Add labels to dataset
    df["Cluster"] = clusters

    # Silhouette Score
    score = silhouette_score(X_scaled, clusters)

    st.subheader("Model Performance")
    st.write(f"**Silhouette Score:** {score:.3f}")
    st.write("The silhouette score measures how similar a data point is to its own cluster compared to other clusters.")

    # PCA Visualization
    st.subheader("Cluster Visualization (PCA Projection)")

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    pca_df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
    pca_df["Cluster"] = clusters

    fig2, ax2 = plt.subplots()
    sns.scatterplot(
        data=pca_df,
        x="PC1",
        y="PC2",
        hue="Cluster",
        palette="Set2",
        ax=ax2
    )

    ax2.set_title("Clusters Visualized in 2D")
    st.pyplot(fig2)

    # Display the data
    st.subheader("Clustered Dataset")
    st.dataframe(df)

    # Download option
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Clustered Data",
        csv,
        "clustered_data.csv",
        "text/csv"
    )

else:
    st.info("Please upload or select a dataset to start clustering.")