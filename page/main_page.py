
import streamlit as st
from functools import partial
import pandas as pd
import json
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

def main_page():

    #st.markdown("# Main page 🎈")
    #st.sidebar.markdown("# Main page 🎈")

    num1, num2, num3, num4 = 0,0,0,0
    st.title("통합과학 교재연구 및 지도 수업시연 평가지")

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        my_date = st.date_input('발표일시', key='my_unique_date_input_key') # 디폴트 오늘
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
        num1 += st.number_input('1', 1, 5,label_visibility="collapsed")
        num1 += st.number_input('2', 1, 5,label_visibility="collapsed")
        st.write('\n')
        st.write('\n')
        num1 += st.number_input('3', 1, 5,label_visibility="collapsed")
        num1 += st.number_input('4', 1, 5,label_visibility="collapsed")

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
        num2 += st.number_input('5', 1, 5,label_visibility="collapsed")
        st.write('\n')
        st.write('\n')

        num2 += st.number_input('6', 1, 5,label_visibility="collapsed")
        st.write('\n')
        st.write('\n')
        st.write('\n')

        num2 += st.number_input('7', 1, 5,label_visibility="collapsed")
        num2 += st.number_input('8', 1, 5,label_visibility="collapsed")

    st.write('---')



    col11, col12, col13 = st.columns([1,3,1])

    with col11:
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
        st.write('수업 운영 기술')

    with col12:
        st.write('\n')
        test2 = st.write('◆ 수업 진행 속도')
        test3 = st.write(' - 학생들의 수업을 이해하기 어려울 정도로 너무 빠르지 않는가?')
        test4 = st.write(' - 학생들의 수업에 대한 집중도를 약화시킬 정도로 너무 느리지 않은가?')
        test5 = st.write('◆ 판서의 적절성')
        test6 = st.write(' - 판서 글씨가 가독성이 좋은가?')
        test7 = st.write(' - 판서 내용이 학습 목표를 원활하게 달성할 수 있을 정도로 조직적인가?')

    with col13:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        num3 += st.number_input('9', 1, 5,label_visibility="collapsed")
        num3 += st.number_input('10', 1, 5,label_visibility="collapsed")
        st.write('\n')
        st.write('\n')
        st.write('\n')

        num3 += st.number_input('11', 1, 5,label_visibility="collapsed")
        num3 += st.number_input('12', 1, 5,label_visibility="collapsed")

    st.write('---')


    col14, col15, col16 = st.columns([1,3,1])

    with col14:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('학생 존중의 태도')

    with col15:
        st.write('\n')
        test2 = st.write('◆ 수업에 대한 열의가 있고, 학생을 존중하는 태도가 드러나는가?')
        test3 = st.write(' - 열의를 가지고 적극적으로 수업을 진행하는가?')
        st.write('\n')

        test4 = st.write(' - 자신 있게 수업을 진행하는가?')
        st.write('\n')

        test7 = st.write(' - 가르치는 태도와 언행등이 학생들 존중하는 모습인가?')

    with col16:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        num4 += st.number_input('13', 1, 5,label_visibility="collapsed")
        num4 += st.number_input('14', 1, 5,label_visibility="collapsed")
        num4 += st.number_input('15', 1, 5,label_visibility="collapsed")

    st.write('---')
    st.write('\n')
    st.write('\n')

    summary = st.text_area("총평")
    score_sum = num1+num2+num3+num4

    # 버튼 누르면 실행
    if st.button("제출"):
        if len(summary) != 0:
            with st.container():
                st.subheader("제출 결과")
                st.write("총평: ", summary)
                st.write("총점: ", score_sum)

                # Save data to a JSON file
                data = {"summary": summary, "score_sum": score_sum}
                with open('data.json', 'w') as f:
                    json.dump(data, f)
        else:
            st.warning('총평을 입력해주세요!', icon="⚠️")


if __name__ == "__main__":
    main_page()




















