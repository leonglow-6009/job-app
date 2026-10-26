import streamlit as st
import urllib.parse
import base64
import os

# 1. 設定頁面標題與佈局
st.set_page_config(page_title="資深人才職通 - 熟齡求職專區", layout="centered", page_icon="💼")

# 2. 全域背景與樣式
bg_url = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1600&auto=format&fit=crop"

st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.72), rgba(0, 0, 0, 0.72)), url('{bg_url}');
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
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.85);
    }}
    </style>
""", unsafe_allow_html=True)

# 3. 頂部職人照與標題
male_img = "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=400&auto=format&fit=crop"
female_img = "https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=400&auto=format&fit=crop"

st.markdown(f"""
    <div class="header-avatars">
        <img src="{male_img}" class="avatar-img" alt="男職人">
        <img src="{female_img}" class="avatar-img" alt="女職人">
        <div>
            <h1 style="margin: 0; padding: 0; font-size: 2.1rem !important; line-height: 1.2;">經驗傳承<br>經驗人才求職通</h1>
        </div>
    </div>
""", unsafe_allow_html=True)

st.subheader("不用寫英文履歷，專為 40-60 歲新馬在地打造！")
st.write("---")

tab1, tab2 = st.tabs(["🔥 JB 熱門職缺專區", "📄 我要發布求職卡"])
admin_phone = "60123456789"

# 智慧讀取本地 QR Code 圖片的函數
def render_qr():
    filenames = ["1000086716.png", "1000086716.JPG", "1000086716.jpg", "qr.png"]
    target = next((f for f in filenames if os.path.exists(f)), None)
    
    if target:
        with open(target, "rb") as img:
            b64_str = base64.b64encode(img.read()).decode()
        st.markdown(f"""
            <div style="text-align: center; margin: 15px 0;">
                <img src="data:image/png;base64,{b64_str}" style="width: 260px; max-width: 80%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);" alt="QR">
                <p style="color: #8A6D3B; font-size: 15px; margin-top: 8px;">DuitNow / Touch 'n Go RM 1 轉賬碼 (U BREAD)</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ 找不到 QR Code 圖片檔案！請確認 GitHub 根目錄有名稱為 1000086716.png 的圖片檔案（請確保上傳的是圖片，非 PDF）。")

with tab1:
    st.markdown("### 🏢 新山在地嚴選職缺（RM 1 微型解鎖）")
    st.write("精選真心徵人的在地企業，只需 **RM 1** 即可獲取老闆直接 WhatsApp 號碼：")

    jobs = [
        {"title": "🚛 资深罗里司机 (3吨/5吨)", "company": "新山某大型物流運輸公司", "location": "Taman Daya / 巴西古当", "pay": "RM 3,800 - RM 5,000", "desc": "需持有 GDL 驾照，熟悉新山与新加坡路线。欢迎责任心强的大哥應徵！"},
        {"title": "📦 仓库理货員 / 包装员", "company": "Mount Austin 食品批发仓", "location": "Taman Mount Austin", "pay": "RM 2,600 - RM 3,300", "desc": "工作单纯稳定，负责货物点算与简单包装。环境舒适，欢迎细心稳重的熟齡男女。"},
        {"title": "🍳 餐厅帮厨 / 后勤杂务", "company": "JB 传统美食餐馆", "location": "Kulai (古来)", "pay": "RM 2,800 - RM 3,600", "desc": "协助厨师备料、厨房清洁与日常杂务。包工作餐，老板好沟通，注重团队和谐。"},
        {"title": "📋 办事处行政/仓管文员", "company": "五金机械贸易行", "location": "Plentong / 柔佛再也", "pay": "RM 3,000 - RM 4,000", "desc": "负责接听电话、简单单據记录与出货安排。会基础电脑操作及简单中巫文即可。"}
    ]

    for job in jobs:
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
            st.markdown("""
                <div class="unlock-box">
                    <h4>💡 解鎖步驟：</h4>
                    <p>1. 請用 Touch 'n Go eWallet / 銀行 App 掃描下方 <b>DuitNow QR</b> 轉賬 <b>RM 1.00</b> (戶口：U BREAD)。</p>
                    <p>2. 轉賬完成後截圖，點擊下方按鈕將截圖傳給管理員，小編會立刻把老闆直接電話發給您！</p>
                </div>
            """, unsafe_allow_html=True)

            render_qr()

            msg = f"你好！我已轉賬 RM 1 解鎖職缺：【{job['title']}】以及轉賬截圖，請發給我老闆的聯絡電話，謝謝！"
            url = f"https://wa.me/{admin_phone}?text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{url}" target="_blank"><button style="width:100%; height:3em; font-size:18px; font-weight:bold; background-color:#25D366; color:white; border-radius:10px; border:none; cursor:pointer; margin-top:10px;">📲 我已轉賬，點此發送截圖領取電話</button></a>', unsafe_allow_html=True)

with tab2:
    st.markdown("### 📄 建立您的專屬經驗卡")
    user_exp = st.text_area("請輸入您的工作經驗與專長", value="", placeholder="例如：我今年 52 歲，在新山做過 15 年羅里司機...", height=150)
    
    col1, col2 = st.columns(2)
    with col1:
        loc = st.selectbox("希望工作地區", ["新山 (Johor Bahru)", "巴西古当 (Pasir Gudang)", "古来 (Kulai)", "柔佛再也 (Johor Jaya)", "其他"])
    with col2:
        pay = st.text_input("期望薪資 (月薪 RM)", placeholder="例如：3500 - 4500")

    if user_exp:
        st.markdown(f"""
            <div class="experience-card">
                <h4>📋 個人求職摘要</h4>
                <p><b>📍 工作地區：</b>{loc}</p>
                <p><b>💰 期望薪資：</b>RM {pay if pay else '面議'}</p>
                <p><b>💪 工作經驗：</b><br>{user_exp}</p>
            </div>
        """, unsafe_allow_html=True)
        
        m = f"你好！我想找工作。地區：{loc}，期望薪資：RM {pay if pay else '面議'}，經驗：{user_exp}"
        u = f"https://wa.me/{admin_phone}?text={urllib.parse.quote(m)}"
        st.markdown(f'<a href="{u}" target="_blank"><button style="width:100%; height:3.5em; font-size:20px; font-weight:bold; background-color:#25D366; color:white; border-radius:12px; border:none; cursor:pointer;">💬 透過 WhatsApp 發送我的經驗卡</button></a>', unsafe_allow_html=True)

st.write("---")
st.caption("© 專為 40-60 歲熟齡與在地求職者打造的高效求職平台")
