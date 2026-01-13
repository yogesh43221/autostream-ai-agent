"""
RAG Node
Answers product questions using retrieved context from knowledge base.
"""
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from app.state import AgentState
from app.rag.retriever import get_retriever
import os


def rag_node(state: AgentState) -> AgentState:
    """
    Answer user question using RAG.
    
    Process:
        1. Retrieve relevant documents from knowledge base
        2. Pass context + question to LLM
        3. Generate answer strictly from context
    
    Args:
        state: Current agent state
        
    Returns:
        Updated state with RAG response
    """
    # Get last user message
    user_question = state['messages'][-1].content
    
    # Retrieve relevant context
    retriever = get_retriever()
    relevant_docs = retriever.retrieve(user_question, top_k=2)
    context = "\n\n".join(relevant_docs)
    
    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )
    
    # RAG prompt
    prompt = f"""You are a helpful assistant for AutoStream, an AI-powered video editing SaaS platform.

Answer the user's question using ONLY the information provided in the context below. If the context doesn't contain enough information to answer the question, say so politely.

Context:
{context}

User question: {user_question}

Provide a clear, concise answer based on the context above."""
    
    response = llm.invoke(prompt)
    
    state['messages'].append(AIMessage(content=response.content))
    return state
