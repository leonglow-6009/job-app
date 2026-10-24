import streamlit as st
import urllib.parse

# 1. 設定頁面標題與佈局
st.set_page_config(page_title="資深人才職通 - 熟齡求職專區", layout="centered", page_icon="💼")

# 2. 設定背景圖片與大字體 CSS 樣式
# 使用半透明遮罩 (rgba) 確保背景圖不干擾文字閱讀
background_image_url = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1600&auto=format&fit=crop"

st.markdown(f"""
    <style>
    /* 全域背景圖片與遮罩 */
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.88), rgba(255, 255, 255, 0.88)), 
                    url('{background_image_url}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 調整字體大小與行距，適合中高齡閱讀 */
    html, body, [class*="css"] {{
        font-size: 19px !important;
        color: #1a1a1a;
    }}

    /* 主標題樣式 */
    h1 {{
        color: #1A365D;
        font-size: 2.2rem !important;
        font-weight: bold;
    }}

    /* 按鈕大字體與高對比色 */
    .stButton>button {{
        width: 100%;
        height: 3.5em;
        font-size: 20px !important;
        font-weight: bold;
        background-color: #25D366;
        color: white;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}

    /* 經驗卡預覽框樣式 */
    .experience-card {{
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #250366;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-top: 15px;
        margin-bottom: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. 頁面標題與簡介
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
    
    card_html = f"""
    <div class="experience-card">
        <h4>📋 個人求職摘要</h4>
        <p><b>📍 工作地區：</b>{location}</p>
        <p><b>💰 期望薪資：</b>RM {expected_pay if expected_pay else '面議'}</p>
        <p><b>💪 工作經驗與專長：</b><br>{user_exp}</p>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

    # 構造 WhatsApp 傳送文字
    msg = f"你好！我想應徵/了解工作。這是我的個人經驗卡：\n\n📍 地區：{location}\n💰 期望薪資：RM {expected_pay if expected_pay else '面議'}\n📝 經驗：{user_exp}"
    encoded_msg = urllib.parse.quote(msg)
    
    # 請將下方電話號碼改為您要接收對接訊息的 WhatsApp 號碼（格式：國家碼+號碼，如 60123456789）
    contact_phone = "60123456789"
    whatsapp_url = f"https://wa.me/{contact_phone}?text={encoded_msg}"

    st.markdown("### 📲 2. 一鍵傳送給老闆/媒合人員：")
    st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; height:3.5em; font-size:20px; font-weight:bold; background-color:#25D366; color:white; border-radius:12px; border:none; cursor:pointer;">💬 透過 WhatsApp 一鍵發送經驗卡</button></a>', unsafe_allow_html=True)

st.write("---")
st.caption("© 專為熟齡與在地求職者打造的高效求職平台")
