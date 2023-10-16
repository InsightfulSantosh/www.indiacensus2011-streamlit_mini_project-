import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
df=pd.read_csv("India's.csv")
lst=list(df["State"].unique())
lst.insert(0,"India's Overall")

st.sidebar.title("India's Census")
selected_State=st.sidebar.selectbox("select a state",lst)
primary=st.sidebar.selectbox("select primary parameter", df.columns[5:])
Secondary=st.sidebar.selectbox("select secondary parameter", df.columns[5:])
plot=st.sidebar.button("Plot graph")
if plot:
    if selected_State=="India's Overall":
        fig=px.scatter_mapbox(df,lat="Latitude",lon="Longitude",size=primary,color=Secondary,hover_name="District",
                              zoom=4,size_max=35,width=1200,height=700,mapbox_style="carto-positron")
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=df[df.State==selected_State]
        fig=px.scatter_mapbox(state_df,lat="Latitude",lon="Longitude",size=primary,color=Secondary,hover_name="District",
                              zoom=5,size_max=35,width=1200,height=700,mapbox_style="carto-positron")
        st.plotly_chart(fig,use_container_width=True)


