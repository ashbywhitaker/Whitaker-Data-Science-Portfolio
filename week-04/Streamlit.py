import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.") 

# Markdown Hashtag - makes it a header - same as using st title 

if st.button("Click me!"):
    st.write("You clicked the button!")
else:
    st.write("Click the button and see what happens!")

##loading CSV file

import pandas as pd

st.subheader("Exploring Our Dataset")

#Load CSV file

df = pd.read_csv("data/sample_data-1.csv")

st.write("Here's our data!")
st.dataframe(df)

city = st.selectbox("Select a City", df["City"].unique(), index = None)
filtered_df = df[df["City"] == city]

st.write(f"People in {city}")
st.dataframe(filtered_df)

# Filter by occupation
occupation = st.selectbox("Select an occupation", df["Occupation"].unique())
filtered_df = df[(df["City"] == city) & (df["Occupation"] == occupation)]

st.write(f"{occupation}s in {city}:")
st.dataframe(filtered_df)

## Add Bar Chart
st.bar_chart(df["Salary"])

##Add Summary Statistics
st.write(df.describe())

import seaborn as sns 

box_plot = sns.boxplot(x=df["City"], y=df["Salary"])

st.pyplot(box_plot.get_figure())