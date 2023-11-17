import streamlit as st


st.title("통합과학 교재연구 및 지도 수업시연 평가지")

col1, col2, col3 = st.columns([1,1,1])

with col1:
    my_date = st.date_input('발표일시') # 디폴트 오늘
with col2:
    fname = st.text_input("발표자")
with col3:
    fname1 = st.text_input("참관자")

st.write('\n')
st.write('채점은 1(저) ~ 5(고)점까지 표시하면 됩니다.')

st.write('---')

col5, col6, col7 = st.columns([1,3,1])

with col5:
    st.write('채점항목')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('학습 내용의 적합성')

with col6:
    st.write("상세 채점 기준")
    st.write('\n')
    test2 = st.write('◆ 학습목표 설정 및 수업 실연에서 일치 여부')
    test3 = st.write(' - 학습목표의 설정은 적합한가?')
    test4 = st.write(' - 학습목표의 의미를 적절한 방법으로 전달하였는가?')
    test5 = st.write('◆ 학습자의 수준을 고려한 수업 ')
    test6 = st.write(' - 학습동기 유발이 제대로 이루어졌는가?')
    test7 = st.write(' - 학습자의 수준에 맞는 과학적 용어나 예시 등을 적절하게 사용하였는가?')

with col7:
    st.write("점수")
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.number_input('1', 1, 5,label_visibility="collapsed")
    st.number_input('2', 1, 5,label_visibility="collapsed")
    st.write('\n')
    st.number_input('3', 1, 5,label_visibility="collapsed")
    st.number_input('4', 1, 5,label_visibility="collapsed")

st.write('---')


col8, col9, col10 = st.columns([1,3,1])

with col8:
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('의사소통 능력')

with col9:
    st.write('\n')
    test2 = st.write('◆ 수업 과정에서 발문')
    test3 = st.write(' - 상황에 맞는 질문을 적절히 사용하여 학생들의 사고를 자극하였는가?')
    test4 = st.write(' - 발문이 학습 구성원 전체와 개인을 대상으로 조화를 이루면서 진행되는가?')
    test5 = st.write('◆ 목소리 크기, 발음, 몸짓, 동선 등이 수업 진행의 적절성')
    test6 = st.write(' - 목소리, 크기, 발음 등이 수업 내용을 전달하기에 적절한가?')
    test7 = st.write(' - 산만하지 않으면서 안정적인 몸짓과 동선으로 학생들의 주의를 집중시키는가?')

with col10:
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.number_input('5', 1, 5,label_visibility="collapsed")
    st.write('\n')

    st.number_input('6', 1, 5,label_visibility="collapsed")
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.number_input('7', 1, 5,label_visibility="collapsed")
    st.number_input('8', 1, 5,label_visibility="collapsed")
















st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

summary = st.text_area("총평")
st.write(summary)

all_score = st.write('합계')
