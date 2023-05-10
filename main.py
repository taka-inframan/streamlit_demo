import streamlit as st
import time

st.title("Streamlit 入門ﾁｬｰｰｰｰｰｰﾝ")

st.write("Progress bar の表示")
"スタート"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
        latest_iteration.text(f"ステータス {i+1}")
        bar.progress(i+1)
        time.sleep(0.1)
        
"Done!"




left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
        right_column.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write("問い合わせ1はこちら")
expander.write("問い合わせ2はこちら")
expander.write("問い合わせ3はこちら")
# condision = st.slider("あなたの今の調子は？",  0, 100, 50)
# "コンディション", condision

# text = st.text_input("あなたの趣味は？")
# "あなたの趣味は", text

# option = st.selectbox(
#         "あなたが好きな数字を教えてください",
#         list(range(1, 11))
# )

# "あなたの好きな数字は", option, "です"

# if st.checkbox("Show Image"):
#         img = Image.open("dog.png")
#         st.image(img, caption="bawbaw", use_column_width=True)
