from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Karol_CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Adnan Karol"
PAGE_ICON = ":wave:"
NAME = "Adnan Karol"
DESCRIPTION = """
Full-Stack Data Scientist at SURU-Part of LIXIL.
"""
EMAIL = "adnanmushtaq5@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/adnan-karol-aa1666179/",
    "GitHub": "https://github.com/adnankarol",
    "Medium": "https://adnankarol.medium.com/",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Data Science, Machine Learning and Python
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills and Technologies")
st.write(
"""
- 👩‍💻 Programming: Python
- 🧠 ML Libraries: Tensorflow, Keras, OpenCV, Pandas, Scikit-learn, Numpy, Scipy, Matplotlib
- ☁️ Cloud: AWS Cloud (Athena, S3, EC2, Redshift, SageMaker, Lambda, SNS, ETL, Eventbridge, IAM), Oracle Cloud
- 🗄️ Databases: Redshift, MongoDB, MySql, SQLite, InfluxDB
- 📊 Business Intelligence: Tableau, Quicksight
- 🛠️ Embedded Hardware: Raspberry Pi, Nvidia Jetson Nano, Arduino, ESP32, IMU, EMG sensors
- 🤖 Automation: Jenkins, Docker, MLOPS, GitHub Actions
- 🌐 Others: Git, Agile, Confluence, JIRA, Scrum
- 🌍 Language: English (Fluent), German (Elementary)
"""
)



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Scientist | [SURU-Part of LIXIL](https://www.suru-water.com)**")
st.write("08/2021 - Present")
st.write(
    """
- ► **Project: Case-Validation:** This project uses **machine learning** to identify houses with anomalies, assisting the Prevention team in preventing water damage. #AnomalyDetection
- ► **Project: Pressure Algo 2.0:** A project aimed at enhancing the way the **SenseGuard device** performs pressure measurements. Enhanced the models for scheduling pressure measurements and leakage detection. #SensorData #LeakageDetection
- ► **Project: GOD (Guage of Drops):** A project that uses **deep learning** to detect homes with micro-leakage and has a development testing accuracy of **96%**. As a result, the Prevention Team’s leak detection business will generate revenue more quickly. This **patent-pending** project is deployed using **AWS Redshift**, **Lambda**, **ETL Jobs**, and **S3**. #MicroLeakage #AWS
- ► **Project: ICAS (Image Capture Assistance System):** A project that requests users to contribute higher-quality pipe system images as part of the registration process. The Sales team will benefit from this by preventing any delays in the device installation procedure. Additionally, I helped the cloud team deploy the project using **Amazon S3**, **Lambda**, and **ETL Jobs**, which works in real-time. The project effectively minimizes the frequency of requests from the operations team for customers to re-upload images, achieving a notable reduction of over **50%**.
- ► **Project: MLOPS for ICAS:** Created the architecture and set up the pipeline for automatic monthly model re-training of the ICAS model to be stable, reliable, and robust, using the data collected from customers. #MLOps #ModelRetraining #DataCollection
- ► **Project: Data Extraction Tools:** Created tools to fetch data from the data lakes. With the help of these tools, the sales and after-sales teams can quickly speed up procedures and pull relevant information from the **AWS big data cloud**. #DataLakes
- ► Conducted a **statistical analysis** of insurance portfolios and performed a suitability analysis for collaboration. Assisted management and business leaders in assessing the viability and profitability of potential collaborations with insurance companies. #InsurancePortfolios
- ► Engineered **Tableau dashboards** to elevate business intelligence within the company, enabling customer service teams to directly support and diagnose customer issues, while also providing valuable assistance during firmware updates and similar tasks. Cleaned Tableau space, eradicated unused dashboards, and optimized queries to make existing dashboards **4x faster** [Dashboard Link](https://public.tableau.com/app/profile/adnan3937#!/). #BusinessIntelligence
- ► Presented **data insights** to customers, showcasing the actionable findings and facilitating informed decision-making.
"""
)


# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Science Intern | [Vialytics GmbH](https://www.vialytics.com)**")
st.write("07/2020 - 03/2021")
st.write(
    """
- ► Trained a **road damage object detector** using **YOLOv4** on **Oracle Cloud**, utilizing **image data**.
- ► Implemented the assessment of **road unevenness** by leveraging **non-visual smartphone sensors**, specifically the **accelerometer data**. This technology is actively employed by the company. #SensorDataAnalysis #RoadConditionAssessment
- ► Conducted **fault and anomaly analysis** to detect and rectify **outliers** within a specific category of damages. #AnomalyDetection
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCATION")
st.write("---")

# --- Education
st.write("🎓", "**Master of Science in Information Technology | University of Stuttgart**")
st.write("Oct. 2018 – May 2021")
st.write(
    """
- ► Master Thesis: Implemented feature extraction techniques and applied both machine learning and deep
  learning algorithms to analyze EEG and ECG signals, aiming to discern the most effective approach between
  machine learning and deep learning methodologies in physiological signal analysis. #SignalProcessing
  #MachineLearning #DeepLearning #FeatureExtraction
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
PROJECTS = {
    "🏆 GOD: System and method for detecting leakages in a fluid-bearing structure": "A project that uses deep learning to detect homes with micro-leakage and has a development testing accuracy of 96%. Currently, this project is filed with the patent office.",
    "🏆 Water Demand Forecasting and Deployment using Docker and Flask": "Developed a comprehensive end-to-end system for forecasting water consumption, encompassing data preprocessing, model construction utilizing CNN-LSTM, and model deployment through Docker and Flask. [GitHub](https://github.com/adnanmushtaq1996/Water_Consumption_Forecasting_Deployment)",
    "🏆 LSTM and CNN Based IMU Sensor Fusion Approach for Human Pose Identification": "Springer, International Symposium on Wearable Robotics, WeRob 2020: Wearable Robotics: [Springer Link](https://link.springer.com/chapter/10.1007/978-3-030-69547-7_74)",
}

for project, description in PROJECTS.items():
    st.write(f"{project}")
    st.write(f"📘 **{description.replace('[GitHub]', '[**GitHub**]')}**\n")


# --- Certification ---
st.write('\n')
st.subheader("Certification")
st.write("---")
st.write(
    """
- ► Achieved AWS Certified Cloud Practitioner certification, demonstrating understanding of AWS Cloud fundamentals. Verify Certification: [AWS Certified Cloud Practitioner](https://www.credly.com/badges/484de3ac-d0ec-410d-8e39-86d0acf9ba00/public_url)
"""
)




