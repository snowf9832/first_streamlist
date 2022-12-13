import streamlit
import pandas

streamlit.title('Snowflake badge 2')

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

streamlit.multiselect("Pick some fruits:", list('Fruit'))

streamlit.dataframe(my_fruit_list)
