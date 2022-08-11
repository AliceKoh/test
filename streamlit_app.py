import streamlit as st
import pandas as pd
#import numpy as np


			
result = {
	'name':'Abram',
	'age':50,
	'gender':'male',
	'alcohol':5
	}

answer = pd.DataFrame(result,index=[0])
st.write(answer)

answer = pd.DataFrame(result,index=[0])
answer.to_csv('data/answer.csv',index=False)
st.write(answer)

