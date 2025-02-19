import streamlit as st
import requests

# Telegram Bot Credentials
TELEGRAM_BOT_TOKEN = "7760155802:AAH_RP6cBX7pzIojKffJXew8uC_nQDnLBRo"  # Replace with your bot token
TELEGRAM_CHAT_ID = "867454554"  # Replace with your Telegram chat ID

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

# Streamlit UI
st.title("Client Submission Form")

company = st.text_input("🏢 Company Name:")
name = st.text_input("👤 Your Name:")
number = st.text_input("📞 Contact Number:")

# Dropdown for "Type"
type_options = ["High Margins", "Commission", "Volume"]
selected_type = st.selectbox("📊 Select Type:", type_options)

if st.button("Submit"):
    if company and name and number and selected_type:
        # Send Telegram Notification
        telegram_message = f"📩 New Submission:\n🏢 Company: {company}\n👤 Name: {name}\n📞 Number: {number}\n📊 Type: {selected_type}"
        send_telegram_message(telegram_message)

        st.success("✅ Submitted successfully! You will receive a Telegram notification.")
    else:
        st.error("⚠️ Please fill in all fields before submitting.")
