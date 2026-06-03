from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

memory_texts = []

dimension = 384

index = faiss.IndexFlatL2(
    dimension
)

def store_memory(text):

    embedding = model.encode([text])

    vector = np.array(
        embedding,
        dtype="float32"
    )

    index.add(vector)

    memory_texts.append(text)

    return "Memory stored."

def search_memory(query):

    if len(memory_texts) == 0:
        return "No memories stored."

    embedding = model.encode([query])

    vector = np.array(
        embedding,
        dtype="float32"
    )

    distances, indices = index.search(
        vector,
        3
    )

    results = []

    for idx in indices[0]:

        if idx < len(memory_texts):

            results.append(
                memory_texts[idx]
            )

    return "\n".join(results)