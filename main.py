import streamlit as st

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📉",
    layout="centered",
)

st.title("📉 Customer Churn Prediction")
st.write("Enter customer information to predict whether the customer may churn.")


@st.cache_resource
def get_prediction_pipeline():
    return PredictPipeline()


with st.form("churn_prediction_form"):
    st.subheader("Customer Information")

    gender = st.selectbox("Gender", ["Female", "Male"])
    senior_citizen = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)

    st.subheader("Services")

    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox(
        "Multiple Lines", ["No", "Yes", "No phone service"]
    )
    internet_service = st.selectbox(
        "Internet Service", ["DSL", "Fiber optic", "No"]
    )
    online_security = st.selectbox(
        "Online Security", ["No", "Yes", "No internet service"]
    )
    online_backup = st.selectbox(
        "Online Backup", ["No", "Yes", "No internet service"]
    )
    device_protection = st.selectbox(
        "Device Protection", ["No", "Yes", "No internet service"]
    )
    tech_support = st.selectbox(
        "Tech Support", ["No", "Yes", "No internet service"]
    )
    streaming_tv = st.selectbox(
        "Streaming TV", ["No", "Yes", "No internet service"]
    )
    streaming_movies = st.selectbox(
        "Streaming Movies", ["No", "Yes", "No internet service"]
    )

    st.subheader("Account & Billing")

    contract = st.selectbox(
        "Contract", ["Month-to-month", "One year", "Two year"]
    )
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)",
        ],
    )
    monthly_charges = st.number_input(
        "Monthly Charges", min_value=0.0, value=50.0, step=0.01
    )
    total_charges = st.number_input(
        "Total Charges", min_value=0.0, value=500.0, step=0.01
    )

    submitted = st.form_submit_button("Predict Churn")


if submitted:
    try:
        customer_data = CustomData(
            gender=gender,
            SeniorCitizen=senior_citizen,
            Partner=partner,
            tenure=tenure,
            Dependents=dependents,
            PhoneService=phone_service,
            MultipleLines=multiple_lines,
            InternetService=internet_service,
            OnlineSecurity=online_security,
            OnlineBackup=online_backup,
            DeviceProtection=device_protection,
            TechSupport=tech_support,
            StreamingTV=streaming_tv,
            StreamingMovies=streaming_movies,
            Contract=contract,
            PaperlessBilling=paperless_billing,
            PaymentMethod=payment_method,
            MonthlyCharges=monthly_charges,
            TotalCharges=total_charges,
        )

        features = customer_data.get_dataframe()
        prediction = get_prediction_pipeline().predict(features)[0]
        will_churn = str(prediction).strip().lower() in {"1", "yes"}

        if will_churn:
            st.error("High churn risk: This customer is likely to leave the service.")
            st.caption("Consider contacting the customer with a retention offer or support.")
        else:
            st.success("Low churn risk: This customer is likely to stay with the service.")
            st.caption("No immediate retention action appears necessary.")

    except Exception as error:
        st.error(f"Prediction failed: {error}")
