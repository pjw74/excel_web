import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError


st.set_page_config(page_title="Mapping Demo", page_icon="🌍")

st.markdown("# Result Page")
@st.cache_data
def from_data_file(filename):
    url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
    )
    return pd.read_json(url)


def display_results(summary, nun_sum):

    st.sidebar.markdown("# Page 2 ❄️")
    st.write(summary)
    st.write(nun_sum)