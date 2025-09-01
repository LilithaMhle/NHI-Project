import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Page Config ---
st.set_page_config(page_title="NHI Dashboard", layout="wide", initial_sidebar_state="collapsed")

# --- Initialize session state ---
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "theme" not in st.session_state:
    st.session_state.theme = "Default (dark glass)"
if "notifications" not in st.session_state:
    st.session_state.notifications = True
if "auto_refresh" not in st.session_state:
    st.session_state.auto_refresh = 0

# --- Themes ---
def dark_theme():
    return """
    <style>
    .stApp { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); color: #f0f0f0; font-family: 'Segoe UI', sans-serif; }
    .card { background: rgba(255,255,255,0.08); padding: 1rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); margin-bottom: 1rem; }
    </style>
    """

def light_theme():
    return """
    <style>
    .stApp { background: #fafafa; color: #333; font-family: 'Segoe UI', sans-serif; }
    .card { background: #fff; padding: 1rem; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 1rem; }
    </style>
    """

# --- Apply Theme ---
if st.session_state.theme == "Default (dark glass)":
    st.markdown(dark_theme(), unsafe_allow_html=True)
else:
    st.markdown(light_theme(), unsafe_allow_html=True)

# --- Layout: Sidebar (Menu) + Main Content ---
col1, col2 = st.columns([1, 5])

pages = ["Home", "EDA", "Model", "Settings"]

with col1:
    st.markdown('<div class="card"><h3>📌 Menu</h3>', unsafe_allow_html=True)
    for p in pages:
        label = {
            "Home": "🏠 Home",
            "EDA": "📊 Exploratory Data Analysis",
            "Model": "🤖 Model Results",
            "Settings": "⚙ Settings",
        }[p]
        if st.button(label, key=p):
            st.session_state.page = p
    st.markdown("</div>", unsafe_allow_html=True)

# --- Notifications ---
notif_placeholder = col2.empty()
if st.session_state.notifications:
    notif_placeholder.info("🔔 Notifications enabled — toggle in Settings to turn off.")

# --- Main Content ---
with col2:
    st.title("🏥 National Health Insurance (NHI) Dashboard")

    # --- HOME ---
    if st.session_state.page == "Home":
        st.header("Project Presentation")
        st.markdown(
            """
            This dashboard showcases a *machine learning project* built to support the rollout of the *National Health Insurance (NHI)* in South Africa.

            ### Key Tasks:
             *Predicting Healthcare Service Demand*  
               Forecast visits to GPs, specialists, and hospitals using demographic and health-related data.  
              Relevance to Task 1 (Predicting Healthcare Service Demand):
              - Enables analysis of how demographics (age, gender, chronic conditions) affect demand.
              - Supports detection of patterns in treatment types, admissions, and length of stay.
              - Provides historical healthcare usage data that can be modeled to predict future demand under the NHI system.
              

            ### 🎯 Purpose:
            These insights help policymakers and healthcare providers *allocate resources efficiently, plan budgets, and ensure equitable access* to services.

            *Developed by:*  
            Mhle L, Mncwango A S, Msane N Z, Mthembu S H, Ngwadla M, Shangase S S
            """
        )

    # --- EDA ---
    elif st.session_state.page == "EDA":
        st.header("Exploratory Data Analysis")

        dataset_path = "datasets"
        if os.path.exists(dataset_path):
            files = [f for f in os.listdir(dataset_path) if f.endswith(".csv")]
            if files:
                selected_file = st.selectbox("📂 Select a dataset", files)
                df = pd.read_csv(os.path.join(dataset_path, selected_file))
                st.dataframe(df.head())

                if "age" in df.columns:
                    st.subheader("Age Distribution")
                    fig, ax = plt.subplots()
                    df["age"].dropna().astype(int).hist(bins=20, ax=ax)
                    st.pyplot(fig)

                if "admission_type" in df.columns:
                    st.subheader("Admission Type Distribution")
                    fig, ax = plt.subplots()
                    df["admission_type"].value_counts().plot(kind="bar", ax=ax)
                    st.pyplot(fig)
            else:
                st.warning("⚠ No CSV files found in the datasets folder.")
        else:
            st.error("❌ Datasets folder not found. Please add it to the project.")

    # --- MODEL RESULTS ---
    elif st.session_state.page == "Model":
        st.header("🤖 Model Results")

        # Fixed Accuracy
        accuracy = 87.88
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Model Accuracy", f"{accuracy:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)

        # Classification Report
        classification_report = """
              precision    recall  f1-score   support

    ELECTIVE       0.00      0.00      0.00         2
   EMERGENCY       0.91      0.97      0.94        30
      URGENT       0.00      0.00      0.00         1

    accuracy                           0.88        33
   macro avg       0.30      0.32      0.31        33
weighted avg       0.82      0.88      0.85        33
        """

        st.subheader("📑 Classification Report")
        st.text_area("Report", classification_report, height=200)

    # --- SETTINGS ---
    elif st.session_state.page == "Settings":
        st.header("⚙ Settings")
        with st.form("settings_form"):
            theme_choice = st.selectbox(
                "Theme", ["Default (dark glass)", "Light"],
                index=0 if st.session_state.theme == "Default (dark glass)" else 1
            )
            notifications_choice = st.checkbox("Show notifications banner", value=st.session_state.notifications)
            auto_refresh_choice = st.number_input("Auto-refresh (seconds, 0 = off)",
                                                  min_value=0, max_value=300,
                                                  value=int(st.session_state.auto_refresh or 0), step=5)
            submitted = st.form_submit_button("Save Settings")
        if submitted:
            st.session_state.theme = theme_choice
            st.session_state.notifications = notifications_choice
            st.session_state.auto_refresh = auto_refresh_choice
            st.success("✅ Settings updated — refresh the page to see changes")
