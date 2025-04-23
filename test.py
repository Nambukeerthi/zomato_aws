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
def test():
      json_file1 = "https://zomato-aws-project-guvi.s3.eu-north-1.amazonaws.com/file1.json"
      data1 = aws_bucket_connection(json_file1)       
      returned_data1 =  json_function(data1) 
      df1 = pd.DataFrame([row.split(", ") for row in returned_data1], columns=['Restaurant_Name', 'Restaurant_ID', 'Price_range','Cuisines','Average_cost','Rating_text',
                                                                     'Rating_color','Rating_votes','Rating','Address','City','City_id','Country_id','Locality'])

   return df1
