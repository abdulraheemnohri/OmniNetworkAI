class MemorySystem:
    def __init__(self):
        self.memories = []

    def add_memory(self, text, metadata=None):
        self.memories.append({"text": text, "metadata": metadata})

    def search_memory(self, query, top_k=3):
        query = query.lower()
        results = [m for m in self.memories if query in m['text'].lower()]
        return results[:top_k]
