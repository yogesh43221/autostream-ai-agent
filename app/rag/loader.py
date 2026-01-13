"""
Knowledge Base Loader
Loads and chunks the knowledge base JSON into retrievable documents.
"""
import json
from pathlib import Path
from typing import List, Dict


def load_knowledge_base() -> List[Dict[str, str]]:
    """
    Load knowledge base and convert to document chunks.
    
    Returns:
        List of documents with 'content' and 'metadata' fields
    """
    kb_path = Path(__file__).parent / "knowledge_base.json"
    
    with open(kb_path, 'r') as f:
        data = json.load(f)
    
    documents = []
    
    # Process plans
    for plan_key, plan_data in data['plans'].items():
        content = f"{plan_data['name']}: {plan_data['description']}"
        documents.append({
            'content': content,
            'metadata': {'type': 'plan', 'plan_name': plan_key}
        })
    
    # Process policies
    for policy_key, policy_data in data['policies'].items():
        content = f"{policy_data['title']}: {policy_data['description']}"
        documents.append({
            'content': content,
            'metadata': {'type': 'policy', 'policy_name': policy_key}
        })
    
    return documents


if __name__ == "__main__":
    # Test the loader
    docs = load_knowledge_base()
    for i, doc in enumerate(docs):
        print(f"\nDocument {i+1}:")
        print(f"Content: {doc['content']}")
        print(f"Metadata: {doc['metadata']}")
