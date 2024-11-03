from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Karol_CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "💼 Digital CV | Adnan Karol"
PAGE_ICON = "🌟"
NAME = "Adnan Karol"
DESCRIPTION = "Full-Stack Data Scientist at SURU - Part of LIXIL 🌐"
EMAIL = "📫 adnanmushtaq5@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/adnan-karol-aa1666179/",
    "GitHub": "https://github.com/adnankarol",
    "Medium": "https://adnankarol.medium.com/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(EMAIL)

# --- SOCIAL LINKS ---
st.write("🌐 Connect with me:")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("🚀 **Experience & Qualifications**")
st.write(
    """
- ✅ 3+ years of experience extracting insights from data
- 🧠 Skilled in Data Science, Machine Learning, and Python
- 📊 Strong foundation in statistics and data analysis
- 💼 Collaborative team player with a proactive approach
"""
)

# --- SKILLS ---
st.write("💡 **Skills and Technologies**")
st.write(
    """
- **👩‍💻 Programming:** Python 🐍
- **🧠 ML Libraries:** TensorFlow, Keras, OpenCV, Pandas, Scikit-Learn, NumPy
- **☁️ Cloud:** AWS Cloud (Athena, S3, EC2, SageMaker, Lambda, ETL, IAM), Oracle Cloud
- **🗄️ Databases:** Redshift, MongoDB, MySQL, SQLite 📂
- **📊 BI Tools:** Tableau, QuickSight 📊
- **🛠️ Embedded Hardware:** Raspberry Pi, Nvidia Jetson Nano, Arduino 🔧
- **🤖 Automation:** Jenkins, Docker, GitHub Actions ⚙️
- 🌐 Others: Git, Agile, Confluence, JIRA, Scrum
- **🌍 Language:** English (Fluent), German (Elementary)
"""
)

# --- WORK HISTORY ---
st.write("📂 **Work History**")
st.write("---")

# --- JOB 1
st.write(
    "🚧", "**Data Scientist | [SURU - Part of LIXIL](https://www.suru-water.com)**"
)
st.write("08/2021 - Present")
st.write(
    """
- 🔍 **Case-Validation:** Developed ML models to detect anomalies, reducing water damage risk #AnomalyDetection
- 💧 **Pressure Algo 2.0:** Improved pressure measurement models for leakage detection #SensorData
- 💡 **GOD (Gauge of Drops):** Deep learning for micro-leak detection with 96% accuracy, deployed on AWS #AWS
- 📸 **ICAS:** Enhanced image quality detection for user registration, reducing re-upload requests by 50%
- 🔄 **MLOps for ICAS:** Built automated monthly model re-training pipelines #MLOps
- 📈 Created **Tableau dashboards** to empower customer support teams and accelerate business intelligence
"""
)

# --- JOB 2
st.write("🚧", "**Data Science Intern | [Vialytics GmbH](https://www.vialytics.com)**")
st.write("07/2020 - 03/2021")
st.write(
    """
- 📷 Trained YOLOv4 for road damage detection on Oracle Cloud #ObjectDetection
- 🚧 Analyzed accelerometer data for road unevenness detection, in active use #SensorData
- ⚙️ Conducted anomaly analysis to improve road damage categorization accuracy
"""
)

# --- EDUCATION ---
st.write("🎓 **Education**")
st.write("---")
st.write("**Master of Science in Information Technology | University of Stuttgart**")
st.write("Oct. 2018 – May 2021")
st.write(
    """
- 🧠 Master Thesis: Used ML & DL to analyze EEG/ECG signals, comparing approaches for best results #SignalProcessing
"""
)

# --- Projects & Accomplishments ---
st.write("🏆 **Projects & Accomplishments**")
st.write("---")
PROJECTS = {
    "GOD: System and method for detecting leakages in fluid-bearing structures": "Deep learning project with 96% accuracy; patent pending.",
    "Water Consumption Prediction Service": "Built an end-to-end forecasting system, deployed with Docker and Flask. [**GitHub**](https://github.com/adnanmushtaq1996/Water_Consumption_Forecasting_Deployment)",
    "LSTM and CNN Based IMU Sensor Fusion Approach for Human Pose Identification": "Published in Springer for using LSTM & CNN in pose detection. [**Springer**](https://link.springer.com/chapter/10.1007/978-3-030-69547-7_74)",
    "YoloV8 Serverless Deployment": "Successfully deployed the YOLOv8 model on Amazon SageMaker Endpoints, integrating it with AWS Lambda and API Gateway to provide scalable object detection solutions. [**GitHub**](https://github.com/adnankarol/YOLOv8Deploy-SageMaker-Lambda-API-Gateway-Model-Deployment)",
    "classifierAgent: A Machine Learning Classification Python Package": "Created a user-friendly Python package designed for efficient machine learning classification tasks, easily installable via pip. [**GitHub**](https://github.com/adnankarol/classifierAgent)",
}

for project, description in PROJECTS.items():
    st.write(f"🔹 **{project}**: {description}")

# --- CERTIFICATIONS ---
st.write("📜 **Certifications**")
st.write("---")
st.write(
    "🏅 **AWS Certified Cloud Practitioner** - Demonstrates AWS Cloud fundamentals [**Badge**](https://www.credly.com/badges/484de3ac-d0ec-410d-8e39-86d0acf9ba00/public_url)"
)
st.write(
    "🎓 **AWS Certified Machine Learning Specialty** - Demonstrates AWS Cloud Machine Learning fundamentals [**Certificate**](https://udemy-certificate.s3.amazonaws.com/pdf/UC-c0e83341-3055-483a-bcb6-7e6f878f2e25.pdf)"
)
