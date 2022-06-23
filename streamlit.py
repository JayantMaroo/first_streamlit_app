import streamlit
streamlit.title('My Parents new Healthy diner')

streamlit.header('Breakfast Menu')
streamlit.header('🥣 Omega 3 and Oatmeal ')
streamlit.header('🥗 Kale, spinch and Rocket smoothie')
streamlit.header('🐔 Hard boiled free range egg')
streamlit.header('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
myfruitlist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

myfruitlist = myfruitlist.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(myfruitlist.index), ['Avocado'])

streamlit.dataframe(myfruitlist)
