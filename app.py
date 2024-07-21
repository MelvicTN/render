import pandas as pd
import scipy.stats
import streamlit as st
import time


# these are stateful variables which are preserved as Streamlin reruns this script
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])


st.header('Tossing a Coin')


# add line plot chart
# `st.line_chart` - https://docs.streamlit.io/develop/api-reference/charts/st.line_chart
chart = st.line_chart([0.5])


# toss_coin function defined that emulates tossing a coin `n` times
# calculates the mean with every new iteration which adds to `chart`(as a new observation)

def toss_coin(n):

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean


# adding slider and the start button to the web app
# reference the following sites for python code
# `st.slider` - https://docs.streamlit.io/develop/api-reference/widgets/st.slider
# `st.button` - https://docs.streamlit.io/develop/api-reference/widgets/st.button

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')



# use two stateful variables as keys of `st.session_state` 
# The session state is preserved over new runs of the Streamlit application. 
# collecting results of experiments in the dataframe kept as `st.session_state['df_experiment_results']`
# use these variables to show the dataframe after each run of the application
# `st.dataframe` - https://docs.streamlit.io/develop/api-reference/data/st.dataframe

if start_button:
    st.write(f'Running the experient of {number_of_trials} trials.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            mean]],
                     columns=['no', 'iterations', 'mean'])
        ],
        axis=0)
    st.session_state['df_experiment_results'] = \
        st.session_state['df_experiment_results'].reset_index(drop=True)

st.write(st.session_state['df_experiment_results'])