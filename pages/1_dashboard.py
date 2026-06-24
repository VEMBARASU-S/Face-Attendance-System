from streamlit_autorefresh import st_autorefresh
import streamlit as st
import matplotlib.pyplot as plt


if "logged_in" not in st.session_state:
    st.error("Please Login First")
    st.stop()
if st.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.switch_page("app.py")
import streamlit as st
import sqlite3
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Face Attendance Dashboard", layout="wide")

st.title("📷 Face Attendance Dashboard")
st_autorefresh(interval=5000, key="refresh")

# Database Connection
conn = sqlite3.connect("attendance.db")
df = pd.read_sql_query("SELECT * FROM attendance", conn)

search = st.text_input("🔍 Search Student")

if search:
    df = df[df["name"].str.contains(search, case=False, na=False)]

selected_date = st.selectbox(
    "📅 Select Date",
    ["All"] + list(df["date"].unique())
)

if selected_date != "All":
    df = df[df["date"] == selected_date]    

st.subheader("Attendance Records")
st.dataframe(df, width="stretch")

# Statistics
st.subheader("Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Unique Students", df["name"].nunique())

with col3:
    today = pd.Timestamp.today().strftime("%Y-%m-%d")
    today_count = len(df[df["date"] == today])

    st.metric("Today's Attendance", today_count)
    last_record = df.iloc[-1]

st.info(
    f"🕒 Last Entry: {last_record['name']} at {last_record['time']}"
)

# Analytics
st.subheader("📊 Attendance Analytics")

attendance_count = df["name"].value_counts()
top_student = attendance_count.idxmax()
top_count = attendance_count.max()

st.success(f"🏆 Top Student: {top_student}")
st.info(f"📋 Attendance Count: {top_count}")


st.subheader("🥧 Attendance Percentage")

fig, ax = plt.subplots(figsize=(4,4))

ax.pie(
    attendance_count,
    labels=attendance_count.index,
    autopct="%1.1f%%"
)

ax.set_title("Attendance Distribution")

st.pyplot(fig)



st.bar_chart(attendance_count)

st.subheader("📈 Attendance Distribution")

st.line_chart(attendance_count)

conn.close()