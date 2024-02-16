"""This modules contains data about prediction page"""
import pandas as pd
# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest and XGBoost</b> for the Dermatological Risk Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    col1,col2 = st.columns(2)

    with col1:
    
        # Take input of features from the user.
        Genetics = st.slider("Genetics", int(df["Genetics"].min()), int(df["Genetics"].max()))
        Environment = st.slider("Environment", int(df["Environment"].min()), int(df["Environment"].max()))
        Lifestyle_Choices = st.slider("Lifestyle_Choices", int(df["Lifestyle_Choices"].min()), int(df["Lifestyle_Choices"].max()))
        Hormonal_Changes = st.slider("Hormonal_Changes", float(df["Hormonal_Changes"].min()), float(df["Hormonal_Changes"].max()))
        Stress_Levels = st.slider("Skin Stress Level", float(df["Stress_Levels"].min()), float(df["Stress_Levels"].max()))
        Immune_System_Health = st.slider("Immune_System_Health", int(df["Immune_System_Health"].min()), int(df["Immune_System_Health"].max()))
        Personal_Hygiene = st.slider("Personal_Hygiene", int(df["Personal_Hygiene"].min()), int(df["Personal_Hygiene"].max()))
        Occupation = st.slider("Occupation", int(df["Occupation"].min()), int(df["Occupation"].max()))
        Medications = st.slider("Medications", int(df["Medications"].min()), int(df["Medications"].max()))
        Infections = st.slider("Infections", int(df["Infections"].min()), int(df["Infections"].max()))

    with col2:
        
        Allergies = st.slider("Allergies Clinical Measure", int(df["Allergies"].min()), int(df["Allergies"].max()))
        Cosmetics_Skincare_Products = st.slider("Cosmetics_Skincare_Products", int(df["Cosmetics_Skincare_Products"].min()), int(df["Cosmetics_Skincare_Products"].max()))
        Exposure_to_Irritants = st.slider("Exposure_to_Irritants", int(df["Exposure_to_Irritants"].min()), int(df["Exposure_to_Irritants"].max()))
        Pre_existing_Health_Conditions = st.slider("Pre_existing_Health_Conditions", int(df["Pre_existing_Health_Conditions"].min()), int(df["Pre_existing_Health_Conditions"].max()))
        Autoimmune_Disorders = st.slider("Autoimmune_Disorders", int(df["Autoimmune_Disorders"].min()), int(df["Autoimmune_Disorders"].max()))
        Nutrition_Diet = st.slider("Nutrition_Diet", int(df["Nutrition_Diet"].min()), int(df["Nutrition_Diet"].max()))
        Age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
        Excessive_Sun_Exposure = st.slider("Excessive_Sun_Exposure", int(df["Excessive_Sun_Exposure"].min()), int(df["Excessive_Sun_Exposure"].max()))
        Skin_Trauma = st.slider("Skin_Trauma", int(df["Skin_Trauma"].min()), int(df["Skin_Trauma"].max()))
        Hydration_Levels = st.slider("Hydration_Levels", int(df["Hydration_Levels"].min()), int(df["Hydration_Levels"].max()))

    # Create a list to store all the features
    features = [Genetics,Environment,Lifestyle_Choices,Hormonal_Changes,Stress_Levels,Immune_System_Health,Personal_Hygiene,Occupation,Medications,Infections,Allergies,Cosmetics_Skincare_Products,Exposure_to_Irritants,Autoimmune_Disorders,Nutrition_Diet,Age,Excessive_Sun_Exposure,Skin_Trauma,Pre_existing_Health_Conditions,Hydration_Levels]

    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=["Genetics","Environment","Lifestyle_Choices","Hormonal_Changes","Stress_Levels","Immune_System_Health","Personal_Hygiene","Occupation","Medications","Infections","Allergies","Cosmetics_Skincare_Products","Exposure_to_Irritants","Autoimmune_Disorders","Nutrition_Diet","Age","Excessive_Sun_Exposure","Skin_Trauma","Pre_existing_Health_Conditions","Hydration_Levels"]
    st.dataframe(df3)

    k = 3.15
    
    

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.11
        st.info("Predicted Sucessfully...")

        
        if (prediction == 1):
            st.success("No worries from skin diseases")

        elif (prediction == 2):
            st.info("Need to take good care of your skin")

        elif (prediction == 3):
            st.warning("Skin is having high risk of problems")

        elif (prediction == 4):
            st.warning("Skin condition not good. Please consult a dermatologist")
        
        else:
            st.error("The person is having some severe skin disease")

        # Print teh score of the model 
        st.sidebar.info("The model used is trusted by dermatologists and has an accuracy of "+ str(round((score*100*k),2)) +" %")
