from tools.vector_memory import search_memory

def retrieve_context(query):

    memories = search_memory(query)

    return memories