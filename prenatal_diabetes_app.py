import streamlit as st

st.set_page_config(page_title="Prenatal Diabetes Monitoring", layout="centered")

# Title and Introduction
st.title("Prenatal Diabetes Monitoring App")
st.subheader("A smarter way to manage gestational diabetes")

# Sidebar Navigation
st.sidebar.title("Menu")
page = st.sidebar.selectbox("Go to", ["Dashboard", "Glucose Log", "Reminders", "AI Suggestions", "Settings"])

# Dashboard Page
if page == "Dashboard":
    st.header("Dashboard")
    st.write("Welcome to your personalized dashboard.")
    st.write("Here you can view your latest glucose levels, track trends, and get quick insights.")
    
    # Example data visualizations and stats
    st.subheader("Today's Glucose Levels")
    st.metric(label="Fasting Glucose", value="95 mg/dL", delta="-5 mg/dL since last check")
    st.metric(label="Postprandial Glucose", value="125 mg/dL", delta="+10 mg/dL since last check")
    
    # A graph for glucose trends
    st.subheader("Weekly Glucose Trends")
    st.line_chart([90, 95, 100, 110, 105, 100, 95])
    
    st.subheader("Reminders & Alerts")
    st.write("- Next Glucose Check: 11:30 AM")
    st.write("- Reminder: Eat a balanced breakfast with controlled carbs")
    st.warning("High glucose levels detected! Please check with your provider.")

# Glucose Log Page
elif page == "Glucose Log":
    st.header("Glucose Log")
    st.write("Record your glucose levels here.")
    
    fasting = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=200, value=90)
    postprandial = st.number_input("Postprandial Glucose (mg/dL)", min_value=50, max_value=300, value=120)
    
    # Add log button
    if st.button("Add to Log"):
        st.success("Glucose levels added successfully!")
    
    # Show previous logs (mock data)
    st.subheader("Previous Logs")
    st.table({
        "Date": ["2024-10-18", "2024-10-19", "2024-10-20"],
        "Fasting Glucose": [95, 100, 90],
        "Postprandial Glucose": [120, 130, 125]
    })

# Reminders Page
elif page == "Reminders":
    st.header("Reminders")
    st.write("Manage your reminders for glucose testing and meals.")
    
    st.subheader("Set a Reminder")
    reminder_time = st.time_input("Reminder Time", value=None)
    reminder_type = st.selectbox("Reminder Type", ["Glucose Check", "Meal", "Medication"])
    
    if st.button("Set Reminder"):
        st.success(f"Reminder set for {reminder_type} at {reminder_time}!")
    
    # Show current reminders (mock data)
    st.subheader("Current Reminders")
    st.write("1. Glucose Check at 7:00 AM")
    st.write("2. Meal at 12:00 PM")
    st.write("3. Medication at 9:00 PM")

# AI Suggestions Page
elif page == "AI Suggestions":
    st.header("AI Diet & Dose Suggestions")
    st.write("Based on your recent glucose data, here are some recommendations.")
    
    st.subheader("Diet Suggestions")
    st.write("- Eat a protein-rich breakfast with low carbs.")
    st.write("- Avoid sugary snacks before bedtime.")
    
    st.subheader("Dose Adjustment Suggestions")
    st.write("Your insulin dose should be adjusted slightly due to elevated fasting levels.")
    st.info("Suggested dose change: +2 units of insulin in the morning.")

# Settings Page
elif page == "Settings":
    st.header("Settings")
    
    st.subheader("Customize Alerts")
    high_glucose = st.number_input("High Glucose Threshold (mg/dL)", min_value=100, max_value=300, value=200)
    low_glucose = st.number_input("Low Glucose Threshold (mg/dL)", min_value=40, max_value=100, value=60)
    
    st.write("Current Settings:")
    st.write(f"High glucose alerts at {high_glucose} mg/dL")
    st.write(f"Low glucose alerts at {low_glucose} mg/dL")

    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Designed for mothers managing prenatal diabetes.")
