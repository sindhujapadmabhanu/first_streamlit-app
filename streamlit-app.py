#import streamlit
# streamlit.title('Hello world')
# streamlit.header('afghj')
# streamlit.text('🥣vbnm')
# streamlit.text('🥗ghjk')
# streamlit.text('🍞yui')

import streamlit
import pandas
streamlit.title('hello')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

import requests
fruityvice_response = requests.get("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.text(fruityvice_response)
streamlit.dataframe(fruityvice_response)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
