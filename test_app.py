import streamlit as st
from PIL import Image
#import streamlit.components.v1 as components
import pandas as pd
#import numpy as np
from prognosis_app import run_prognosis_app

			
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

