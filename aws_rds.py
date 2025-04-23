import json
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu           # STREAMLIT
import pymysql                                          # AWS RDS PYTHON BASED MYSQL CONNECTION
from mysql.connector import Error                       # LOCAL MYSQL CONECTION
import plotly.express as px                             # CHART VIZUALISATION
import boto3                                            # AWS S3 BUKET CONECTION AND READ
from sqlite3 import Connection                          # SQL CONNECTION
from sqlalchemy import create_engine                    # MYSQL QUERY READ PYTHON BASED
import pickle                                           # MACHINE LEARNING MODEL PICKLE FILE(.PKL)
import requests
#-----------------------------------------------------------

# AWS S3 BUCKET CONNECTION


def aws_bucket_connection(file):
    
        url = file  # Replace with your JSON URL
        
        response = requests.get(url)
        
        data_json = response.json()  # Parses JSON into Python dict
        
        return data_json 

#-------------------------------------------------------------


#  BASIC CODING

def json_function(data):
  dataF=[]   
  for i in data:
    if 'restaurants' in i:
        
      for j in i: 
        for j in i['restaurants']:
           
            
            
            price_range1 = (j['restaurant'].get('price_range', 'Key not found'))
            
            res_name1 = (j['restaurant'].get('name', 'Key not found'))  
            res_id1 = (j['restaurant']['R'].get('res_id', 'Key not found'))   
            cuisines1 = (j['restaurant'].get('cuisines', 'Key not found').replace(",", " "))
            average_cost1 = (j['restaurant'].get('average_cost_for_two', 'Key not found'))
            
            rating_text1 = (j['restaurant']['user_rating'].get('rating_text', 'Key not found'))
            rating_color1 = (j['restaurant']['user_rating'].get('rating_color', 'Key not found'))
            rating_votes1 = (j['restaurant']['user_rating'].get('votes', 'Key not found'))
            rating_aggre1 = (j['restaurant']['user_rating'].get('aggregate_rating', 'Key not found'))
            
               
            address1 = (j['restaurant']['location'].get('address', 'Key not found').replace(",", " "))  
            city1 = (j['restaurant']['location'].get('city', 'Key not found').replace(",", " "))
            country_id1 = (j['restaurant']['location'].get('country_id', 'Key not found'))
            locality_verbose1 = (j['restaurant']['location'].get('locality_verbose', 'Key not found').replace(",", " "))
            city_id1 = (j['restaurant']['location'].get('city_id', 'Key not found'))
            
              
            print_data= (res_name1, res_id1, price_range1, cuisines1,average_cost1, rating_text1, rating_color1, rating_votes1, rating_aggre1, address1, city1, city_id1, country_id1, locality_verbose1)    
            dataF.append(", ".join(map(str, print_data)))        
            
            
  
  return dataF


#-----------------------------------------------------


# DATA EXTRACTION 
def data_extraction():
json_file1 = "https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file1.json"
data1 = aws_bucket_connection(json_file1)       
returned_data1 =  json_function(data1) 
df1 = pd.DataFrame([row.split(", ") for row in returned_data1], columns=['Restaurant_Name', 'Restaurant_ID', 'Price_range','Cuisines','Average_cost','Rating_text',
                                                               'Rating_color','Rating_votes','Rating','Address','City','City_id','Country_id','Locality'])

#-------

json_file2 = "https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file2.json"
data2 = aws_bucket_connection(json_file2) 
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

json_file3 = "https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file3.json"
data3 = aws_bucket_connection(json_file3) 
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

json_file4 = "https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file4.json"
data4 = aws_bucket_connection(json_file4)
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

json_file5 = "https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file5.json"
data5 = aws_bucket_connection(json_file5)
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


#  MYSQL / AWS RDS CONNECTION

limited_df = df_original.head(100)

engine = create_engine('mysql+pymysql://admin:nambukeerthi@zomato-database-1.cdko86s0kxtq.eu-north-1.rds.amazonaws.com:3306/zomatoaws')

connection_variable ='mysql+pymysql://admin:nambukeerthi@zomato-database-1.cdko86s0kxtq.eu-north-1.rds.amazonaws.com:3306/zomatoaws'
try:
    with engine.begin() as conn:
        limited_df.to_sql('zomatodata', con=conn, if_exists='replace', index=False)
except Exception as e:
        st.write("Error occurred:", e)
        
        
def insert_query():    
        
    conn = pymysql.connect(
        host='zomato-database-1.cdko86s0kxtq.eu-north-1.rds.amazonaws.com',
        user='admin',
        password='nambukeerthi',
        database='zomatoaws',
        port='3306'
    )

    cursor = conn.cursor()

    sql = "USE zomatoaws;"
    
    cursor.execute(sql)

    conn.commit()
    conn.close()      
            
     
def show_table(data1,data2):
    
     
        from sqlalchemy import text

        query_2 = text("""
            SELECT * FROM zomatodata  
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
            st.markdown("---")    

