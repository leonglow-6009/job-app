import streamlit as st
import urllib.parse

# 1. 設定頁面標題與佈局
st.set_page_config(page_title="新山資深人才職通 - 熟齡求職與在地招募", layout="centered", page_icon="💼")

# 2. 設定背景圖片與深色高對比 CSS 樣式
background_image_url = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1600&auto=format&fit=crop"

st.markdown(f"""
    <style>
    /* 全域背景圖片與深色遮罩 */
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
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

    /* 經驗卡與職缺卡預覽框樣式 */
    .experience-card, .job-item-card {{
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #25D366;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        margin-top: 15px;
        margin-bottom: 20px;
    }}
    .experience-card *, .experience-card h4, .experience-card p,
    .job-item-card *, .job-item-card h4, .job-item-card p {{
        color: #1a1a1a !important;
    }}

    /* 頂部真人形象圖樣式：超大尺寸、無邊框、3D立體浮動陰影 */
    .header-avatars {{
        display: flex;
        align-items: center;
        gap: 18px;
        margin-bottom: 18px;
        flex-wrap: wrap;
    }}
    .avatar-img {{
        width: 130px;
        height: 130px;
        border-radius: 20px;
        object-fit: cover;
        border: none !important;
        outline: none !important;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.2) inset;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. 頁面標題與 50-60 歲熟齡亞洲/馬來西亞在地職人專業照
avatar_male = "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=400&auto=format&fit=crop"
avatar_female = "https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=400&auto=format&fit=crop"

st.markdown(f"""
    <div class="header-avatars">
        <img src="{avatar_male}" class="avatar-img" alt="資深男職人">
        <img src="{avatar_female}" class="avatar-img" alt="資深女職人">
        <div>
            <h1 style="margin: 0; padding: 0; font-size: 2.1rem !important; line-height: 1.2;">新山熟齡<br>求職與招募通</h1>
        </div>
    </div>
""", unsafe_allow_html=True)

st.subheader("免寫英文履歷，專為 40-60 歲在地朋友打造！")

st.write("---")

# 4. 使用分頁切換：【我要找工作】 vs 【瀏覽新山最新職缺】
tab1, tab2 = st.tabs(["👤 我要找工作 (製作經驗卡)", "🏢 瀏覽新山最新職缺 (老闆招募牆)"])

with tab1:
    st.markdown("### 📄 1. 建立您的個人經驗卡")
    st.write("請輸入或用手機語音輸入您的工作經驗：")

    default_text = "例如：我今年 52 歲，在新山做過 15 年羅里司機與車隊調度，熟悉新加坡與新山路線，想找穩定的車隊主管或駕駛工作..."
    user_exp = st.text_area("工作經驗與專長", value="", placeholder=default_text, height=150, key="user_exp_input")

    col1, col2 = st.columns(2)
    with col1:
        location = st.selectbox("希望工作地區", ["新山 (Johor Bahru)", "巴西古当 (Pasir Gudang)", "笨珍 (Pontian)", "古来 (Kulai)", "士姑来 (Skudai)"])
    with col2:
        expected_pay = st.text_input("期望薪資 (月薪 RM)", placeholder="例如：3500 - 4500", key="pay_input")

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

        msg = f"你好！我想應徵/了解工作。這是我的個人經驗卡：\n\n📍 地區：{location}\n💰 期望薪資：RM {pay_text}\n📝 經驗：{user_exp}"
        encoded_msg = urllib.parse.quote(msg)
        contact_phone = "60123456789"  # 您的接收 WhatsApp 號碼
        whatsapp_url = f"https://wa.me/{contact_phone}?text={encoded_msg}"

        st.markdown("### 📲 2. 一鍵傳送給老闆/媒合人員：")
        st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; height:3.5em; font-size:20px; font-weight:bold; background-color:#25D366; color:white; border-radius:12px; border:none; cursor:pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">💬 透過 WhatsApp 一鍵發送經驗卡</button></a>', unsafe_allow_html=True)

with tab2:
    st.markdown("### 🏢 新山在地精選職缺（適合 40-60 歲）")
    st.write("以下為您精選目前新山地區熱門、歡迎資深經驗人才的真實職缺，點擊即可直接透過 WhatsApp 聯繫老闆應徵：")

    # 這裡您可以自由新增、修改新山的真實職缺清單！
    jb_jobs = [
        {
            "title": "🚚 3噸客貨車 / 羅里司機 (新山區)",
            "company": "新山某大型物流運輸公司",
            "location": "新山 / 巴西古當",
            "salary": "RM 3,500 - RM 4,800",
            "desc": "需有 GDL 駕照，熟悉新山與新加坡路況，工作穩定，歡迎 40-55 歲熟練司機。",
            "phone": "60123456789"
        },
        {
            "title": "📦 倉庫理貨員 / 點貨主管",
            "company": "Taman Mount Austin 批發倉庫",
            "location": "Mount Austin, JB",
            "salary": "RM 3,000 - RM 3,800",
            "desc": "負責日常貨品點收、分類與倉庫出貨管理。工作單純，細心負責即可。",
            "phone": "60123456789"
        },
        {
            "title": "🧹 商用大樓 / 廠房清潔督導",
            "company": "JB 專業物業清潔管理",
            "location": "Skudai / Senai",
            "salary": "RM 2,800 - RM 3,500",
            "desc": "帶領小團隊負責商業區或工廠日常清潔維護，有相關管理經驗者佳。",
            "phone": "60123456789"
        },
        {
            "title": "🧑‍🍳 傳統餅家 / 食品廠幫廚與包裝",
            "company": "JB 知名傳統食品廠",
            "location": "Johor Jaya",
            "salary": "RM 2,600 - RM 3,200",
            "desc": "負責食品簡單加工、包裝與品質檢查，環境乾淨，歡迎手腳俐落的中高齡大哥大姐。",
            "phone": "60123456789"
        }
    ]

    for job in jb_jobs:
        job_msg = f"你好！我对这个职位很感兴趣：\n\n📌 職位：{job['title']}\n🏢 公司：{job['company']}\n📍 地點：{job['location']}\n💰 薪資：{job['salary']}"
        encoded_job_msg = urllib.parse.quote(job_msg)
        job_wa_url = f"https://wa.me/{job['phone']}?text={encoded_job_msg}"

        job_card_html = f"""
        <div class="job-item-card">
            <h4>{job['title']}</h4>
            <p><b>🏢 公司：</b>{job['company']}</p>
            <p><b>📍 地點：</b>{job['location']} | <b>💰 薪資：</b>{job['salary']}</p>
            <p><b>📝 工作內容：</b>{job['desc']}</p>
            <a href="{job_wa_url}" target="_blank">
                <button style="width:100%; height:2.8em; font-size:16px; font-weight:bold; background-color:#25D366; color:white; border-radius:8px; border:none; cursor:pointer; margin-top:8px;">
                    💬 WhatsApp 立即應徵此職缺
                </button>
            </a>
        </div>
        """
        st.markdown(job_card_html, unsafe_allow_html=True)

st.write("---")
st.caption("© 專為熟齡與在地求職者打造的高效求職平台 | 助您輕鬆對接新山好工作")
