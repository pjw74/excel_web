import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError


# st.set_page_config(page_title="Mapping Demo", page_icon="🌍")
#
# st.markdown("# Result Page")
# @st.cache_data
# def from_data_file(filename):
#     url = (
#             "http://raw.githubusercontent.com/streamlit/"
#             "example-data/master/hello/v1/%s" % filename
#     )
#     return pd.read_json(url)
#
#
# def display_results(summary, nun_sum):
#
#     st.sidebar.markdown("# Page 2 ❄️")
#     st.write(summary)
#     st.write(nun_sum)



import streamlit as st
from streamlit_gsheets import GSheetsConnection
# import gspread
# import json
#
# creds = json.loads(st.secrets["gsheets"]["creds"])
# gc = gspread.service_account_from_dict(creds)
# spreadsheet = gc.open('test')
#
# st.write(spreadsheet.title)

# Create a connection object.
if st.button("sheet 초기화"):
    conn = st.connection("gsheets", type=GSheetsConnection)
    conn.clear(worksheet="Orders")
    st.success("삭제되었습니다.")

if st.button("sheet 확인"):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(
        worksheet="Orders",
        ttl=1,
    )

    # df.insert({row.날짜}:[15])
    st.dataframe(df)

    # st.write("맨 끝")
    # st.write(df.iloc[-1])

    # new_row = {'날짜':'2023-12-07', '발표자':'홍길동', '참관자':'참관자1, 참관자2', '총평':'좋았습니다.', '총점':90}
    # df = df.append(new_row, ignore_index=True)

    # Print results.
    # for row in df.itertuples():
    #     st.write(f"날짜: {row.날짜} \n",
    #              f"발표자: {row.발표자} \n",
    #              f"참관자: {row.참관자}",
    #              f"총평: {row.총평} \n",
    #              f"총점: {row.총점} \n",
    #     )




