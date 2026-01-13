"""
RAG Retriever
Semantic search over knowledge base using local embeddings (zero-cost).
"""
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np
from .loader import load_knowledge_base


class LocalRetriever:
    """
    Local semantic search using sentence-transformers.
    No external API calls - completely free.
    """
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize retriever with local embedding model.
        
        Args:
            model_name: HuggingFace model name (default: all-MiniLM-L6-v2)
        """
        print(f"Loading embedding model: {model_name}...")
        self.model = SentenceTransformer(model_name)
        
        # Load and embed knowledge base
        self.documents = load_knowledge_base()
        self.contents = [doc['content'] for doc in self.documents]
        
        print("Embedding knowledge base...")
        self.embeddings = self.model.encode(self.contents, convert_to_numpy=True)
        print(f"Indexed {len(self.documents)} documents")
    
    def retrieve(self, query: str, top_k: int = 2) -> List[str]:
        """
        Retrieve top-k most relevant documents for a query.
        
        Args:
            query: User question
            top_k: Number of documents to retrieve
            
        Returns:
            List of relevant document contents
        """
        # Embed query
        query_embedding = self.model.encode([query], convert_to_numpy=True)[0]
        
        # Compute cosine similarity
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        
        # Get top-k indices
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        # Return top documents
        return [self.contents[i] for i in top_indices]


# Global retriever instance (initialized once)
_retriever = None


def get_retriever() -> LocalRetriever:
    """Get or create global retriever instance."""
    global _retriever
    if _retriever is None:
        _retriever = LocalRetriever()
    return _retriever


if __name__ == "__main__":
    # Test the retriever
    retriever = get_retriever()
    
    test_queries = [
        "What are your pricing plans?",
        "Do you offer refunds?",
        "What's included in the Pro plan?"
    ]
    
    for query in test_queries:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print(f"{'='*60}")
        results = retriever.retrieve(query, top_k=2)
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result}")
