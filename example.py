import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


a=(" Hello :sunglasses:")
st.write(a)

#dataframe

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)
#st.table(df)
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

#charts

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [19.2403, 73.1305],  #second bracket is use for lattitude and longitude
     columns=['lat', 'lon'])

st.map(df)


picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)


data = pd.read_csv("IPL.csv")
st.dataframe(data)
st.table(data)