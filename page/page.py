import streamlit as st


st.title("통합과학교재연구및 지도 수업시연 평가지")

col1, col2, col3 = st.columns([1,1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.

with col1:
    # column 1 에 담을 내용
    my_date = st.date_input('발표일시') # 디폴트 오늘
    #st.write(my_date)
with col2:
    # column 2 에 담을 내용
    fname = st.text_input("발표자")
    #st.title(fname)
with col3:
    # column 3 에 담을 내용
    fname1 = st.text_input("참관자")
    #st.title(fname1)


st.write('\n')
st.write('채점은 1(저) ~ 5(고)점까지 표시하면 됩니다.')

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
    st.write('학습 내용의 적합성')

with col6:
    # column 2 에 담을 내용
    st.write("상세 채점 기준")
    st.write('\n')
    test2 = st.write('◆ 학습목표 설정 및 수업 실연에서 일치 여부')
    test3 = st.write(' - 학습목표의 설정은 적합한가?')
    test4 = st.write(' - 학습목표의 의미를 적절한 방법으로 전달하였는가?')
    test5 = st.write('◆ 학습자의 수준을 고려한 수업 ')
    test6 = st.write(' - 학습동기 유발이 제대로 이루어졌는가?')
    test7 = st.write(' - 학습자의 수준에 맞는 과학적 용어나 예시 등을 적절하게 사용하였는가?')

#st.title(fname)
with col7:
    st.write("점수")
    st.write('\n')
    st.write('\n')
    st.write('\n')

# st.number_input('1', 1, 5,label_visibility="collapsed")
    st.number_input('2', 1, 5,label_visibility="collapsed")
    st.number_input('3', 1, 5,label_visibility="collapsed")
    # st.number_input('4', 1, 5,label_visibility="collapsed")
    st.write('\n')

    st.number_input('5', 1, 5,label_visibility="collapsed")
    st.number_input('6', 1, 5,label_visibility="collapsed")

    #st.title(fname1)

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

summary = st.text_area("총평")
st.write(summary)

all_score = st.write('합계')
