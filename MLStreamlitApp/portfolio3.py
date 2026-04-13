import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split #To prepare the data for manipulation
from sklearn.linear_model import LogisticRegression #For the logistic regression part of my model
from sklearn.tree import DecisionTreeClassifier #To use a decision tree
from sklearn.metrics import accuracy_score, roc_curve, roc_auc_score #These will be a few of the metrics I want to use
import matplotlib.pyplot as plt #For the ROC curve 
from sklearn.datasets import load_iris, load_wine #loading the two sample datasets I thought might be interesting

# Title and Brief Descriptions of the Different Metrics and buttons that can be used by the model
st.title("Interactive Machine Learning Explorer")
st.write("Logistic Regression: A classification algorithm that models the probability of a class using the logistic function. It is widely used for binary classification tasks.")

st.write("Decision Tree: A model that splits data based on feature values to make predictions. It creates a flowchart-like structure for decision making.")

st.write("Test Size (%): The percentage of the dataset reserved for testing the model's performance. The remaining data is used for training.")

st.write("C (Inverse Regularization Strength): A parameter controlling regularization; smaller values specify stronger regularization to prevent overfitting. Inverse of regularization strength, so higher C means less regularization.")

st.write("Max Iterations: The maximum number of iterations the algorithm runs during training to optimize the model parameters.")

# Dataset selection
#Creates a section to choose between datasets
dataset_option = st.sidebar.selectbox("Choose Dataset", ["Upload your own", "Iris", "Wine"])
#The following lines of code show a different streamlit depending on what the user chooses
if dataset_option == "Upload your own": #This is used when the user wants to upload their own
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Dataset Preview:", df.head()) #Shows a dataset preview in the viewer
    else:
        st.warning("Please upload a dataset to proceed.")
        df = None
elif dataset_option == "Iris":
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    #Displays a brief description of the dataset the user has chosen
    st.write("Iris Dataset: A dataset loaded from sk.learn containing measurements of 150 iris flowers from three different species. Features include sepal length, sepal width, petal width, and petal length.")
elif dataset_option == "Wine":
    wine = load_wine()
    df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
    df['target'] = wine.target
    #Displays a brief description of the dataset the user has chosen
    st.write("Wine Dataset: Contains chemical analysis results of wines. Similar to the Irish dataset, this dataset contains multiple features of the wine including alcohol content, malic acid, ash, and other chemical properties.")

# Proceed only if the dataset is loaded
if df is not None:
    # Show feature and target selection
    features = df.columns[:-1]
    target = df.columns[-1]
    
    st.sidebar.header("Model Hyperparameters") #The model hyperparameters are what the user can control
    test_size = st.sidebar.slider("Test set size (%)", 10, 50, 20) #Creates a slider for amending the test size
    model_type = st.sidebar.selectbox("Model Type", ["Logistic Regression", "Decision Tree"]) #Creates a selecton box for either logistic regression or decision tree

    # Hyperparameters
    if model_type == "Logistic Regression":
        C = st.sidebar.slider("C (Inverse of regularization strength)", 0.01, 10.0, 1.0)
        max_iter = st.sidebar.slider("Max Iterations", 100, 1000, 200)
    elif model_type == "Decision Tree":
        max_depth = st.sidebar.slider("Max Depth", 1, 20, 5)
        min_samples_split = st.sidebar.slider("Min Samples Split", 2, 20, 2)
    
    # Prepare data
    X = df[features]
    y = df[target]
    
    # Determine number of classes early
    n_classes = len(y.unique()) #This is part of the fix i had to implement for the multi class in the ROC

    # Splitting the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size/100, random_state=42
    )
    
    # The two options in my selection box 
    if model_type == "Logistic Regression":
        model = LogisticRegression(C=C, max_iter=max_iter, solver='lbfgs')
    elif model_type == "Decision Tree":
        model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split)
    
    # Train model
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Get probabilities with a separate multi class and binary as I was getting errors for multi class using Iris and Wine
    if hasattr(model, "predict_proba"):
        y_proba_full = model.predict_proba(X_test)
        if n_classes > 2:
            y_proba = y_proba_full  # full probabilities for multi-class
        else:
            y_proba = y_proba_full[:, 1]  # binary positive class probability
    else:
        y_proba = None

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"**Accuracy:** {accuracy:.2f}") #Display Accuracy 
    st.write("**Accuracy:** The proportion of correct predictions out of all predictions made.") #Brief description of accuracy
    st.write("Formula: (Number of correct predictions) / (Total predictions)") #Overview of formula

    # ROC-AUC calculation and plotting
    if y_proba is not None:
        if n_classes > 2:
            # Multi-class ROC-AUC- as mentioned previously I had to account specifically for multi class
            roc_auc = roc_auc_score(y_test, y_proba, multi_class='ovr')
        else:
            # Binary ROC-AUC
            roc_auc = roc_auc_score(y_test, y_proba)
#A little more context for the ROC multi class 
#ROC is intended for binary classifications, but some of the datasets people might want to use will not be binary.
#Therefore, the 'ovr' will take a class as positive and combine the other classes into one negative.
#It then does this with every class and uses the average to compute the ROC.
        # Plot ROC curve for binary
        #While the curves are there, it really is not showing properly at all. 
        # I debated deleting this entirely from the model, but it could just be for these datasets that is struggling.
        if n_classes == 2:
            fpr, tpr, _ = roc_curve(y_test, y_proba)
            fig, ax = plt.subplots()
            ax.plot(fpr, tpr, label=f'ROC curve (area = {roc_auc:.2f})')
            ax.plot([0, 1], [0, 1], 'k--')
            ax.set_xlabel('False Positive Rate')
            ax.set_ylabel('True Positive Rate')
            ax.set_title('ROC Curve')
            ax.legend(loc='lower right')
            st.pyplot(fig)
        else:
            from sklearn.preprocessing import label_binarize
            y_test_binarized = label_binarize(y_test, classes=range(n_classes))
            fig, ax = plt.subplots()
            for i in range(n_classes):
                fpr, tpr, _ = roc_curve(y_test_binarized[:, i], y_proba[:, i])
                roc_auc = roc_auc_score(y_test_binarized[:, i], y_proba[:, i])
                ax.plot(fpr, tpr, label=f'Class {i} (area = {roc_auc:.2f})')
                ax.plot([0, 1], [0, 1], 'k--')
                ax.set_xlabel('False Positive Rate')
                ax.set_ylabel('True Positive Rate')
                ax.set_title('Multi-class ROC Curves')
                ax.legend(loc='lower right')
                st.pyplot(fig)
else:
    st.info("Please upload or select a dataset to start modeling.")