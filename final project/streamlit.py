import streamlit as st
# 강의2, 깃00
# 타이틀 적용
st.title('\:bread: Hi! bread')
# 특수 이모티콘 삽입 예시
# 이모지는 약속된 기호를 넣어여 함
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/


# Header 적용
st.header('너의 위치를 말해봐!')

# Subheader 적용
st.subheader('서울 중구 OO동')
# 검색창 구현

# 캡션 적용
st.caption('캡션을 한 번 넣어 봤습니다')

# 코드 표시
# 3개의 따옴표로 감싸서 코드를 표현
sample_code = '''
def function():
    print('hello, world')
'''
# 작성한 코드의 내용과 언어를 표시
st.code(sample_code, language="python")

# 일반 텍스트
st.text('일반적인 텍스트를 입력해 보았습니다.')

# 마크다운 문법 지원
# ** : bold
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
# 컬러코드: blue, green, orange, red, violet 이게 다임

st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:")

# LaTex 수식 지원
st.latex(r'\sqrt{x^2+y^2}=1')

# 강의3, 깃01
# DF 출력

import pandas as pd
import numpy as np


st.title('데이터프레임 튜토리얼')

# DataFrame 샘플 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)
# True하면 컨테이너 넓이를 모두 활용
# 만들어진 DF를 넣음
# DF는 interactive한 UI제공, 칼럼명을 눌러 오름차순, 내림차순을 할 수 있음
st.dataframe(dataframe, use_container_width=False)


# 테이블(static) : 만들어진 DF를 정적인 UI를 제공
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
# 단순 조회
st.table(dataframe)


# 메트릭
# delta는 양수, 음수에 따라 자동으로 색깔이 바뀜
st.metric(label="온도", value="10°C", delta="1.2°C")
st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

# 컬럼으로 영역을 나누어 표기한 경우
# 컨테이너 3등분하고, 이름 명명
# 비슷한 빵가게 출력할 때 괜찮을 듯
col1, col2, col3 = st.columns(3)
# col1 컨테이너에 원하는 데이터 입력
col1.metric(label="달러USD", value="1,228 원", delta="-12.00 원")

col2.metric(label="일본JPY(100엔)", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")

# 강의4, 깃2
from datetime import datetime as dt
import datetime

# 버튼 클릭
button = st.button('버튼에 들어갈 텍스트')
# 버튼이 클릭됐을때 실행될 내용
if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')


# 파일 다운로드 버튼
# 샘플 데이터 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# 다운로드 버튼 연결
st.download_button(
    label='CSV로 다운로드',
    data=dataframe.to_csv(), 
    file_name='sample.csv', 
    mime='text/csv'
)

# 체크 박스
agree = st.checkbox('체크박스에 들어갈 문구')
# 체크박스가 실행되면 실행될 것 지정
if agree:
    st.write('체크 박스 실행결과 :100:')

# 라디오 선택 버튼
mbti = st.radio(
    '라디오 버튼의 라벨값, 질문지',
    # 라디오 버튼의 선택지 입력
    ('ISTJ', 'ENFP', '선택지 없음'))
# 라디오 버튼이 클릭 됐을때 구현할 것들
if mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# 선택 박스
mbti = st.selectbox(
    '선택 박스의 라벨. 질문지',
    # 선택 박스의 선택지
    ('ISTJ', 'ENFP', '선택지 없음'), 
    # 선택 박스의 기본값. 첫번째가 index=0
    index=2
)
# 선택 박스의 선택결과들
if mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# 다중 선택 박스
options = st.multiselect(
    '라벨값, 질문들어갈 자리',
    # 선택지
    ['망고', '오렌지', '사과', '바나나'],
    # 기본으로 들어갈 선택지
    ['망고', '오렌지'])
# 다중 선택 박스의 결과
st.write(f'당신의 선택은: :red[{options}] 입니다.')


# 슬라이더
values = st.slider(
    # 라벨 값
    '범위의 값을 다음과 같이 지정할 수 있어요:sparkles:',
    #최소값, 최대값, (value)
    0.0, 100.0, (25.0, 75.0))
st.write('선택 범위:', values)

# 슬라이더 응용
start_time = st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    # datetime에서 년, 원, 일, 시, 분
    # 최소값
    min_value=dt(2020, 1, 1, 0, 0), 
    # 최대값
    max_value=dt(2020, 1, 7, 23, 0),
    # default
    value=dt(2020, 1, 3, 12, 0),
    # 1칸 움직일때 마다 어느정도 움직일건지 범위 지정
    # 1시간 간격으로 움직음
    # 1일 days
    step=datetime.timedelta(hours=1),
    # 날짜 출력 형식 지정
    # HH:24시간표현법으로 표현
    format="MM/DD/YY - HH:mm")
st.write("선택한 약속 시간:", start_time)


# 텍스트 입력
# 사용자로부터 입력값 받을 때 사용
title = st.text_input(
    label='가고 싶은 여행지가 있나요?', 
    # input 안에 입력값이 없을때 보여줄 제안
    placeholder='여행지를 입력해 주세요'
)
# 입력값 받고 엔터를 누르면 실행될 것
st.write(f'당신이 선택한 여행지: :violet[{title}]')

# 숫자 입력
number = st.number_input(
    label='나이를 입력해 주세요.', 
    min_value=10, 
    max_value=100, 
    # default
    value=30,
    # 움직일 단위
    step=5
)
st.write('당신이 입력하신 나이는:  ', number)


# 강의 5, 깃3

import random
st.title(':sparkles:로또 생성기:sparkles:')
# 로또 생성 파일
def generate_lotto():
    # 로또에서 중복 숫자 방지
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 46)
        lotto.add(number)
# 리스트로 변환해서 소트
    lotto = list(lotto)
    lotto.sort()
    return lotto
# 함수로 만들어진 6개 숫자 출력
st.subheader(f'행운의 번호: :green[{generate_lotto()}]')
# 생성된 시각 
st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

# 로또 생성 버튼
button = st.button('로또를 생성해 주세요!')

if button:
    # 로또 생성 5번 반복
    for i in range(1, 6):
        st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
# 강의6, 깃4
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
# plt.rcParams['font.family'] = "AppleGothic"
# Windows, 리눅스 사용자
plt.rcParams['font.family'] = "NanumGothic"
plt.rcParams['axes.unicode_minus'] = False


# DataFrame 생성
data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})

st.dataframe(data, use_container_width=True)

# matplotlib으로 그래프 그리기
fig, ax = plt.subplots()
ax.bar(data['이름'], data['나이'])
st.pyplot(fig)
# seaborn으로 그래프 그리기
barplot = sns.barplot(x='이름', y='나이', data=data, ax=ax, palette='Set2')
fig = barplot.get_figure()

st.pyplot(fig)

#############

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

st.pyplot(fig)

##### Barcode

code = np.array([
    1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

pixel_per_bar = 4
dpi = 100

fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')

st.pyplot(fig)
