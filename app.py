import streamlit as st

import datetime
import requests

'''
# TaxiFareModel front
'''
d = st.date_input("When would you like to take a cab ride?", datetime.date(2019, 7, 6))
t = st.time_input('Choose your time', datetime.time(8, 45))
pickup_datetime=(str(d)+ ' '+str(t))
pickup_longitude = st.number_input('Insert a pickup longitude')
pickup_latitude = st.number_input('Insert a pickup latitude')
dropoff_longitude = st.number_input('Insert a dropoff longitude')
dropoff_latitude = st.number_input('Insert a dropoff latitude')
passenger_count = st.number_input('Insert the amount of passengers')


#import API
url = 'https://taxifare.lewagon.ai/predict'
#Let's build a dictionary containing the parameters for our API...
params= {
           "pickup_datetime": [pickup_datetime],
            "pickup_longitude": [float(pickup_longitude)],
            "pickup_latitude": [float(pickup_latitude)],
            "dropoff_longitude": [float(dropoff_longitude)],
            "dropoff_latitude": [float(dropoff_latitude)],
            "passenger_count": [int(passenger_count)]
          }

response = requests.get(url, params)
prediction =response.json()['fare']

if st.button('Get estimate'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('The current amount of the expected fare is ')
    st.write(prediction)
else:
    st.write('You have not clicked yet...')
