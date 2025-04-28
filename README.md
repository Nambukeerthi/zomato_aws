<h1> Zomato_Cost_Prediction_AWS_Deployment </h1>


<h1 align="center">
  <br>
  <a href=""><img src="" alt="" width="400"></a>
  <br>
 
  <br>
</h1>


<p align="center">
  <a href="#Introduction"></a> 
  <a href="#Technologies Applied"></a>  
</p>

Video Link: [Linked-IN Video](https://www.linkedin.com/posts/nambu-keerthi-r-9b8839283_project-name-zomato-cost-prediction-aws-activity-7322432538038149120-d3tT?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEUARVwBltI0ri4ApeK7YzcbHxGViaHfWEM)

Portfolio: [Nambu Keerthi](https://portfolio-b5zieg8xn5nhwau5b4bhp8.streamlit.app/)

## Introduction 
This project aims to develop machine learning models for the zomato like business:

1. Average Cost of Two People Prediction Model – To accurately forecast average cost of two.
2. Random Forest Model – To find cost effectively.

Manually predicting cost is time-consuming and may lead to correct decisions. These models will automate the process, improving accuracy and efficiency. These models will help in making better cost decisions and efficient cost management. 

**Domain** : *Food* 

## Technologies Applied
* Python
* Streamlit
* Machine Learning Model
* AWS RDS (mysql)
* AWS S3
* AWS EC2


## Project Setup
1. Firstly install all the required extensions in the requirements.txt
```
pip install -r requirements.txt
```

2. Second get the Data from the Data source and Load the data for Data cleaning and Pre Processing. Then finding the outliers for removing then make it visible the dataset columns by using matplotlib and seaborn.
```
import seaborn as sns
import matplotlib.pyplot as plt

```

3. Split the dataset as well as  train and test data for creating ML models. Save the models in ".pkl" file 
```
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

```
  
4. Last we can run the streamlit app
```
streamlit run zomato_aws_app.py
```

## AWS 

**AWS RDS**
```
host='zomato-database-1.cdko86s0kxtq.eu-north-1.rds.amazonaws.com',
        user='admin',
        password='nambukeerthi',
        database='zomatoaws',
        port= 3306
```
**AWS S3**
```
        url = file  # Replace with your JSON URL
        
        response = requests.get(url)
        
        data_json = response.json()  # Parses JSON into Python dict
        
        return data_json
```

**AWS EC2**
OS: Ubunto
```
sudo apt update

sudo apt-get update

sudo apt upgrade -y

sudo apt install git curl unzip tar make sudo vim wget -y

git clone "Your-repository"

sudo apt install python3-pip

pip3 install -r requirements.txt (or) pip install -r <your-package> --break-system-packages

#Temporary running
python3 -m streamlit run app.py

#Permanent running
nohup python3 -m streamlit run app.py

Note: Streamlit runs on this port: 8501

```


## Project Methodology

**Price Prediction**

1. Click the "Price" button after fill all selection boxes. Fill in the following required informations.

2. The app will display the cost price based on the provided information.

**Visualization**

3. Click the "click here" button. Dataframes and Barchart and hotel's details will shown.
