import streamlit as st

st.header('Tossing a Coin')

# adding slider and the button to the web app
# reference the following sites for python code
# `st.slider` - https://docs.streamlit.io/develop/api-reference/widgets/st.slider
# `st.button` - https://docs.streamlit.io/develop/api-reference/widgets/st.button

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experient of {number_of_trials} trials.')

st.write('It is not a functional application yet. Under construction.')