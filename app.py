import streamlit as st
import urllib.parse

# 1. 設定頁面標題與佈局
st.set_page_config(page_title="資深人才職通 - 熟齡求職專區", layout="centered", page_icon="💼")

# 2. 設定背景圖片與深色高對比 CSS 樣式
background_image_url = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1600&auto=format&fit=crop"

st.markdown(f"""
    <style>
    /* 全域背景圖片與深色遮罩 */
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)), 
                    url('{background_image_url}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 全域字體大小與白色文字設定 */
    html, body, [class*="css"] {{
        font-size: 19px !important;
        color: #ffffff !important;
    }}

    /* 主標題顏色 */
    h1, h2, h3, h4, p, label {{
        color: #ffffff !important;
    }}

    /* 輸入框文字與背景設為清晰可讀 */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: #000000 !important;
        font-size: 18px !important;
        border-radius: 8px;
    }}
    
    /* 下拉選單文字 */
    .stSelectbox div[data-baseweb="select"] {{
        color: #000000 !important;
    }}

    /* 經驗卡預覽框樣式 */
    .experience-card {{
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #25D366;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        margin-top: 15px;
        margin-bottom: 20px;
    }}
    .experience-card *, .experience-card h4, .experience-card p {{
        color: #1a1a1a !important;
    }}

    /* 真人頭像圖片樣式 */
    .avatar-img {{
        width: 110px;
        height: 110px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #ffffff;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        margin-bottom: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. 真人頭像與頁面標題
profile_photo_url = "
