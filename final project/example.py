import streamlit as st
import pandas as pd
import requests
import numpy as np
import pydeck as pdk
import folium as f
from streamlit_folium import folium_static

text_file = pd.read_csv('텍스트포함(streamlit_dataset1).csv')
map_file = pd.read_csv('경위도포함(streamlit_dataset2).csv')

## 홈페이지 배경 
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:url("https://i.imgur.com/wtY58mv.png");
            background-attachment:fixed;
            background-size:cover
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


add_bg_from_url()


 
## 메인 페이지 
def home_page():   
    st.markdown("<h1 style='font-size:50pt; text-align:center; color:blak;'>Hi Bread</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:20pt; text-align:center; color:blak;'>너의 위치를 말해봐!</h2>", unsafe_allow_html=True)
    # st.subheader(st.session_state.page)
    def check_input():
        if st.session_state.inputAddress:
            st.session_state.page = 'new_page'
        
    
    st.text_input(
        label='',  
        key='inputAddress',
        placeholder='예시)서울 중구 OO동',
        on_change=check_input
    )

## 어디에 있는 친구를 만나고 싶어? 페이지 
def new_page(address):

    inputAddress = st.session_state.inputAddress 
        
    if 'inputAddress' not in st.session_state:
        st.session_state.inputAddress = address # 초기 주소 설정 
        
    # 이전에 입력한 주소를 유지하도록 address를 inputAddress에 할당
    st.session_state.inputAddress = address
    
    st.markdown("<h2 style='font-size:20pt; text-align:center; color:black;'>어디 있는 친구를 만나고 싶어?</h2>", unsafe_allow_html=True)
    st.write(f"<h3 style='font-size:15pt; text-align:center;'> 지금 너의 현재 위치는 <{inputAddress}> 이야. 반경 범위를 클릭해줘:)", unsafe_allow_html=True)


    # 위치 데이터 설정 (소공동의 위도 및 경도)
    # 구글 맵 API 키 설정
    api_key = "구글 API"
        
    # Google Geocoding API를 사용하여 주소를 위도와 경도로 변환
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    # 주소가 올바르게 변환되면
    if data['status'] == 'OK':
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        
        # 슬라이더로 조절할 반경 초기값 설정
        default_radius = 300  # 300m로 초기화
        
        # 슬라이더로 반경 조절
        radius = st.slider('반경(m)', 50, 1000, default_radius, 50) # 최소 50, 최대 10000, 시작점 default_radius, 올라 가는 기준 50
        
        options = st.multiselect(
            '어떤 친구를 만나고 싶어?',
            ['군집0', '1', '2', '3', '4', '5', '선택 안함']
)
        st.write(options)

        # Folium을 사용하여 지도 생성
        m = f.Map(location=[lat, lng], zoom_start=15)

        # 검색 위치에 마커 추가
        f.Marker(
            [lat, lng],
            popup='Search Location',
            icon=f.Icon(color='red')
        ).add_to(m)
        
        # 검색 위치 주변 가게 마커 추가
        for index, row in map_file.iterrows():
            popup_content = f"""<div style='width: 200px;'>{row['Store']}</div>"""
            f.Marker(
                [row['Y'], row['X']],
                popup=f.Popup(popup_content, max_width=300),
                icon=f.Icon(color='blue')
            ).add_to(m)

        # 검색 위치 주변에 반경 표시
        f.Circle(
            location=[lat, lng],
            radius=radius,  # 반경 (미터)
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(m)

        # Folium 지도를 Streamlit에 표시
        folium_container = st.empty()
        with folium_container:
            folium_static(m)
            
    if st.button("메인으로 돌아가기"):
        st.session_state.page = 'home'
        st.session_state.inputAddress = ''  # 입력 주소 초기화
        st.experimental_rerun()  # 페이지 다시 그리기
            
    if st.button("새로운 친구 보러가기"):
        st.session_state.page = 'new_page1'
        st.session_state.inputAddress = ''  # 입력 주소 초기화
        st.experimental_rerun()  # 페이지 다시 그리기
      
      
def new_page1():
    st.markdown("<h2 style='font-size:20pt; text-align:center; color:black;'>어디 있는 친구를 만나고 싶어?</h2>", unsafe_allow_html=True)
      
      
  
# 페이지 렌더링
if 'page' not in st.session_state:
    st.session_state.page = 'home'
    st.session_state.inputAddress = ''  # 초기 세션 상태 설정

if 'inputAddress' not in st.session_state:
    st.session_state.inputAddress = ''
    
    
    
    
if st.session_state.page == 'home':
    print(st.session_state.page)
    home_page()
elif st.session_state.page == 'new_page':
    print(st.session_state.page)
    new_page(st.session_state.inputAddress)            
elif st.session_state.page == 'new_page1':
    print(st.session_state.page)
    new_page1()