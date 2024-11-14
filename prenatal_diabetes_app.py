import streamlit as st
import pandas as pd

st.set_page_config(page_title="Prenatal Diabetes Monitoring", layout="centered")

# Title and Introduction
st.title("Prenatal Diabetes Monitoring App")
st.subheader("A smarter way to manage gestational diabetes")

# Sidebar Navigation
st.sidebar.title("Menu")
page = st.sidebar.selectbox("Go to", ["Dashboard", "Glucose Log", "Reminders", "AI Suggestions", "Settings"])

# Dashboard Page
if page == "Dashboard":
    st.header("Dashboard (Under Development)")
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
    st.write("Record and manage your glucose readings.")

    # Initialize session state to store glucose logs
    if "glucose_log" not in st.session_state:
        st.session_state["glucose_log"] = []

    # Input fields for glucose levels
    fasting = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=200, value=90)
    postprandial = st.number_input("Postprandial Glucose (mg/dL)", min_value=50, max_value=300, value=120)
    log_date = st.date_input("Date", value=None)

    # Add button to log readings
    if st.button("Add to Log"):
        if log_date:
            st.session_state["glucose_log"].append({
                "Date": log_date.strftime("%Y-%m-%d"),
                "Fasting Glucose": fasting,
                "Postprandial Glucose": postprandial
            })
            st.success("Glucose levels added successfully!")
        else:
            st.error("Please select a valid date.")

    # Display the glucose log
    st.subheader("Previous Logs")
    if st.session_state["glucose_log"]:
        # Convert logs to a pandas DataFrame
        df_log = pd.DataFrame(st.session_state["glucose_log"])
        st.dataframe(df_log, use_container_width=True)

        # Editing Logs
        st.subheader("Edit a Log Entry")
        log_index = st.selectbox("Select Log Entry to Edit", options=range(len(st.session_state["glucose_log"])), format_func=lambda i: f"{st.session_state['glucose_log'][i]['Date']} (Fasting: {st.session_state['glucose_log'][i]['Fasting Glucose']} mg/dL, Postprandial: {st.session_state['glucose_log'][i]['Postprandial Glucose']} mg/dL)")
        if st.button("Edit Selected Log"):
            log_to_edit = st.session_state["glucose_log"][log_index]
            edited_date = st.date_input("Edit Date", value=pd.to_datetime(log_to_edit["Date"]))
            edited_fasting = st.number_input("Edit Fasting Glucose (mg/dL)", value=log_to_edit["Fasting Glucose"])
            edited_postprandial = st.number_input("Edit Postprandial Glucose (mg/dL)", value=log_to_edit["Postprandial Glucose"])

            if st.button("Save Changes"):
                st.session_state["glucose_log"][log_index] = {
                    "Date": edited_date.strftime("%Y-%m-%d"),
                    "Fasting Glucose": edited_fasting,
                    "Postprandial Glucose": edited_postprandial
                }
                st.success("Log entry updated successfully!")
                st.experimental_rerun()

        # Option to delete a log
        st.subheader("Delete a Log Entry")
        delete_index = st.selectbox("Select Log Entry to Delete", options=range(len(st.session_state["glucose_log"])), format_func=lambda i: f"{st.session_state['glucose_log'][i]['Date']} (Fasting: {st.session_state['glucose_log'][i]['Fasting Glucose']} mg/dL, Postprandial: {st.session_state['glucose_log'][i]['Postprandial Glucose']} mg/dL)")
        if st.button("Delete Selected Log"):
            st.session_state["glucose_log"].pop(delete_index)
            st.success("Log entry deleted successfully!")
            st.experimental_rerun()

        # Export logs to CSV
        st.download_button(
            label="Export to CSV",
            data=df_log.to_csv(index=False).encode("utf-8"),
            file_name="glucose_log.csv",
            mime="text/csv"
        )
    else:
        st.info("No glucose readings logged yet.")

# Reminders Page
elif page == "Reminders":
    st.header("Reminders")
    st.write("Manage your reminders for glucose testing, meals, and medications.")

    # Initialize session state for reminders
    if "reminders" not in st.session_state:
        st.session_state["reminders"] = []

    # Add Reminder Section
    st.subheader("Set a Reminder")
    reminder_time = st.time_input("Reminder Time", value=None)
    reminder_type = st.selectbox("Reminder Type", ["Glucose Check", "Meal", "Medication"])
    reminder_date = st.date_input("Reminder Date", value=None)

    if st.button("Add Reminder"):
        if reminder_date and reminder_time:
            st.session_state["reminders"].append({
                "Date": reminder_date.strftime("%Y-%m-%d"),
                "Time": reminder_time.strftime("%H:%M"),
                "Type": reminder_type
            })
            st.success("Reminder added successfully!")
        else:
            st.error("Please select a valid date and time.")

    # View Reminders Section
    st.subheader("Current Reminders")
    if st.session_state["reminders"]:
        df_reminders = pd.DataFrame(st.session_state["reminders"])
        st.table(df_reminders)

        # Delete Reminder Section
        st.subheader("Delete a Reminder")
        reminder_index = st.selectbox("Select Reminder to Delete", options=range(len(st.session_state["reminders"])), format_func=lambda i: f"{st.session_state['reminders'][i]['Type']} on {st.session_state['reminders'][i]['Date']} at {st.session_state['reminders'][i]['Time']}")
        if st.button("Delete Selected Reminder"):
            st.session_state["reminders"].pop(reminder_index)
            st.success("Reminder deleted successfully!")
            st.experimental_rerun()  # Refresh the app to update the table

        # Export Reminders to CSV
        st.subheader("Export Reminders")
        st.download_button(
            label="Export to CSV",
            data=df_reminders.to_csv(index=False).encode("utf-8"),
            file_name="reminders.csv",
            mime="text/csv"
        )
    else:
        st.info("No reminders set yet.")

# AI Suggestions Page
elif page == "AI Suggestions":
    st.header("AI Diet & Dose Suggestions (Under Development)")
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
    
    # Initialize session state for settings
    if "settings" not in st.session_state:
        st.session_state["settings"] = {
            "high_glucose": 200,
            "low_glucose": 60
        }

    # Customize Alerts
    st.subheader("Customize Alerts")
    high_glucose = st.number_input(
        "High Glucose Threshold (mg/dL)", 
        min_value=100, max_value=300, 
        value=st.session_state["settings"]["high_glucose"]
    )
    low_glucose = st.number_input(
        "Low Glucose Threshold (mg/dL)", 
        min_value=40, max_value=100, 
        value=st.session_state["settings"]["low_glucose"]
    )

    # Save Settings
    if st.button("Save Settings"):
        st.session_state["settings"]["high_glucose"] = high_glucose
        st.session_state["settings"]["low_glucose"] = low_glucose
        st.success("Settings saved successfully!")

    # Reset to Default Settings
    if st.button("Reset to Default Settings"):
        st.session_state["settings"]["high_glucose"] = 200
        st.session_state["settings"]["low_glucose"] = 60
        st.success("Settings reset to default values!")
        st.experimental_rerun()

    # Preview Alerts
    st.subheader("Preview Alerts")
    if st.button("Preview High Glucose Alert"):
        st.warning(f"High glucose alert triggered at {high_glucose} mg/dL!")

    if st.button("Preview Low Glucose Alert"):
        st.warning(f"Low glucose alert triggered at {low_glucose} mg/dL!")

    # Export Settings
    st.subheader("Export Settings")
    settings_json = {
        "High Glucose Threshold": st.session_state["settings"]["high_glucose"],
        "Low Glucose Threshold": st.session_state["settings"]["low_glucose"]
    }
    st.download_button(
        label="Export to JSON",
        data=str(settings_json).encode("utf-8"),
        file_name="settings.json",
        mime="application/json"
    )

    # Import Settings
    st.subheader("Import Settings")
    uploaded_file = st.file_uploader("Upload Settings JSON File", type=["json"])
    if uploaded_file is not None:
        imported_settings = eval(uploaded_file.read().decode("utf-8"))
        st.session_state["settings"]["high_glucose"] = imported_settings["High Glucose Threshold"]
        st.session_state["settings"]["low_glucose"] = imported_settings["Low Glucose Threshold"]
        st.success("Settings imported successfully!")
        st.experimental_rerun()

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Designed for mothers managing prenatal diabetes.")
