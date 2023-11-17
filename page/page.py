import streamlit as st



st.title("통합과학교재연구및 지도 수업시연 평가지")

# 6. 날짜 입력
my_date = st.date_input('발표일시') # 디폴트 오늘
st.write(my_date)

fname = st.text_input("발표자: ")
st.title(fname)

fname1 = st.text_input("참관자: ")
st.title(fname1)

st.write('채점은 색이 표시된 부분에 1(저) ~ 5(고)점까지 표시하면 됩니다.')


message = st.text_area("메시지를 입력하세요")
st.write(message)



col1,col2 = st.columns([2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.

with col1 :
    # column 1 에 담을 내용
    st.title('here is column1')
with col2 :
    # column 2 에 담을 내용
    st.title('here is column2')
    st.checkbox('this is checkbox1 in col2 ')


# with 구문 말고 다르게 사용 가능
col1.subheader(' i am column1  subheader !! ')
col2.checkbox('this is checkbox2 in col2 ')
#=>위에 with col2: 안의 내용과 같은 기능을합니다