import json
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import mysql.connector
from mysql.connector import Error
import plotly.express as px                             # CHART VIZUALISATION
import boto3                                            # AWS S3 BUKET CONECTION AND READ
from sqlite3 import Connection
from sqlalchemy import create_engine                    # MYSQL CONNECTION AND READ
import pickle
import joblib
import requests
import test

class option:
  
  option_cuisines = ['American', 'Asian', 'NorthIndian', 'Thai', 'European', 'Mexican',
       'Chinese', 'Cafe', 'Italian', 'FingerFood', 'Indian', 'Mughlai',
       'Mediterranean', 'FastFood', 'SouthIndian', 'Middle', 'Eastern',
       'Bengali', 'Tex-Mex', 'Biryani', 'Desserts', 'Seafood',
       'StreetFood', 'Tea', 'Bakery', 'Burger', 'Pizza', 'HealthyFood',
       'Salad', 'Beverages', 'Japanese', 'British', 'Spanish', 'Greek',
       'Charcoal', 'Grill', 'Indonesian', 'NorthEastern', 'Burmese',
       'German', 'Andhra', 'Chettinad', 'Goan', 'Hyderabadi', 'Awadhi',
       'Arabian', 'Lebanese', 'Lucknowi', 'IceCream', 'Kerala',
       'Rajasthani', 'Armenian', 'Sandwich', 'Malaysian', 'French',
       'Maharashtrian', 'Malwani', 'Portuguese', 'African', 'Juices',
       'Tibetan', 'Mithai', 'BBQ', 'Cajun', 'Vietnamese', 'Steak',
       'Parsi', 'Mangalorean', 'Gujarati', 'Korean', 'International',
       'Fusion', 'Turkish', 'Singaporean', 'Malay', 'Western',
       'Australian', 'Cantonese', 'Dim', 'Sum', 'Pakistani', 'Afghani',
       'Filipino', 'Lankan', 'Döner', 'Bar', 'Food', 'Restaurant',
       'Börek', 'World', 'Cuisine', 'Patisserie', 'Izgara', 'Fresh',
       'Fish', 'Kebab', 'Coffee-Tea', 'Curry', 'Taiwanese',
       'Contemporary', 'Sushi', 'Ramen', 'Tapas', 'Vegetarian',
       'Peruvian', 'Latin', 'Brazilian', 'Mineira', 'Gourmet',
       'Argentine', 'AsianFusion', 'Kiwi', 'Pub', 'Chips', 'Sunda',
       'Peranakan', 'Deli', 'Belgian', 'Durban', 'Scottish', 'Breakfast',
       'Southwestern', 'Bihari', 'Naga', 'Assamese', 'Drinks', 'RawMeats',
       'Kashmiri', 'Moroccan', 'Nepalese', 'Iranian', 'Varies', 'Oriya',
       'Persian', 'Canadian', 'Southern', 'Caribbean', 'Irish',
       'Hawaiian', 'Cuban', 'Diner', 'Bubble', 'Teriyaki']

  encoded_cusines = {'American': 1,'Asian': 2,'NorthIndian': 3, 'Thai': 4, 'European': 5,'Mexican': 6, 'Chinese': 7,'Cafe': 8,
 'Italian': 9,'FingerFood': 10,'Indian': 11,'Mughlai': 12,'Mediterranean': 13,'FastFood': 14,'SouthIndian': 15,'Middle': 16,'Eastern': 17,'Bengali': 18,
 'Tex-Mex': 19,'Biryani': 20,'Desserts': 21,'Seafood': 22,'StreetFood': 23,'Tea': 24,'Bakery': 25,'Burger': 26,'Pizza': 27,'HealthyFood': 28,'Salad': 29,'Beverages': 30,'Japanese': 31,'British': 32,
 'Spanish': 33,'Greek': 34,'Charcoal': 35,'Grill': 36,'Indonesian': 37,'NorthEastern': 38,'Burmese': 39,'German': 40,'Andhra': 41,'Chettinad': 42,'Goan': 43,'Hyderabadi': 44,
 'Awadhi': 45,'Arabian': 46,'Lebanese': 47,'Lucknowi': 48,'IceCream': 49,'Kerala': 50,'Rajasthani': 51,'Armenian': 52,'Sandwich': 53,'Malaysian': 54,'French': 55,'Maharashtrian': 56,
 'Malwani': 57,'Portuguese': 58,'African': 59,'Juices': 60,'Tibetan': 61,'Mithai': 62,'BBQ': 63,'Cajun': 64,'Vietnamese': 65,'Steak': 66,'Parsi': 67,'Mangalorean': 68,'Gujarati': 69,
 'Korean': 70,'International': 71,'Fusion': 72,'Turkish': 73,'Singaporean': 74,'Malay': 75,'Western': 76,'Australian': 77,'Cantonese': 78,'Dim': 79, 'Sum': 80,
 'Pakistani': 81,'Afghani': 82,'Filipino': 83,'Lankan': 84,'Döner': 85,'Bar': 86,'Food': 87,'Restaurant': 88,'Börek': 89, 'World': 90,'Cuisine': 91,'Patisserie': 92,'Izgara': 93,'Fresh': 94,
 'Fish': 95,'Kebab': 96,'Coffee-Tea': 97,'Curry': 98,'Taiwanese': 99,'Contemporary': 100,'Sushi': 101,'Ramen': 102,'Tapas': 103,'Vegetarian': 104,'Peruvian': 105,'Latin': 106,'Brazilian': 107,
 'Mineira': 108,'Gourmet': 109,'Argentine': 110,'AsianFusion': 111,'Kiwi': 112,'Pub': 113,'Chips': 114,'Sunda': 115,'Peranakan': 116,'Deli': 117,'Belgian': 118,'Durban': 119,'Scottish': 120,'Breakfast': 121,
 'Southwestern': 122,'Bihari': 123,'Naga': 124,'Assamese': 125,'Drinks': 126,'RawMeats': 127, 'Kashmiri': 128, 'Moroccan': 129,'Nepalese': 130, 'Iranian': 131, 'Varies': 132, 'Oriya': 133, 'Persian': 134,
 'Canadian': 135, 'Southern': 136, 'Caribbean': 137, 'Irish': 138, 'Hawaiian': 139, 'Cuban': 140, 'Diner': 141, 'Bubble': 142,
 'Teriyaki': 143}

  option_rating_text =['VeryGood', 'Excellent', 'Poor', 'Good', 'Average', 'Not rated']
  
  encoded_rating_text ={'Not rated':1, 'Poor':2, 'Average':3, 'Good':4, 'VeryGood':5, 'Excellent':6}
  
  option_rating = ['1', '2', '3', '4', '5']
  
  encoded_rating ={'1':1.0, '2':2.0, '3':3.0, '4':4.0, '5':5.0 }
  

  # 'Dummy':  72,  
  
  option_city_id =['New Delhi', 'Kolkata', 'Mumbai', 'Bangalore', 'Pune',  'Hyderabad', 'Chennai', 'Lucknow', 'Kochi',
       'Jaipur', 'Ahmedabad', 'Chandigarh', 'Goa', 'Indore', 'Nashik', 'Ludhiana', 'Guwahati', 'Amritsar', 'Kanpur',
       'Allahabad', 'Aurangabad', 'Bhopal', 'Ranchi', 'Vizag', 'Bhubaneshwar', 'Coimbatore', 'Mangalore', 'Vadodara', 'Nagpur',
       'Agra', 'Dehradun', 'Mysore', 'Puducherry', 'Surat', 'Varanasi', 'Patna', 'Dubai', 'Singapore', 'Sharjah', 'Abu Dhabi', 'Colombo',
       'İstanbul', 'Ankara', 'London', 'Doha', 'Makati City',  'Cape Town', 'Sandton', 'Brasília',
       'São Paulo', 'Manchester', 'Birmingham', 'Auckland', 'Wellington City', 'Rio de Janeiro', 'Jakarta', 'Pretoria', 'Edinburgh', 
       ' Yorkton',  ' Vernonia', ' Mayfield', ' Dicky Beach', ' Trentham East', ' Lakes Entrance',' Hepburn Springs', ' Ojo Caliente', ' Inverloch',
       ' Vineland Station', ' Weirton',  ' Potrero',  ' Cochrane', ' Princeton', 
       ' Tanunda', ' Clatskanie', ' Fernley', ' Middleton Beach', ' Mc Millan', ' Bandung', ' Lorn',
       ' Victor Harbor', ' Huskisson', ' Armidale', ' Winchester Bay', ' Forrest', ' Macedon', ' Monroe',
       ' Phillip Island', ' Consort', ' Santa Rosa',  ' Penola', ' Beechworth', ' Chatham-Kent',
       ' Paynesville', ' East Ballina', ' Lincoln',  ' Montville', ' Flaxton', ' Lakeview', ' Balingup', ' Palm Cove', ' Orlando', ' Tampa Bay',
       ' Pensacola', ' Albany', ' Valdosta', ' Gainesville', ' Savannah', ' Columbus', ' Dalton', ' Augusta', ' Athens', ' Macon',
       ' Rest of Hawaii', ' Des Moines', ' Davenport',  ' Sioux City',
       ' Cedar Rapids/Iowa City', ' Waterloo', ' Dubuque', ' Boise', ' Pocatello']
  
  encoded_city_id ={'New Delhi':  1,  'Kolkata':   2,  'Mumbai':   3,  'Bangalore':   4,  'Pune':   5,  'Hyderabad':   6,   'Chennai':  7,  'Lucknow':   8,  'Kochi':   9,
        'Jaipur':  10,  'Ahmedabad':  11,  'Chandigarh':  12,  'Goa':  13,  'Indore':  14,  'Nashik':  16,  'Ludhiana':  20,  'Guwahati':  21,  'Amritsar':  22,
        'Kanpur':  23,  'Allahabad':  24,  'Aurangabad':  25,  'Bhopal':  26,  'Ranchi':  27,  'Vizag':  28,  'Bhubaneshwar':  29, 'Coimbatore':  30,   'Mangalore': 31,
        'Vadodara':  32,  'Nagpur':  33,  'Agra':  34,  'Dehradun':  35, 'Mysore':   36,  'Puducherry':  37, 'Surat':   38,  'Varanasi':  39,  'Patna':  40,
        'Dubai':  51,  'Singapore':  52,  'Sharjah':  56, 'Abu Dhabi':   57,  'Colombo':  58,  'İstanbul':  59,  'Ankara':  60,  'London':  61,  'Doha':  62,
        'Makati City':  63,  'Cape Town' : 64,  'Sandton':  65,  'Brasília':  66,  'São Paulo':  67,  'Manchester':  68,  'Birmingham':  69, 'Auckland':   70,  'Wellington City':  71,
        'Rio de Janeiro':  73,  'Jakarta':  74, 'Pretoria':   75, 'Edinburgh':   76, ' Yorkton': 3600, ' Vernonia' : 8351, ' Mayfield':  2249, ' Dicky Beach':  2575,
        ' Trentham East'  : 1556, ' Lakes Entrance':  1364, ' Hepburn Springs':  1563, ' Ojo Caliente': 7598, ' Inverloch':  1342, ' Vineland Station':  3418, ' Weirton': 10358, ' Potrero': 8956, 
        ' Cochrane': 10261, ' Princeton': 3977, ' Tanunda': 1770, ' Clatskanie': 8410, ' Fernley': 7634, ' Middleton Beach': 1902, ' Mc Millan':  6321, ' Bandung': 11052, ' Lorn':  2242, ' Victor Harbor': 1730,
        ' Huskisson': 2218, ' Armidale': 2309, ' Winchester Bay': 8327, ' Forrest': 1695, ' Macedon': 1565, ' Monroe': 10238, ' Phillip Island': 1345, ' Consort':  2824, ' Santa Rosa': 11071,
        ' Penola': 1800, ' Beechworth': 1424, ' Chatham-Kent': 3525, ' Paynesville': 1353, ' East Ballina':  2051, ' Lincoln':  943, ' Montville': 2617, ' Flaxton': 2576, ' Lakeview':  8397,
        ' Balingup' : 1924, ' Palm Cove':  2430, ' Orlando':  601, ' Tampa Bay': 604, ' Pensacola':  607, ' Albany':  610, ' Valdosta':  613, ' Gainesville':  616, ' Savannah':  619,
        ' Columbus': 622, ' Dalton':  625, ' Augusta':  628, ' Athens':  634, ' Macon':  637, ' Rest of Hawaii':  640, ' Des Moines':  643, ' Davenport':  646, ' Sioux City':  649,
        ' Cedar Rapids/Iowa City': 652, ' Waterloo':  655, ' Dubuque':  658, ' Boise':  664, ' Pocatello':  667 }
  
  option_country_id =['India', 'United Arab Emirates', 'Singapore', 'Sri Lanka', 'Turkey', 'England', 'Qatar', 'Philippines', 'South Africa', 'Brazil', 'New Zealand', 'Dummy', 'Indonesia', 
                      'Canada', 'USA', 'Australia']
  
  encoded_country_id ={ 'India': 1,'United Arab Emirates' : 214, 'Singapore':184, 'Sri Lanka': 191, 'Turkey' : 208, 'England' : 215, 'Qatar' : 166, 'Philippines' : 162, 
                       'South Africa' : 189, 'Brazil' : 30, 'New Zealand' : 148, 'Dummy': 17, 'Indonesia' : 94, 'Canada': 37, 'USA' : 216, 'Australia': 14}
  


  # Sample data
  facility_places = {
      
    'India': ['New Delhi', 'Kolkata', 'Mumbai', 'Bangalore', 'Pune',  'Hyderabad', 'Chennai', 'Lucknow', 'Kochi',
       'Jaipur', 'Ahmedabad', 'Chandigarh', 'Goa', 'Indore', 'Nashik', 'Ludhiana', 'Guwahati', 'Amritsar', 'Kanpur',
       'Allahabad', 'Aurangabad', 'Bhopal', 'Ranchi', 'Vizag', 'Bhubaneshwar', 'Coimbatore', 'Mangalore', 'Vadodara', 'Nagpur',
       'Agra', 'Dehradun', 'Mysore', 'Puducherry', 'Surat', 'Varanasi', 'Patna'] , 
    
    'United Arab Emirates' : ['Dubai',  'Sharjah', 'Abu Dhabi'], 
    
    'Singapore' : ['Singapore'], 
    
    'Sri Lanka' : ['Colombo'], 
    
    'Turkey' : ['İstanbul', 'Ankara'], 
    
    'England' : ['London', 'Manchester', 'Birmingham', 'Edinburgh', ' Lincoln'], 
    
    'Qatar' : ['Doha'], 
    
    'Philippines' : ['Makati City'], 
    
    'South Africa' : ['Cape Town','Sandton','Pretoria'], 
    
    'Brazil' : ['Brasília', 'São Paulo', 'Rio de Janeiro'], 
    
    'New Zealand' : ['Auckland', 'Wellington City'],  
    
    'Indonesia' : ['Jakarta', ' Bandung'], 
    
    'Canada' : [' Yorkton', ' Cochrane',' Consort',' Chatham-Kent'], 
    
    'USA' : [' Vernonia',' Mayfield', ' Ojo Caliente',' Vineland Station', ' Potrero', ' Princeton', ' Clatskanie', ' Fernley',
        ' Monroe', ' Santa Rosa', ' Orlando', ' Tampa Bay', ' Pensacola', ' Albany', ' Valdosta', ' Gainesville', 
        ' Savannah', ' Columbus', ' Athens',' Macon', ' Rest of Hawaii', ' Des Moines', ' Davenport',  ' Sioux City',
         ' Cedar Rapids/Iowa City', ' Dubuque',' Boise', ' Pocatello'], 
    
    'Australia' : [' Dicky Beach',' Trentham East', ' Lakes Entrance', ' Hepburn Springs', ' Inverloch',' Weirton'
              ' Tanunda', ' Middleton Beach', ' Mc Millan', ' Lorn', ' Victor Harbor', ' Huskisson', ' Armidale'
              ' Winchester Bay', ' Forrest', ' Macedon', ' Phillip Island',' Penola', ' Beechworth', 
              ' Paynesville', ' East Ballina', ' Montville', ' Flaxton', ' Lakeview', ' Balingup',
              ' Palm Cove', ' Dalton', ' Augusta', ' Waterloo']
    
   }
      
  
#-------------------------------------------------------------------

# STREAMLIT

st.header(" ZOMATO PREDICTION ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

            

with st.form("my form 1"): 
        st.write(" Average Cost of Two People")
        col1,col2,col3 = st.columns([5,2,5])
        with col1:
                    st.write (" ")
                    cuisines1 = st.selectbox(label = "CUISINES", options = option.option_cuisines, index =None)
                    rating_text1 = st.selectbox(label = "RATING TEXT", options = option.option_rating_text, index =None)
                    rating1 = st.selectbox(label = "RATING", options = option.option_rating, index =None)
        
        with col3:
                    st.write (" ")
                    country_name1 = st.selectbox("Country", options = list(option.facility_places.keys()))
                    #country_name1 = st.selectbox(label = "COUNTRY NAME", options = option.option_country_id, index =None)
                    
                    if country_name1:
                       states = option.facility_places[country_name1]
                       city_name1 = st.selectbox("State",  states)
                    else:
                       city_name1 = None

                    # Display selected values
                    if country_name1 and city_name1:
                       st.success(f"Country : {country_name1}, State : {city_name1}")
                    

                    
                       
                    submitted = st.form_submit_button(label = "PRICE")
                    st.markdown("""
                            <style>
                            div.stButton > button:first-child {
                                background-color: #009999;
                                color: white;
                                width: 100%;
                            }
                            </sytle>
                            """, unsafe_allow_html=True)   
                    
        if submitted:
                    with st.spinner("Predicting..."):
                        if not all([cuisines1,rating_text1,rating1,country_name1,city_name1]):
                            st.error ("please fill all fields")  
                        else:
                            Cuisines = option.encoded_cusines[cuisines1]
                            Rating_text = option.encoded_rating_text[rating_text1]
                            Rating = option.encoded_rating[rating1]
                            Country_id = option.encoded_country_id[country_name1]
                            City_id = option.encoded_city_id[city_name1]
                            
                            #with open('zomato_ML1.pkl', 'rb') as files:
                                #model = pickle.load(files)

                            url_ml = "https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/zomato_ML1.pkl"  # replace with your actual URL
                            response_ml = requests.get(url_ml)
                            model = pickle.loads(response_ml.content)
                           
                            user_data = np.array([[Cuisines,Rating_text,Rating,City_id,Country_id]]) 
                            raw_prediction = model.predict(user_data)
                            resale_price = round(raw_prediction[0],2)
                            st.write('## :green[AVERAGE COST : ] ', resale_price) 
if st.button("CLICK HERE"):
  test.test()
