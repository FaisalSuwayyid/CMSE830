import streamlit as st

import seaborn as sns
import pandas as pd
import plotly.express as px

df_iris = sns.load_dataset("iris")

fig = px.scatter_3d(df_iris, x='sepal_length', y='sepal_width', z='petal_width', color='species')

st.write("""
# Iris Dataset
Relations between sepal and petal dimensions in different Iris species?
""")
st.plotly_chart(fig, theme=None, use_container_width=True)

