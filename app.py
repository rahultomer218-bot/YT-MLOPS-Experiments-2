import streamlit as st

# st.tile को st.title होना चाहिए
st.title("Power Calculator")

st.write("यह एक साधारण पावर कैलकुलेटर है। बेस और एक्सपोनेंट दर्ज करें।")

# इनपुट लेना
n = st.number_input("Base नंबर दर्ज करें")
e = st.number_input("Exponent नंबर दर्ज करें")

# गणना करना
if st.button("Calculate"):
    power = n ** e
    st.write(f"{n} की पावर {e} का परिणाम है: {power}")