from pdf_utils import read_pdf, chunk_text
from embeddings import create_embeddings
from retriever import create_faiss_index, search_chunks
from llm import generate_answer

def main():
    file_path = r"C:\Users\Aadiluddin\Downloads\MOHAMMED_AADILUDDIN_QUAMRI_Statista.pdf"

    text = read_pdf(file_path)
    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)
    index = create_faiss_index(embeddings)

    while True:
        query = input("\nAsk a question (or 'exit'): ")

        if query.lower() == "exit":
            break

        results = search_chunks(query, chunks, index)
        context = "\n".join(results)

        answer = generate_answer(context, query)

        print("\n💡 Answer:\n", answer)


if __name__ == "__main__":
    main()