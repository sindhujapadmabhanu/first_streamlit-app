#import streamlit
# streamlit.title('Hello world')
# streamlit.header('afghj')
# streamlit.text('🥣vbnm')
# streamlit.text('🥗ghjk')
# streamlit.text('🍞yui')

import streamlit
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)



