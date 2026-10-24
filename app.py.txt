import streamlit as st
import urllib.parse

# 1. 設定頁面為手機優先的集中佈局
st.set_page_config(page_title="資深人才極簡求職通", layout="centered")

# 使用 CSS 放大字體與按鈕，適合 40-60 歲族群在手機上操作
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 20px !important;
    }
    .stButton>button {
        width: 100%;
        height: 3em;
        font-size: 22px !important;
        background-color: #25D366;
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("👵👴 經驗傳承 · 經驗人才求職通")
st.subheader("不用寫英文履歷，用最簡單的方式找好工作！")

st.divider()

# 2. 功能一：生成個人經驗卡
st.header("📝 1. 建立您的個人經驗卡")

user_input = st.text_area(
    "請輸入或用手機語音輸入您的工作經驗：", 
    placeholder="例如：我今年 52 歲，在新山做過 15 年羅里司機與車隊調度，熟悉新加坡與新山路線，想找穩定的車隊主管或駕駛工作...",
    height=150
)

phone_num = st.text_input("您的聯絡電話 / WhatsApp 號碼：", placeholder="例如：012-3456789")

if st.button("✨ 一鍵生成經驗卡"):
    if user_input and phone_num:
        st.success("✅ 經驗卡已成功生成！")
        st.markdown("### 🎴 您的專屬經驗卡")
        st.info(f"""
        **【資深求職者專長摘要】**
        * **工作經歷**：{user_input}
        * **聯絡電話**：{phone_num}
        * **平台認證**：具有豐富實務經驗、工作穩定性高
        """)
    else:
        st.warning("請填寫您的經驗與電話哦！")

st.divider()

# 3. 功能二：手機一鍵 WhatsApp 聯絡老闆
st.header("💼 2. 最新友善成熟人才職缺")

# 模擬在地職缺範例
job_title = "資深車隊組長 / 現場調度員"
company = "南馬物流有限公司 (Johor Bahru)"
salary = "RM 3,800 - RM 4,500 / 月"
boss_whatsapp = "60127778888" # 老闆的 WhatsApp 號碼

st.markdown(f"""
* **職位**：{job_title}
* **公司**：{company}
* **薪資**：{salary}
* **特點**：歡迎 40 歲以上、懂車隊管理與路況者
""")

# 自動產生 WhatsApp 連結
message = f"你好，我在資深人才求職通看到貴公司招聘【{job_title}】，我有意應徵，這是我的聯絡方式：{phone_num}。"
encoded_message = urllib.parse.quote(message)
whatsapp_url = f"https://wa.me/{boss_whatsapp}?text={encoded_message}"

# 按鈕直連 WhatsApp
st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; height:3em; font-size:20px; background-color:#25D366; color:white; border:none; border-radius:10px;">📲 直接用 WhatsApp 聯絡老闆</button></a>', unsafe_allow_html=True)