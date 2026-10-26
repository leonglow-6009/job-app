import streamlit as st
import urllib.parse

# 1. 設定頁面標題與佈局
st.set_page_config(page_title="資深人才職通 - 熟齡求職專區", layout="centered", page_icon="💼")

# 2. 背景圖片與 CSS 樣式
background_image_url = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1600&auto=format&fit=crop"

st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.72), rgba(0, 0, 0, 0.72)), 
                    url('{background_image_url}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    html, body, [class*="css"] {{
        font-size: 19px !important;
        color: #ffffff !important;
    }}

    h1, h2, h3, h4, p, label {{
        color: #ffffff !important;
    }}

    .stTextInput>div>div>input, .stTextArea>div>div>textarea {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: #000000 !important;
        font-size: 18px !important;
        border-radius: 8px;
    }}
    
    .stSelectbox div[data-baseweb="select"] {{
        color: #000000 !important;
    }}

    .job-card, .experience-card {{
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #25D366;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        margin-top: 15px;
        margin-bottom: 15px;
    }}
    .job-card *, .job-card h4, .job-card p,
    .experience-card *, .experience-card h4, .experience-card p {{
        color: #1a1a1a !important;
    }}

    .unlock-box {{
        background-color: #FFF9E6;
        border: 2px dashed #E6A23C;
        padding: 18px;
        border-radius: 12px;
        margin-top: 10px;
        margin-bottom: 15px;
    }}
    .unlock-box p, .unlock-box h4 {{
        color: #8A6D3B !important;
    }}

    .header-avatars {{
        display: flex;
        align-items: center;
        gap: 18px;
        margin-bottom: 18px;
        flex-wrap: wrap;
    }}
    .avatar-img {{
        width: 120px;
        height: 120px;
        border-radius: 20px;
        object-fit: cover;
        border: none !important;
        outline: none !important;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.85);
    }}
    </style>
""", unsafe_allow_html=True)

# 3. 頁面標頭與 3D 浮動熟齡職人照
avatar_male = "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=400&auto=format&fit=crop"
avatar_female = "https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=400&auto=format&fit=crop"

st.markdown(f"""
    <div class="header-avatars">
        <img src="{avatar_male}" class="avatar-img" alt="資深男職人">
        <img src="{avatar_female}" class="avatar-img" alt="資深女職人">
        <div>
            <h1 style="margin: 0; padding: 0; font-size: 2.1rem !important; line-height: 1.2;">經驗傳承<br>經驗人才求職通</h1>
        </div>
    </div>
""", unsafe_allow_html=True)

st.subheader("不用寫英文履歷，專為 40-60 歲新馬在地打造！")

st.write("---")

tab1, tab2 = st.tabs(["🔥 JB 熱門職缺專區", "📄 我要發布求職卡"])

admin_phone = "60123456789"  # 您的 WhatsApp 號碼

# ----------------- 分頁 1：職缺專區 -----------------
with tab1:
    st.markdown("### 🏢 新山在地嚴選職缺（RM 1 微型解鎖）")
    st.write("精選真心徵人的在地企業，只需 **RM 1** 即可獲取老闆直接 WhatsApp 號碼：")

    jb_jobs = [
        {
            "id": "job1",
            "title": "🚛 资深罗里司机 (3吨/5吨)",
            "company": "新山某大型物流運輸公司",
            "location": "Taman Daya / 巴西古当",
            "pay": "RM 3,800 - RM 5,000",
            "desc": "需持有 GDL 驾照，熟悉新山与新加坡路线。欢迎责任心强、经验丰富的大哥應徵！"
        },
        {
            "id": "job2",
            "title": "📦 仓库理货員 / 包装员",
            "company": "Mount Austin 食品批发仓",
            "location": "Taman Mount Austin",
            "pay": "RM 2,600 - RM 3,300",
            "desc": "工作单纯稳定，负责货物点算与简单包装。环境舒适，欢迎细心稳重的熟齡男女。"
        },
        {
            "id": "job3",
            "title": "🍳 餐厅帮厨 / 后勤杂务",
            "company": "JB 传统美食餐馆",
            "location": "Kulai (古来)",
            "pay": "RM 2,800 - RM 3,600",
            "desc": "协助厨师备料、厨房清洁与日常杂务。包工作餐，老板好沟通，注重团队和谐。"
        },
        {
            "id": "job4",
            "title": "📋 办事处行政/仓管文员",
            "company": "五金机械贸易行",
            "location": "Plentong / 柔佛再也",
            "pay": "RM 3,000 - RM 4,000",
            "desc": "负责接听电话、简单单据记录与出货安排。会基础电脑操作及简单中巫文即可。"
        }
    ]

    # 直接穩定的 DuitNow QR 圖片連結
    qr_img_url = "https://i.imgur.com/39316uB.png"  # 或 GitHub 原始圖片完整連結

    for job in jb_jobs:
        st.markdown(f"""
            <div class="job-card">
                <h4>{job['title']}</h4>
                <p><b>🏢 公司：</b>{job['company']}</p>
                <p><b>📍 地點：</b>{job['location']}</p>
                <p><b>💰 薪資：</b>{job['pay']}</p>
                <p><b>📝 工作內容：</b>{job['desc']}</p>
                <p><b>📞 聯絡電話：</b><span style="color: #E6A23C; font-weight: bold;">🔒 已加密（付 RM 1 解鎖）</span></p>
            </div>
        """, unsafe_allow_html=True)

        with st.expander(f"🔓 點擊此處支付 RM 1 解鎖【{job['title']}】的聯絡電話"):
            st.markdown(f"""
                <div class="unlock-box">
                    <h4>💡 解鎖步驟：</h4>
                    <p>1. 請用 Touch 'n Go eWallet / 銀行 App 掃描下方 <b>DuitNow QR</b> 轉賬 <b>RM 1.00</b> (戶口：U BREAD)。</p>
                    <p>2. 轉賬完成後截圖，點擊下方按鈕將截圖傳給管理員，小編會立刻把老闆直接電話發給您！</p>
                </div>
            """, unsafe_allow_html=True)

            # 使用 Streamlit 內建 st.image 以保證 100% 成功加載
            st.image("https://raw.githubusercontent.com/leonglow-6009/job-app/main/1000086716.png", caption="DuitNow / Touch 'n Go RM 1 轉賬碼 (U BREAD)", width=280)

            receipt_msg = f"你好！我已轉賬 RM 1 解鎖職缺：【{job['title']}】，這是我的轉賬截圖，請發給我老闆的聯絡電話，謝謝！"
            encoded_receipt_msg = urllib.parse.quote(receipt_msg)
            receipt_url = f"https://wa.me/{admin_phone}?text={encoded_receipt_msg}"

            st.markdown(f'<a href="{receipt_url}" target="_blank"><button style="width:100%; height:3em; font-size:18px; font-weight:bold; background-color:#25D366; color:white; border-radius:10px; border:none; cursor:pointer; margin-top:10px;">📲 我已轉賬，點此發送截圖領取電話</button></a>', unsafe_allow_html=True)

        st.write("")

# ----------------- 分頁 2：建立個人求職卡 -----------------
with tab2:
    st.markdown("### 📄 建立您的專屬經驗卡")
    st.write("如果您找不到合適的工作，可以自己填寫專長，免費發布經驗卡：")

    default_text = "例如：我今年 52 歲，在新山做過 15 年羅里司機與車隊調度，熟悉新加坡與新山路線，想找穩定的車隊主管或駕駛工作..."
    user_exp = st.text_area("請輸入您的工作經驗與專長", value="", placeholder=default_text, height=150)

    col1, col2 = st.columns(2)
    with col1:
        location = st.selectbox("希望工作地區", ["新山 (Johor Bahru)", "巴西古當 (Pasir Gudang)", "古來 (Kulai)", "柔佛再也 (Johor Jaya)", "其他"])
    with col2:
        expected_pay = st.text_input("期望薪資 (月薪 RM)", placeholder="例如：3500 - 4500")

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

        msg = f"你好！我想應徵/找工作。這是我的個人經驗卡：\n\n📍 地區：{location}\n💰 期望薪資：RM {pay_text}\n📝 經驗：{user_exp}"
        encoded_msg = urllib.parse.quote(msg)
        whatsapp_url = f"https://wa.me/{admin_phone}?text={encoded_msg}"

        st.markdown("### 📲 一鍵發送給媒合人員：")
        st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; height:3.5em; font-size:20px; font-weight:bold; background-color:#25D366; color:white; border-radius:12px; border:none; cursor:pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">💬 透過 WhatsApp 免費發送我的經驗卡</button></a>', unsafe_allow_html=True)

st.write("---")
st.caption("© 專為 40-60 歲熟齡與在地求職者打造的高效求職平台")
