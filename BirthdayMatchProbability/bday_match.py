import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt
import calendar
import datetime
import random

def formula(persons):
    # math.pow(365, persons) 
    days_of_year = 365
    big_multiplication = 1
    for i in range(persons):
        big_multiplication *= days_of_year
        days_of_year -= 1 
    inverse_result = (big_multiplication/math.pow(365, persons))
    result = 1 - inverse_result
    print(result)
    return result

def get_random_calendar():
    current_year = datetime.datetime.now().year
    month = random.randint(1, 12)
     # Get the number of days in the selected month
    days_in_month = calendar.monthrange(current_year, month)[1]
    
    # Randomly select a day
    day = random.randint(1, days_in_month)
    return f"{day} {calendar.month_name[month]}"




# Example data
x_list = np.arange(0, 100)
y_list = np.linspace(0, 1, 100) 
random_date = get_random_calendar()


probability = 0.00
people = st.number_input("¿Cuántas personas hay en la habitación?", 0, 100)
if st.button("Generar Probabilidad"):
    probability = formula(people)
    random_dates = [get_random_calendar() for _ in range(people)]
    dates_list = list(random_dates)
    
    dictionary = {}
    for date in dates_list:
        if date not in dictionary:
            dictionary[date] = 1
        else:
            print(f"{date} es un cumpleaños repetido!")
            st.text(f"{date} es un cumpleaños repetido!")
    df = pd.DataFrame(
       random_dates, columns=["cumpleaños"]
    )
    st.table(df)
 
# Create a DataFrame where x_list is the index and random is the data
df = pd.DataFrame({'x': x_list, 'y': y_list})


# Base line chart
line = alt.Chart(df).mark_line().encode(
    x='x',
    y='y'
)

# Highlight specific point
point = alt.Chart(pd.DataFrame({'x': [people], 'y': [probability]})).mark_point(color='red', size=100).encode(
    x='x',
    y='y'
)

# Combine line and point
chart = line + point

st.altair_chart(chart, use_container_width=True)
 