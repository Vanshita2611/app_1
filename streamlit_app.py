import streamlit as st
import pandas as pd
import numpy as np

st.title('Empowering the Automotive Industry with Data Analytics')

@st.cache
def load_data(nrows):
  
   data = pd.read_csv('../input/indian-cars-dataset/cars_ds_final.csv', nrows=nrows)
   df['car'] = df.Make + ' ' + df.Model
   c = ['Make','Model','car','Variant','Body_Type','Fuel_Type','Fuel_System','Type','Drivetrain','Ex-Showroom_Price','Displacement','Cylinders',
     'ARAI_Certified_Mileage','Power','Torque','Fuel_Tank_Capacity','Height','Length','Width','Doors','Seating_Capacity','Wheelbase','Number_of_Airbags']
    df_full = df.copy()
    df['Ex-Showroom_Price'] = df['Ex-Showroom_Price'].str.replace('Rs. ','',regex=False)
    df['Ex-Showroom_Price'] = df['Ex-Showroom_Price'].str.replace(',','',regex=False)
    df['Ex-Showroom_Price'] = df['Ex-Showroom_Price'].astype(int)
    df = df[c]
    df = df[~df.ARAI_Certified_Mileage.isnull()]
    df = df[~df.Make.isnull()]
    df = df[~df.Width.isnull()]
    df = df[~df.Cylinders.isnull()]
    df = df[~df.Wheelbase.isnull()]
    df = df[~df['Fuel_Tank_Capacity'].isnull()]
    df = df[~df['Seating_Capacity'].isnull()]
    df = df[~df['Torque'].isnull()]
    df['Height'] = df['Height'].str.replace(' mm','',regex=False).astype(float)
    df['Length'] = df['Length'].str.replace(' mm','',regex=False).astype(float)
    df['Width'] = df['Width'].str.replace(' mm','',regex=False).astype(float)
    df['Wheelbase'] = df['Wheelbase'].str.replace(' mm','',regex=False).astype(float)
    df['Fuel_Tank_Capacity'] = df['Fuel_Tank_Capacity'].str.replace(' litres','',regex=False).astype(float)
    df['Displacement'] = df['Displacement'].str.replace(' cc','',regex=False)
    df.loc[df.ARAI_Certified_Mileage == '9.8-10.0 km/litre','ARAI_Certified_Mileage'] = '10'
    df.loc[df.ARAI_Certified_Mileage == '10kmpl km/litre','ARAI_Certified_Mileage'] = '10'
    df['ARAI_Certified_Mileage'] = df['ARAI_Certified_Mileage'].str.replace(' km/litre','',regex=False).astype(float)
    df.Number_of_Airbags.fillna(0,inplace= True)
    df['price'] = df['Ex-Showroom_Price'] * 0.014
    df.drop(columns='Ex-Showroom_Price', inplace= True)
    df.price = df.price.astype(int)
    HP = df.Power.str.extract(r'(\d{1,4}).*').astype(int) * 0.98632
    HP = HP.apply(lambda x: round(x,2))
    TQ = df.Torque.str.extract(r'(\d{1,4}).*').astype(int)
