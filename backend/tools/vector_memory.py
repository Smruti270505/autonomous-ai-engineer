from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

memory_texts = []
MEMORY_FILE = "memory.pkl"

dimension = 384

index = faiss.IndexFlatL2(
    dimension
)
if os.path.exists(MEMORY_FILE):

    with open(
        MEMORY_FILE,
        "rb"
    ) as f:

        memory_texts = pickle.load(f)

        embeddings = model.encode(
            memory_texts
        )

        vector = np.array(
            embeddings,
            dtype="float32"
        )

        index.add(vector)
def store_memory(text):

    embedding = model.encode([text])

    vector = np.array(
        embedding,
        dtype="float32"
    )

    index.add(vector)

    memory_texts.append(text)

    with open(
    MEMORY_FILE,
    "wb"
) as f:

     pickle.dump(
        memory_texts,
        f
    )

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