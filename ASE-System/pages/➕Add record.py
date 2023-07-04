import os
import django
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TrafficBackend.settings")
django.setup()
from Backend.models import Numberplate
queryset = Numberplate.objects.all()
data= [[obj.pk, obj.No_plate, obj.Car_speed, obj.Location, obj.Fine_amount, obj.Status, obj.Record_date, obj.Image] for obj in queryset]

st.set_page_config(page_title="Add Record", page_icon="➕", layout="wide")

if 'number_of_rows' not in st.session_state:
    st.session_state['number_of_rows']=3
    st.session_state['type'] = 'Categorical'

increament = st.sidebar.button('show more columns ➕')
if increament:
    st.session_state.number_of_rows +=1
decrement = st.sidebar.button('show fewer columns ')
if decrement:
    st.session_state.number_of_rows -= 1

df=pd.DataFrame(data, columns=["pk", "No_plate", "Car_speed", "Location", "Fine_amount", "Status", "Record_date", "Image"])