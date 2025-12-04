import streamlit as st

# --- 網頁設定 ---
st.set_page_config(page_title="醫師團課揪團生成器", page_icon="👨‍⚕️")

# --- 標題區 ---
st.title("醫師團課揪團生成器 (AI Powered)")
st.markdown("只要填寫課程資訊，就能一鍵生成精美的 LINE/FB 揪團文案！")

# --- 輸入區 ---
col1, col2 = st.columns(2)
with col1:
    course_name = st.text_input("課程名稱", placeholder="例如：進階超音波實戰工作坊")
    original_price = st.number_input("原價學費 (元)", min_value=0)
with col2:
    group_price = st.number_input("團報優惠價 (元)", min_value=0)

# 計算折扣
if original_price > 0 and group_price > 0:
    discount = original_price - group_price
    st.info(f"💡 這樣每人可以省下：${discount} 元")

course_highlights = st.text_area("課程亮點 / 學分資訊", placeholder="例如：可申請急救加護學分、手把手教學、名額有限...")
course_link = st.text_input("報名連結", placeholder="https://...")

# --- 按鈕與文案生成邏輯 ---
if st.button("✨ 生成揪團文案", type="primary"):
    if not course_name:
        st.error("請輸入課程名稱！")
    else:
        # 這裡就是把資料組裝起來的地方
        result = f"🔥 【熱門團課】{course_name} 開團揪人！\n\n"
        
        if original_price > 0:
            result += f"💰 原價學費：${original_price}\n"
        result += f"🏷️ 團報優惠：${group_price} "
        
        if original_price > group_price:
             result += f"(現省 ${original_price - group_price}❗)\n"
        else:
             result += "\n"
             
        result += f"\n✨ 課程亮點：\n{course_highlights}\n"
        result += f"\n👉 手刀報名連結：{course_link}\n"
        result += "\n--------------------------------\n💬 還有名額，要加+1，滿團即止！"
        
        st.success("生成成功！請複製下方文字貼到群組：")
        st.code(result)
