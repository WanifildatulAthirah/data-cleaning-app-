import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Cleaning App - Wani", layout="wide", page_icon="🌼")
st.title("🧹 Data Cleaning App")

# Step 1: File Upload
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file:
    # Step 2: Load the file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.subheader("Preview of the Data")
    st.dataframe(df.head())

    # Step 3: Show missing values and duplicates
    st.subheader("Data Information")
    st.write("Missing values per column:", df.isnull().sum())
    st.write("Number of duplicate rows:", df.duplicated().sum())

    # Step 4: Buttons for cleaning
    st.subheader("Data Cleaning Options")

    if st.button("Remove Missing Values"):
        df = df.dropna()
        st.success("Missing values removed!")
        st.dataframe(df.head())

    if st.button("Handle Missing Values (Fill with Mean/Mode)"):
        for column in df.columns:
            if df[column].dtype in ['int64', 'float64']:
                df[column].fillna(df[column].mean(), inplace=True)
            else:
                df[column].fillna(df[column].mode()[0], inplace=True)
        st.success("Missing values handled!")
        st.dataframe(df.head())

    if st.button("Remove Duplicate Rows"):
        df = df.drop_duplicates()
        st.success("Duplicate rows removed!")
        st.dataframe(df.head())

    # Step 5: Download cleaned file
    st.subheader("Download Cleaned File")

    cleaned_csv = df.to_csv(index=False)  # Save dataframe as CSV string

    st.download_button(
        label="Download Cleaned CSV",
        data=cleaned_csv,
        file_name='cleaned_data.csv',
        mime='text/csv'
    )
