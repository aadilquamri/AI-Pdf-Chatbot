import streamlit as st
from pdf_utils import read_pdf, chunk_text
from embeddings import create_embeddings
from retriever import create_faiss_index, search_chunks
from llm import generate_answer
import tempfile

st.title("📄 PDF Chatbot")

# ✅ Upload file instead of typing path
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("PDF uploaded successfully!")

    text = read_pdf(file_path)
    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)
    index = create_faiss_index(embeddings)

    query = st.text_input("Ask a question")

    if query:
        results = search_chunks(query, chunks, index)
        context = "\n".join(results)

        answer = generate_answer(context, query)

        st.write("💡 Answer:")
        st.write(answer)        