import streamlit as st
import urllib.parse

# 1. 頁面基本設定
st.set_page_config(
    page_title="資深人才經驗求職通",
    page_icon="👴",
    layout="centered"
)

# 2. 加入高級感的 CSS 樣式（美化背景、卡片與按鈕）
st.markdown("""
    <style>
    /* 全局背景：柔和質感漸層 */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* 標題區域美化 */
    .main-title {
        color: #1e3a8a;
        font-size: 28px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #4b5563;
        font-size: 18px;
        text-align: center;
        margin-bottom: 25px;
        font-weight: 500;
    }

    /* 白色立體卡片區塊 */
    .css-card {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        border: 1px solid #e5e7eb;
    }

    /* 調整文字框與標籤字體大小 */
    .stTextArea label {
        font-size: 20px !important;
        font-weight: 700 !important;
        color: #1f2937 !important;
    }
    
    /* 大按鈕樣式 */
    .stButton>button {
        width: 100%;
        height: 3.2em;
        font-size: 20px !important;
        font-weight: bold;
        background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        transition: all 0.2s ease-in-out;
    }
    
    .stButton>button:hover {
        background: linear-gradient(90deg, #1d4ed8 0%, #1e40af 100%);
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. 頁面標題
st.markdown('<div class="main-title">👴👵 經驗傳承·經驗人才求職通</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">不用寫英文履歷，用最簡單的方式找好工作！</div>', unsafe_allow_html=True)

# 4. 主要卡片區塊
st.markdown('<div class="css-card">', unsafe_allow_html=True)
st.markdown("### 📝 1. 建立您的個人經驗卡")

exp_text = st.text_area(
    "請輸入或用手機語音輸入您的工作經驗：",
    placeholder="例如：今年 52 歲，在新山做過 15 年羅里司機與車隊調度，熟悉新加坡與新山路線，想找穩定的車隊主管或駕駛工作...",
    height=150
)

st.markdown("---")
st.markdown("### 📞 2. 選擇聯繫方式")
phone_number = st.text_input("請輸入您的 WhatsApp 手機號碼（範例：0123456789）：", value="")

if st.button("🚀 生成經驗卡並一鍵 WhatsApp 聯絡老闆"):
    if exp_text.strip() == "":
        st.warning("請先輸入您的工作經驗喔！")
    elif phone_number.strip() == "":
        st.warning("請輸入您的手機號碼！")
    else:
        # 整理文字格式
        formatted_msg = f"你好！我在【經驗人才求職通】看到您的招聘資訊。\n\n【我的個人經驗簡介】：\n{exp_text}\n\n【我的聯絡電話】：{phone_number}"
        encoded_msg = urllib.parse.quote(formatted_msg)
        
        # 預設範例老闆 WhatsApp 號碼（可替換為真實號碼）
        target_whatsapp = "60123456789" 
        wa_link = f"https://wa.me/{target_whatsapp}?text={encoded_msg}"
        
        st.success("✅ 經驗卡已成功建立！")
        st.markdown(f'''
            <a href="{wa_link}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366; color:white; padding:15px; border-radius:12px; text-align:center; font-size:22px; font-weight:bold; margin-top:10px; box-shadow:0 4px 10px rgba(37,211,102,0.3);">
                    📲 點擊這裡直接打開 WhatsApp 發送給老闆
                </div>
            </a>
        ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 頁尾小提示
st.caption("💡 提示：您可以直接使用手機鍵盤上的「語音輸入」按鈕，用講的就能自動變文字喔！")
