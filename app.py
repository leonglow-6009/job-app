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

    /* 放大、無邊框的亞洲熟齡男女照片樣式 */
    .header-container {{
        display: flex;
        align-items: center;
        gap: 18px;
        margin-bottom: 15px;
    }}
    .avatar-img {{
        width: 110px;
        height: 110px;
        border-radius: 12px;
        object-fit: cover;
        border: none !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.6);
    }}
    </style>
""", unsafe_allow_html=True)

# 3. 頁面標題與放大、無邊框的亞洲熟齡男女真人照片（更具經驗與成熟感）
avatar_asian_male = "https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=400&auto=format&fit=crop"
avatar_asian_female = "https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=400&auto=format&fit=crop"

st.markdown(f"""
    <div class="header-container">
        <img src="{avatar_asian_male}" class="avatar-img" alt="熟齡男職人">
        <img src="{avatar_asian_female}" class="avatar-img" alt="熟齡女職人">
    </div>
""", unsafe_allow_html=True)

st.title("👨‍🔧 經驗傳承 · 經驗人才求職通")
st.subheader("不用寫英文履歷，用最簡單的方式找好工作！")

st.write("---")

# 4. 步驟 1：輸入個人經驗
st.markdown("### 📄 1. 建立您的個人經驗卡")
st.write("請輸入或用手機語音輸入您的工作經驗：")

default_text = "例如：我今年 52 歲，在新山做過 15 年羅里司機與車隊調度，熟悉新加坡與新山路線，想找穩定的車隊主管或駕駛工作..."
user_exp = st.text_area("工作經驗與專長", value="", placeholder=default_text, height=150)

# 5. 選擇期望薪資與地區
col1, col2 = st.columns(2)
with col1:
    location = st.selectbox("希望工作地區", ["新山 (Johor Bahru)", "巴西古當 (Pasir Gudang)", "笨珍 (Pontian)", "古來 (Kulai)", "其他"])
with col2:
    expected_pay = st.text_input("期望薪資 (月薪 RM)", placeholder="例如：3500 - 4500")

# 6. 生成經驗卡與一鍵 WhatsApp 聯絡
if user_exp:
    st.markdown("### 🎴 您的經驗卡預覽：")
    
    pay_text = expected_pay if expected_pay else '面議'
    card_html = (
        '<div class="experience-card">'
        '<h4>📋 個人求職摘要</h4>'
        f'<p><b>📍 工作地區：</b>{location}</p>'
        f'<p><b>💰 期望薪資：</b>RM {pay_text}</p>'
        f'<p><b>💪 工作經驗與專長：</b><br>{user_exp}</p>'
        '</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)

    # 構造 WhatsApp 傳送文字
    msg = f"你好！我想應徵/了解工作。這是我的個人經驗卡：\n\n📍 地區：{location}\n💰 期望薪資：RM {pay_text}\n📝 經驗：{user_exp}"
    encoded_msg = urllib.parse.quote(msg)
    
    contact_phone = "60123456789"
    whatsapp_url = f"https://wa.me/{contact_phone}?text={encoded_msg}"

    st.markdown("### 📲 2. 一鍵傳送給老闆/媒合人員：")
    st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; height:3.5em; font-size:20px; font-weight:bold; background-color:#25D366; color:white; border-radius:12px; border:none; cursor:pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">💬 透過 WhatsApp 一鍵發送經驗卡</button></a>', unsafe_allow_html=True)

st.write("---")
st.caption("© 專為熟齡與在地求職者打造的高效求職平台")
