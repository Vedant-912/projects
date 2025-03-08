import streamlit as st
import PyPDF2  # For PDF text extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    # Combine job description with resumes
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Calculate cosine similarity
    job_description_vector = tfidf_matrix[0:1]
    resume_vectors = tfidf_matrix[1:]
    cosine_similarities = cosine_similarity(job_description_vector, resume_vectors).flatten()

    return cosine_similarities

# Streamlit app
st.title("AI Resume Screening & Candidate Ranking System")

# Job description input
st.header("Job Description")
job_description = st.text_area("Enter the job description")

# File Uploader
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("Ranked Resumes")

    # Extract text from uploaded resumes
    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text)

    # Rank resumes
    scores = rank_resumes(job_description, resumes)

    # Display ranked resumes with scores
    ranked_resumes = sorted(zip(uploaded_files, scores), key=lambda x: x[1], reverse=True)

    for idx, (file, score) in enumerate(ranked_resumes):
        st.subheader(f"Rank {idx + 1} (Similarity Score: {score:.2f})")
        st.write(f"**File Name:** {file.name}")
        st.write("**Resume Text:**")
        st.text(resumes[uploaded_files.index(file)])  # Display the resume text
        st.write("---")