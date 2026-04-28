import streamlit as st
from datetime import datetime

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="AgriSafe AI",
    page_icon="🌱",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------
st.title("🌱 AgriSafe AI Dashboard")
st.subheader("Smart Farming Monitoring System")

st.write("Welcome! This system helps monitor crops, soil, and environmental conditions using AI.")

st.divider()

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("Control Panel")

mode = st.sidebar.selectbox(
    "Choose Mode",
    ["Overview", "Soil Analysis", "Crop Health", "AI Assistant"]
)

st.sidebar.info("AgriSafe AI v1.0")

# ---------------------------
# PROJECT LINKS (FIXED)
# ---------------------------
st.sidebar.title("🔗 Project Links")

# GitHub
st.sidebar.markdown("🌐 [GitHub Repository](https://github.com/aseelabor/AgriSafe---Ai)")

# Report PDF
try:
    with open("report.pdf", "rb") as f:
        st.sidebar.download_button(
            label="📄 Download Report",
            data=f,
            file_name="AgriSafe_Report.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.sidebar.error("Report file not found ❌")

# Slides PDF
try:
    with open("slides.pdf", "rb") as f:
        st.sidebar.download_button(
            label="📊 Download Slides",
            data=f,
            file_name="AgriSafe_Slides.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.sidebar.error("Slides file not found ❌")

# ---------------------------
# MAIN CONTENT
# ---------------------------
if mode == "Overview":
    col1, col2, col3 = st.columns(3)

    col1.metric("Soil Moisture", "68%", "+2%")
    col2.metric("Temperature", "32°C", "-1°C")
    col3.metric("Crop Health", "Good", "Stable")

    st.success("System running normally 🌿")

elif mode == "Soil Analysis":
    st.header("🌱 Soil Analysis")

    moisture = st.slider("Soil Moisture Level", 0, 100, 50)
    ph = st.slider("Soil pH Level", 0.0, 14.0, 7.0)

    if moisture < 30:
        st.warning("Soil is too dry. Irrigation needed.")
    elif moisture > 80:
        st.warning("Soil is too wet. Reduce watering.")
    else:
        st.success("Soil moisture is optimal.")

    if ph < 6.0:
        st.info("Soil is acidic.")
    elif ph > 7.5:
        st.info("Soil is alkaline.")
    else:
        st.success("Soil pH is balanced.")

elif mode == "Crop Health":
    st.header("🌾 Crop Health Monitoring")

    health = st.selectbox("Select Crop Condition", ["Healthy", "Mild Stress", "Diseased"])

    if health == "Healthy":
        st.success("Crops are in excellent condition 🌿")
    elif health == "Mild Stress":
        st.warning("Crops need attention (watering or nutrients).")
    else:
        st.error("Disease detected! Immediate action required.")

elif mode == "AI Assistant":
    st.header("🤖 AI Farming Assistant")

    user_input = st.text_input("Ask something about your farm:")

    if user_input:
        st.write("AI Response:")
        st.info("Based on current conditions, ensure proper irrigation and monitor soil nutrients.")

# ---------------------------
# FOOTER
# ---------------------------
st.divider()
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")