from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Deepak Ravikumar_7_0.pdf"
profile_pic = current_dir / "assets" / "profile-pic-1.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Deepak Ravikumar"
PAGE_ICON = ":wave:"
NAME = "Deepak Ravikumar"
DESCRIPTION = """
Senior Machine Learning Engineer & Data Scientist with over 7 years of professional experiences in making prediction for large datasets with practical knowledge in statistics.
"""
EMAIL = "deepak.060593@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/positivedeepak/",
    "GitHub": "https://github.com/WhiteD3vil"
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2)
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
- ✔️ 7 years of professional experiences in making prediction for large datasets.
- ✔️ Strong hands on experience and knowledge in Python and Excel.
- ✔️ Good understanding of statistical principles and their respective applications.
- ✔️ Implemented many ML/DL applications using Scikit-learn & Pytorch framework.
- ✔️ Have experience in end-to-end ML pipeline automation using MLOps frameworks  and also have experience in CI/CD pipelines using GitHub actions
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """🦾🤖🦿🖥️🧠👾👩‍💻👨‍💻
- 🦾 Machine Learning: Logistic Regression, Decision tree, Random Forest, Gradient Descent, PCA, KNN, Naive Bayes, SVM
- 🧠 Deep Learning: CNN, Faster RCNN, UNET, RNN, LSTM, YOLO models, Attention models (BERT, Siameese Networks)
- 🖥️ Domains: E-commerce, Supply chain, Healthcare, Geospatial
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy), SQL, VBA, C++, HTML, CSS, JavaScript, SQL, Pyspark, Selenium
- 📊 Data Visulization: MS Excel, Plotly, Panel, Matplotlib, Streamlit
- 📚 Frameworks: Flask, Streamlit, TensorFlow, PyTorch, Keras, OpenCV, Pandas, NumPy, Matplotlib
- 🗄️ DataStores: Postgres, MongoDB, MySQL, DynamoDB, AWS S3, RedShift
- 🤖 DevOps: Docker, Kubernetes, Terraform, AWS CDK
- 🛠️ Tools: Git, Github, Jira, Azure Devops, Heroku, VS code, Jupyter Notebook
- ☁️ Cloud: AWS (Pursuing Machine Learning - Speciality certification at CloudGuru), Azure
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Scientist | Techmango Technologies**")
st.write("04/2020 - Present")
st.write(
    """
- ► Having real-time work experience in using more than 15+ services in AWS cloud like Lambda, Eventbridge, Stepfunction, EMR, ECR, SNS, SQS, Glue, Secrets Manager, RDS, RedShift, S3, Athena, SageMaker.
- ► Worked on distributed systems using Spark for transforming terrabytes of raw data into useful data.
- ► Have experience in end-to-end ML pipeline automation using MLOps frameworks and also have experience in CI/CD pipelines using GitHub actions.
- ► Deployed many ML applications by containerizing it using Docker and created custom models in ECR.
- ► Analyzed and reduced the cost of AWS glue by 90% using CloudWatch Metrics and SparkUI.
- ► Migrated memory-intense glue jobs to EMR to save overall cost by 95%.
- ► Created multiple chatbots using RASA NLP framework for IKEA client and deployed in Azure cloud.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Application Engineer | Amazon.com**")
st.write("11/2015 - 03/2020")
st.write(
    """
- ► Developed an web application using Flask for multiple projects such as Face Recognition, Activity Recognition & Number plate detection.
- ► Responsible for creating various AWS resources and developed a complete end-to-end ETL framework using AWS services.
- ► Designed, implemented and evaluated models to solve problems in computer vision like image classification, object detection & segmentation.
- ► Responsibilities includes intial research, planning the project, designing the product, creating ML models, and testing & productionizing.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
