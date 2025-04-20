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
# AWS S3 bucket connection


# AWS RDS connection
#df = pd.read_csv('s3://your-bucket-name/folder/your_file.csv', storage_options={"key": "YOUR_KEY", "secret": "YOUR_SECRET"})

# MySQL connection info
username = 'admin'
password = 'nambukeerthi'
host = 'zomato-database-1.cdko86s0kxtq.eu-north-1.rds.amazonaws.com'          # or your host IP
port = '3306'                # default MySQL port
database = 'zomatoaws'


#-------------------------------------------------------------

def json_function(data):
  dataF=[]   
  for i in data:
    if 'restaurants' in i:
        #print(i)
      for j in i: 
        for j in i['restaurants']:
        #print(j)   
            
            #if 'price_range' in j['restaurant']: 
            price_range1 = (j['restaurant'].get('price_range', 'Key not found'))
            #if 'name' in j['restaurant']:  
            res_name1 = (j['restaurant'].get('name', 'Key not found'))  
            res_id1 = (j['restaurant']['R'].get('res_id', 'Key not found'))   
            cuisines1 = (j['restaurant'].get('cuisines', 'Key not found').replace(",", " "))
            average_cost1 = (j['restaurant'].get('average_cost_for_two', 'Key not found'))
            
            rating_text1 = (j['restaurant']['user_rating'].get('rating_text', 'Key not found'))
            rating_color1 = (j['restaurant']['user_rating'].get('rating_color', 'Key not found'))
            rating_votes1 = (j['restaurant']['user_rating'].get('votes', 'Key not found'))
            rating_aggre1 = (j['restaurant']['user_rating'].get('aggregate_rating', 'Key not found'))
            
            #for l in j['restaurant']['location']:    
            address1 = (j['restaurant']['location'].get('address', 'Key not found').replace(",", " "))  
            city1 = (j['restaurant']['location'].get('city', 'Key not found').replace(",", " "))
            country_id1 = (j['restaurant']['location'].get('country_id', 'Key not found'))
            locality_verbose1 = (j['restaurant']['location'].get('locality_verbose', 'Key not found').replace(",", " "))
            city_id1 = (j['restaurant']['location'].get('city_id', 'Key not found'))
            
            
            print_data= (res_name1, res_id1, price_range1, cuisines1,average_cost1, rating_text1, rating_color1, rating_votes1, rating_aggre1, address1, city1, city_id1, country_id1, locality_verbose1)    
            dataF.append(", ".join(map(str, print_data)))        
            # LISTED DATA INTO DATAFRAME
            
  
  return dataF


#-----------------------------------------------------

file_path1 = 'https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file1.json'        # //  df = pd.read_csv('s3://your-bucket-name/folder/your_file.csv', storage_options={"key": "YOUR_KEY", "secret": "YOUR_SECRET"})
with open(file_path1, "r") as a:
 data1 = json.load(a)
returned_data1 =  json_function(data1) 
df1 = pd.DataFrame([row.split(", ") for row in returned_data1], columns=['Restaurant_Name', 'Restaurant_ID', 'Price_range','Cuisines','Average_cost','Rating_text',
                                                               'Rating_color','Rating_votes','Rating','Address','City','City_id','Country_id','Locality'])

#-------

file_path2 = 'https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file1.json'
with open(file_path2, "r") as b:
 data2 = json.load(b)
returned_data2 =  json_function(data2)

max_columns = 14  # or whatever your intended number of columns is
dataF2_fixed = []

for row in returned_data2:
    row_values = row.split(',')
    if len(row_values) > max_columns:
        row_values = row_values[:max_columns]  # Truncate to the desired number of columns
    elif len(row_values) < max_columns:
        row_values.extend([''] * (max_columns - len(row_values)))  # Add empty values for missing columns
    dataF2_fixed.append(row_values)

# Now create the DataFrame with consistent data
df2 = pd.DataFrame(dataF2_fixed, columns=['Restaurant_Name', 'Restaurant_ID', 'Price_range', 'Cuisines', 'Average_cost',
                                           'Rating_text', 'Rating_color', 'Rating_votes', 'Rating', 'Address', 'City',
                                           'City_id', 'Country_id', 'Locality'])
#-------

file_path3 = 'https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file1.json'
with open(file_path3, "r") as c:
 data3 = json.load(c)
returned_data3=  json_function(data3)

max_columns = 14  # or whatever your intended number of columns is
dataF3_fixed = []

for row in returned_data3:
    row_values = row.split(',')
    if len(row_values) > max_columns:
        row_values = row_values[:max_columns]  # Truncate to the desired number of columns
    elif len(row_values) < max_columns:
        row_values.extend([''] * (max_columns - len(row_values)))  # Add empty values for missing columns
    dataF3_fixed.append(row_values)

# Now create the DataFrame with consistent data
df3 = pd.DataFrame(dataF3_fixed, columns=['Restaurant_Name', 'Restaurant_ID', 'Price_range', 'Cuisines', 'Average_cost',
                                           'Rating_text', 'Rating_color', 'Rating_votes', 'Rating', 'Address', 'City',
                                           'City_id', 'Country_id', 'Locality'])

#-------

file_path4 = 'https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file1.json'
with open(file_path4, "r") as d:
 data4 = json.load(d)
returned_data4 =  json_function(data4)

max_columns = 14  # or whatever your intended number of columns is
dataF4_fixed = []

for row in returned_data4:
    row_values = row.split(',')
    if len(row_values) > max_columns:
        row_values = row_values[:max_columns]  # Truncate to the desired number of columns
    elif len(row_values) < max_columns:
        row_values.extend([''] * (max_columns - len(row_values)))  # Add empty values for missing columns
    dataF4_fixed.append(row_values)

# Now create the DataFrame with consistent data
df4 = pd.DataFrame(dataF4_fixed, columns=['Restaurant_Name', 'Restaurant_ID', 'Price_range', 'Cuisines', 'Average_cost',
                                           'Rating_text', 'Rating_color', 'Rating_votes', 'Rating', 'Address', 'City',
                                           'City_id', 'Country_id', 'Locality'])

#-------

file_path5 = 'https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file1.json'
with open(file_path5, "r") as e:
 data5 = json.load(e)
returned_data5 =  json_function(data5)

max_columns = 14  # or whatever your intended number of columns is
dataF5_fixed = []

for row in returned_data5:
    row_values = row.split(',')
    if len(row_values) > max_columns:
        row_values = row_values[:max_columns]  # Truncate to the desired number of columns
    elif len(row_values) < max_columns:
        row_values.extend([''] * (max_columns - len(row_values)))  # Add empty values for missing columns
    dataF5_fixed.append(row_values)

# Now create the DataFrame with consistent data
df5 = pd.DataFrame(dataF5_fixed, columns=['Restaurant_Name', 'Restaurant_ID', 'Price_range', 'Cuisines', 'Average_cost',
                                           'Rating_text', 'Rating_color', 'Rating_votes', 'Rating', 'Address', 'City',
                                           'City_id', 'Country_id', 'Locality'])

df_concat = pd.concat([df1, df2,df3,df4,df5], ignore_index=True)
df_original = df_concat.drop_duplicates(ignore_index=True)

df_original['Cuisines'] = df_original['Cuisines'].str.replace('Continental', '', regex=True)
df_original['Rating_text'] = df_original['Rating_text'].str.replace(' Very Good', 'Very Good', regex=True)
df_original['Rating_text'] = df_original['Rating_text'].str.replace(' Excellent', 'Excellent', regex=True)
df_original['Rating_text'] = df_original['Rating_text'].str.replace(' Poor', 'Poor', regex=True)
df_original['Rating_text'] = df_original['Rating_text'].str.replace(' Average', 'Average', regex=True)
df_original['Rating_text'] = df_original['Rating_text'].str.replace(' Not rated', 'Not rated', regex=True)
df_original['Rating_text'] = df_original['Rating_text'].str.replace(' Good', 'Good', regex=True)
df_original = df_original[~df_original['Rating_text'].isin([' North Indian  Chinese  Continental  Italian', ' Continental  American  Italian  Bakery',' Chinese  North Indian',' 350',' 200',' 300',' 250'])]
df_original = df_original[~df_original['City_id'].isin([' New Delhi', ' Level 3  City Square Mall  Rajouri Garden  New Delhi',' D-15  Bhai Ji Market  Near Bishanpura Village  Sector 58  Noida',' Faridabad',
                                                        ' 31  2nd Floor  Hauz Khas Village  New Delhi',' Davenport'])]
df_original.reset_index(inplace=True)

#-------------------------------------------------------------------

# MYSQL 

# MySQL connection info

limited_df = df_original.head(100)
#engine = create_engine('mysql+pymysql://root:root@localhost:3306/practice')

#connection_variable ='mysql+pymysql://root:root@localhost:3306/practice'
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

connection_variable ='mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

try:
    with engine.begin() as conn:
        limited_df.to_sql('zomatodata', con=conn, if_exists='replace', index=False)
except Exception as e:
        st.write("Error occurred:", e)
        
        
def insert_query():        
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="practice"
    )

    cursor = conn.cursor()

    sql = "USE practice"
    
    cursor.execute(sql)

    conn.commit()
    conn.close()      
            
     
def show_table(data1,data2):
     #engine = create_engine('postgresql://username:password@localhost:5432/your_database')
     # Query the data
     
        from sqlalchemy import text

        query_2 = text("""
            SELECT * FROM zomato  
            WHERE Cuisines LIKE :cuisine 
            AND City = :city 
            ORDER BY Rating DESC 
            LIMIT 10
        """)

        params = {
            "cuisine": f"%{data1}%",
            "city": data2
        }

        table2 = pd.read_sql_query(query_2, engine, params=params)
   
     
        return table2
                          
#-------------------------------------------------------------------

# VISUALIZATION

def visual(tables):
    
        st.dataframe(tables, use_container_width=True)
        visual_data1 = tables[['Restaurant_Name', 'Rating']]  
        st.dataframe(visual_data1, use_container_width=True)
        
        fig_bar_1 = px.bar(visual_data1, x = "Restaurant_Name", y = "Rating", title = "BAR CHART",color_discrete_sequence= px.colors.sequential.haline, hover_name="Restaurant_Name")
        st.plotly_chart(fig_bar_1, theme=None, use_container_width=True)
        
        for index, row in tables.iterrows():
            st.markdown(f"#### Restaurant {index + 1}")
            st.write(f"Restaurant_Name : {row['Restaurant_Name']}")
            st.write(f"Restaurant_ID : {row['Restaurant_ID']}")
            st.write(f"Cuisines : {row['Cuisines']}")
            st.write(f"Rating_text : {row['Rating_text']}")
            st.write(f"Rating_votes : {row['Rating_votes']}")
            st.write(f"Rating : {row['Rating']}")
            st.write(f"Address : {row['Address']}")
            st.markdown("---")  # Add a separator  
    
#-------------------------------------------------------------------

# MACHINE LEARNING MODEL

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
                            
                            with open('zomato_ML.pkl', 'rb') as files:
                                model = pickle.load(files)
                            
                            user_data = np.array([[Cuisines,Rating_text,Rating,City_id,Country_id]]) 
                            raw_prediction = model.predict(user_data)
                            resale_price = round(raw_prediction[0],2)
                            st.write('## :green[AVERAGE COST : ] ', resale_price) 
if st.button("CLICK HERE"):
                              
    insert_query()
    task1 = show_table(cuisines1,city_name1)  
    visual(task1)           
                
            
          