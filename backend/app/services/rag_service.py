from sentence_transformers import SentenceTransformer
import openai
import numpy as np
import faiss

# Initialize once
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
docs = []

def add_document(text: str):
    embedding = model.encode([text])[0]
    index.add(np.array([embedding]).astype("float32"))
    docs.append(text)

def answer_query(query: str):
    q_emb = model.encode([query])[0]

    D, I = index.search(np.array([q_emb]).astype("float32"), k=1)
    context = docs[I[0][0]] if docs else "No context available"

    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ]
    )

    return completion.choices[0].message["content"], context