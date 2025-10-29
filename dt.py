import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# Page Setup
# ----------------------------------------------------------
st.set_page_config(page_title="📊 Student Analytics Dashboard", layout="wide")
st.title("📊 Student Analytics Dashboard")
st.write("A Power BI–style dashboard built using Streamlit, Pandas, NumPy, and Matplotlib")

# ----------------------------------------------------------
# Load Data Directly
# ----------------------------------------------------------
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Usman", "Hina", "Bilal", "Ayesha", "Hassan", "Noor"],
    "Math": np.random.randint(50, 100, 10),
    "Science": np.random.randint(40, 100, 10),
    "English": np.random.randint(45, 95, 10),
    "Computer": np.random.randint(60, 100, 10),
    "Geography": np.random.randint(55, 100, 10)
}
df = pd.DataFrame(data)
subjects = ["Math", "Science", "English", "Computer", "Geography"]

# ----------------------------------------------------------
# Summary KPIs
# ----------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("📘 Students", len(df))
col2.metric("🏅 Highest Total", int(df[subjects].sum(axis=1).max()))
col3.metric("📈 Average Score", f"{df[subjects].mean().mean():.2f}")
col4.metric("💻 Best Subject", df[subjects].mean().idxmax())

st.markdown("---")

# ----------------------------------------------------------
# Row 1: 3 Charts
# ----------------------------------------------------------
row1_col1, row1_col2, row1_col3 = st.columns(3)

# Chart 1: Bar Chart - Average per Subject
with row1_col1:
    st.subheader("📊 Average Marks per Subject")
    avg_subjects = df[subjects].mean()
    st.bar_chart(avg_subjects)

# Chart 2: Pie Chart - Subject Contribution
with row1_col2:
    st.subheader("🥧 Subject Score Contribution")
    fig, ax = plt.subplots()
    ax.pie(avg_subjects, labels=subjects, autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)

# Chart 3: Bar Chart - Total Marks by Student
with row1_col3:
    st.subheader("👩‍🎓 Total Marks by Student")
    df["Total"] = df[subjects].sum(axis=1)
    total_df = df[["Name", "Total"]].set_index("Name")
    st.bar_chart(total_df)

# ----------------------------------------------------------
# Row 2: 3 Charts
# ----------------------------------------------------------
row2_col1, row2_col2, row2_col3 = st.columns(3)

# Chart 4: Line Chart - Performance Comparison
with row2_col1:
    st.subheader("📈 Student Performance Across Subjects")
    st.line_chart(df.set_index("Name")[subjects])

# Chart 5: Histogram - Distribution of Selected Subject
with row2_col2:
    st.subheader("📊 Subject Score Distribution")
    subject_choice = st.selectbox("Choose a Subject", subjects, key="hist_select")
    bins = st.slider("Bins", 5, 20, 10, key="bins_slider")
    fig2, ax2 = plt.subplots()
    ax2.hist(df[subject_choice], bins=bins, color="lightblue", edgecolor="black")
    ax2.set_xlabel("Score Range")
    ax2.set_ylabel("Frequency")
    ax2.set_title(f"Distribution of {subject_choice} Scores")
    st.pyplot(fig2)

# Chart 6: Correlation Heatmap
with row2_col3:
    st.subheader("🔗 Subject Correlation Heatmap")
    corr = df[subjects].corr()
    fig3, ax3 = plt.subplots()
    cax = ax3.matshow(corr, cmap="coolwarm")
    fig3.colorbar(cax)
    ax3.set_xticks(range(len(subjects)))
    ax3.set_yticks(range(len(subjects)))
    ax3.set_xticklabels(subjects, rotation=45)
    ax3.set_yticklabels(subjects)
    st.pyplot(fig3)

# ----------------------------------------------------------
# Data Table
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📋 Complete Student Data")
st.dataframe(df)






