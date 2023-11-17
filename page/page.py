import streamlit as st


st.title("통합과학교재연구및 지도 수업시연 평가지")

col1,col2, col3 = st.columns([1,1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.

with col1:
    # column 1 에 담을 내용
    my_date = st.date_input('발표일시') # 디폴트 오늘
    #st.write(my_date)

with col2:
    # column 2 에 담을 내용
    fname = st.text_input("발표자: ")
    #st.title(fname)
with col3:
    # column 2 에 담을 내용
    fname1 = st.text_input("참관자: ")
    #st.title(fname1)

st.write('채점은 색이 표시된 부분에 1(저) ~ 5(고)점까지 표시하면 됩니다.')




st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

summary = st.text_area("총평")
st.write(summary)

all_score = st.write('합계')
