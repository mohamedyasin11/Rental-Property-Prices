# importing the libraries for this project 
import streamlit as st
from datetime import datetime,timedelta
import pickle
st.title('Smart Predictive Modeling for Rental  Property Prices')


types = st.sidebar.selectbox('Type', [None,'RK1','BHK1','BHK2','BHK3','BHK4','BHK4PLUS'])
Type_dict = {'RK1':0,'BHK1':1,'BHK2':2,'BHK3':3,'BHK4':4,'BHK4PLUS':5}

latitude = st.sidebar.number_input('enter the latitude: ')

longitude = st.sidebar.number_input('enter the longitude: ')

lease_type = st.sidebar.selectbox('lease_type', [None,'BACHELOR', 'ANYONE','FAMILY','COMPANY'])
lease_type_dict = {'BACHELOR':0,'ANYONE':1,'FAMILY':2,'COMPANY':3}

gym = st.sidebar.selectbox('gym', [None,'YES', 'NO'])
dict1 = {'NO':0,'YES':1}

lift = st.sidebar.selectbox('lift', [None,'YES', 'NO'])

swimming_pool = st.sidebar.selectbox('swimming_pool', [None,'YES', 'NO'])

negotiable = st.sidebar.selectbox('negotiable', [None,'YES', 'NO'])

furnishing = st.sidebar.selectbox('furnishing', [None,'NOT_FURNISHED','SEMI_FURNISHED','FULLY_FURNISHED'])
furnishing_dict ={'NOT_FURNISHED':0,'SEMI_FURNISHED':1,'FULLY_FURNISHED':2}

parking = st.sidebar.selectbox('parking', [None,'NONE','TWO_WHEELER','FOUR_WHEELER','BOTH'])
parking_dict = {'NONE':0,'TWO_WHEELER':1,'FOUR_WHEELER':2,'BOTH':3}

property_size =  st.sidebar.number_input('enter the property_size: ')

property_age =  st.sidebar.number_input('enter the property_age: ')

bathroom =  st.sidebar.number_input('enter the No of bathroom: ')

facing = st.sidebar.selectbox('facing', [None,'N','S','E','W','NE','NW','SE','SW'])
facing_dict ={'N':0,'S':1,'E':2,'W':3,'NE':4,'NW':5,'SE':6,'SW':7}

cup_board =  st.sidebar.number_input('enter the No of cup_board: ')

floor =  st.sidebar.number_input('enter the No of floor: ')

total_floor =  st.sidebar.number_input('enter the No of total_floor: ')

water_supply = st.sidebar.selectbox('water_supply', [None,'CORPORATION','CORP_BORE','BOREWELL'])
water_supply_dict = {'CORPORATION':0,'CORP_BORE':1,'BOREWELL':2}

building_type = st.sidebar.selectbox('building_type', [None,'IF','IH','AP','GC'])
building_type_dict = {'IF':0,'IH':1,'AP':2,'GC':3}

balconies =  st.sidebar.number_input('enter the No of balconies: ')


data = ['type', 'latitude', 'longitude', 'lease_type', 'gym', 'lift',
       'swimming_pool', 'negotiable', 'furnishing', 'parking', 'property_size',
       'property_age', 'bathroom', 'facing', 'cup_board', 'floor',
       'total_floor', 'water_supply', 'building_type', 'balconies']

if None not in data and st.button('predict'):
    features = [Type_dict[types], latitude, longitude, lease_type, dict1[gym], dict1[lift],
           dict1[swimming_pool], dict1[negotiable], furnishing_dict[furnishing], 
           parking_dict[parking], property_size,property_age, bathroom, facing_dict[facing], 
           cup_board, floor,total_floor, water_supply_dict[water_supply],
           building_type_dict[building_type],balconies]
    model = pickle.load(open('Property_Rental_Price.sav','rb'))
    predict = model.predict([features])[0]
    st.title(f"your Rental Price is : Rs{round(predict)}")