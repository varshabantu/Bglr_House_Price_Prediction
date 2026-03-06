#Streamlit UI

#import neceessary libraries

import pickle
import streamlit as st 
import pandas as pd 

#Model De-serialization (loading model)

with open("Linear_model.pkl","rb") as file:
    model = pickle.load(file)

#model.predict(data)


#import joblib
#file = "model.pkl"
#model=joblib.load(file)
#model.predict(data)

#encoded de-serialization(loading encoder)
with open("label_encoder.pkl","rb") as file1:
    encoder = pickle.load(file1)
    

#load cleaned dataset

df = pd.read_csv("cleaned_data.csv")


st.set_page_config(page_title="house price prediction bangalore",page_icon="https://thumbs.dreamstime.com/b/green-houses-community-model-abstract-real-estate-logo-vector-professional-architecture-company-design-115154734.jpg")
with st.sidebar:
    st.title("Bengalore House Price Prediction")
    st.image("https://thumbs.dreamstime.com/b/green-houses-community-model-abstract-real-estate-logo-vector-professional-architecture-company-design-115154734.jpg")

#input fields

#'location','bhk','total_sqft','bath','encoded_loc'
location = st.selectbox("Location: ",options=df["location"].unique())

BHK = st.selectbox("bhk: ",options=sorted(df["bhk"].unique()))

total_sqft = st.number_input("Total_sqft: ",min_value=300)

bath = st.selectbox("No. of Restrooms: ",options=sorted(df["bath"].unique()))

#encoded the new location
encoded_loc = encoder.transform([location])

#new data preparation
new_data = [[BHK,total_sqft,bath,encoded_loc[0]]]

#prediction
col1,col2 = st.columns([1,2])

if col2.button("Predict House Price"):
    pred = model.predict(new_data)[0]
    pred = round(pred*100000)
    st.subheader(f"Predicted Price : Rs. {pred}")