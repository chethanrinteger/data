import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px
import matplotlib.pyplot as plt

st.title("Product Intelligent")
st.sidebar.title("Inventory")

st.markdown("Product Intelligent ")
st.sidebar.markdown("Inventory And Product Performance")


DATA_URL = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vRffwlmhiARpcl03gaG07TDMbFCbjJOdFpOkscij4-CPIwzNCiQdwC8TsxBjKjN6zV3BUraUDjxUC0p/pub?gid=1604835951&single=true&output=csv")
data = pd.read_csv(DATA_URL)
#data = load_data()
st.write(data)
