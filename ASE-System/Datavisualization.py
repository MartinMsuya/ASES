import os
import django
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TrafficSpeed.settings")
django.setup()

import streamlit as st
from Backend.models import Numberplate
import pandas as pd
import streamlit.components.v1 as stc
import plotly.express as px
import time
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import plotly.subplots as sp
import plotly.graph_objects as go

#Query Data from django model
queryset = Numberplate.objects.all()
data= [[obj.pk, obj.No_plate, obj.Car_speed, obj.Location, obj.Fine_amount, obj.Status, obj.Record_date, obj.Image] for obj in queryset]
df = pd.DataFrame(data, columns=["pk", "No_plate", "Car_speed", "Location", "Fine_amount", "Status", "Record_date", "Image"])
df = df.sort_values('Record_date', ascending=False)
#page behaviour
st.set_page_config(page_title="Traffic Speed", page_icon="🚚", layout="wide")


col1,col2,col3 = st.columns(3)
form_search = st.form(key="search")
filterword = form_search.text_input(label="Search")
submit = form_search.form_submit_button(label="submit")

show_form_search = True

#Remove default theme
theme_plotly = None

#Load external CSS Style
with open('style_data.css') as f:
    st.markdown(f"<style>{f.read()}<style/>", unsafe_allow_html=True)


#Switcher
st.sidebar.header("Please Filter Here")
location=st.sidebar.multiselect(
    "Select the Locations:",
    options=df["Location"].unique(),
    default=df["Location"].unique()
)

status = st.sidebar.multiselect(
    "Select the Status:",
    options=df["Status"].unique(),
    default=df["Status"].unique()
)


df_selection = df.query(
    "Location == @location & Status== @status "
)


#Create homepage
def Homepage(df_search):
    #Data summeries
    total_record = int(df_selection['pk'].count())
    total_Inv = float(df_selection['Fine_amount'].sum())
    total1, total2 = st.columns(2, gap="large")
    with total1:
        st.info('Total Records', icon="➕")
        st.metric(label='sum', value=f"{total_record}")
    with total2:
        st.info('Total Fine Amount', icon="➕")
        st.metric(label='Total penalt amount', value=f"{total_Inv:,.0f}")
    st.markdown("""___""")

    #Print dataframe
    with st.expander("🧾View Record Table"):
        showdata = st.multiselect('Filter :', df_search.columns, default=["No_plate","Car_speed","Location","Fine_amount","Status","Record_date","Image"])
        st.dataframe(df_search[showdata], use_container_width=True)



#Graphs part
def Graphs():
    # Group by location and count records
    records_by_location = df_selection.groupby("Location").size().reset_index(name="Count")

    # Sort the records by location
    records_by_location = records_by_location.sort_values("Location")

    # 1. Create a line graph
    fig_line = go.Figure(data=go.Scatter(x=records_by_location["Location"], y=records_by_location["Count"], mode='lines'))

    # Customize the line graph
    fig_line.update_layout(
        title='Records by Location',
        xaxis_title='Location',
        yaxis_title='Number of Records'
    )
    #2. Inverted bar chart - Records by Month
    df_selection["Month"] = pd.to_datetime(df_selection["Record_date"]).dt.strftime("%B")
    records_by_month = df_selection.groupby("Month").size().reset_index(name="Count")
    fig_inverted_bar = px.bar(
        records_by_month,
        x="Count",
        y="Month",
        orientation="h",
        color_discrete_sequence=["#0083B8"]*len(records_by_month),
        title="Records by Month",
    )
    fig_inverted_bar.update_layout(
        xaxis_title="Number of Records",
        yaxis_title="Month",
        showlegend=False
    )
    #3. Pie chart - Records by Status
    records_by_status = df_selection.groupby("Status").size().reset_index(name="Count")
    color_mapping = {
        "Unpaid": "#FF7F0E",
        "Paid": "#1F77B4",
    }
    fig_pie = px.pie(
        records_by_status,
        values="Count",
        names="Status",
        color="Status",
        color_discrete_map=color_mapping,
        title="Records by Status",
    )
    graph_width = 300

    # Create two columns with adjusted widths
    col1, col2, _ = st.columns([graph_width, graph_width, 1])

    # Graph 1
    with col1:
        st.plotly_chart(fig_line, use_container_width=True)

    # Add a small space between the graphs
    col2.empty()

    # Graph 2
    with col2:
        st.plotly_chart(fig_inverted_bar, use_container_width=True)
    
    st.plotly_chart(fig_pie, use_container_width=False)


#Side bar
def sideBar():
    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=["Home", "Graphs"],
            icons=["Home", "📊"],
            menu_icon="cast",
            default_index=0#option,
        )

    if selected == "Home":
        show_search_form = True
    else:
        show_search_form = False

    if selected=="Home":
        try:
            if submit:
                for column in df_selection.columns:
                    df_search = df_selection[df_selection[column]== filterword]
                    if len(df_search.index)>0:
                        break
                Homepage(df_search)
            else:
                Homepage(df_selection)
        except:
            st.warning("One or more options are mandatory!")
    if selected=="Graphs":
        try:

            Graphs()
        except:
            st.warning("One or more options are mandatory!")
sideBar()



#Footer 
footer = """
    <style>

        a:hover, a:active {
        color:red;
        background-color:transparent;
        text-decoration: underline;
        }
        
        .footer {
        position: fixed;
        left: 0;
        height: 5%;
        bottom: 0;
        width: 100%;
        background-color: #243946;
        color: white;
        text-align:center;
        }
        </style>
    <div class="footer">
        <p>ASE SYSTEM </p>
        </div>
"""
st.markdown(footer, unsafe_allow_html=True)