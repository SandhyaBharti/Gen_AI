import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
import os

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Mistral Chat",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern design
st.markdown("""
    <style>
        * {
            margin: 0;
            padding: 0;
        }
        
        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 2rem 0;
        }
        
        .stChatMessage {
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            animation: slideIn 0.3s ease-out;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .stChatMessage.user {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 18px;
            margin-left: auto;
            margin-right: 0;
            max-width: 85%;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .stChatMessage.assistant {
            background: white;
            border-radius: 18px;
            margin-left: 0;
            margin-right: auto;
            max-width: 85%;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            border-left: 4px solid #667eea;
        }
        
        .chat-header {
            text-align: center;
            margin-bottom: 2rem;
            padding-top: 1rem;
        }
        
        .chat-header h1 {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }
        
        .chat-header p {
            color: #666;
            font-size: 1rem;
            font-weight: 400;
        }
        
        .input-container {
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 600px;
            padding: 1.5rem;
            background: linear-gradient(180deg, rgba(197, 207, 226, 0.8) 0%, rgba(197, 207, 226, 0.95) 100%);
            backdrop-filter: blur(10px);
            z-index: 100;
        }
        
        .stTextInput {
            width: 100%;
        }
        
        .stTextInput input {
            border-radius: 25px !important;
            border: 2px solid #667eea !important;
            padding: 12px 20px !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput input:focus {
            border-color: #764ba2 !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        }
        
        .messages-container {
            margin-bottom: 5rem;
        }
        
        .empty-state {
            text-align: center;
            padding: 3rem 1rem;
            color: #999;
        }
        
        .empty-state-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
        
        .empty-state h2 {
            color: #333;
            margin-bottom: 0.5rem;
        }
        
        .empty-state p {
            color: #999;
            font-size: 0.95rem;
        }
        
        /* Hide Streamlit default elements */
        .stDeployButton {
            display: none;
        }
        
        footer {
            display: none;
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = ChatMistralAI(model="mistral-small-2603")

# Header
st.markdown("""
    <div class="chat-header">
        <h1>💬 Mistral Chat</h1>
        <p>Chat with Mistral AI - Start a conversation</p>
    </div>
""", unsafe_allow_html=True)

# Messages container
st.markdown('<div class="messages-container">', unsafe_allow_html=True)

if len(st.session_state.messages) == 0:
    st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">💭</div>
            <h2>Start a Conversation</h2>
            <p>Ask me anything and I'll help you out!</p>
        </div>
    """, unsafe_allow_html=True)
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

st.markdown('</div>', unsafe_allow_html=True)

# Input container at the bottom
st.markdown('<div class="input-container">', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input(
    "Type your message...",
    key="chat_input",
    max_chars=None
)

st.markdown('</div>', unsafe_allow_html=True)

# Process user input
if user_input:
    # Add user message to session state
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get response from Mistral
    with st.spinner(""):
        response = st.session_state.model.invoke(user_input)
        assistant_message = response.content
    
    # Add assistant message to session state
    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(assistant_message)
    
    # Rerun to update the layout
    st.rerun()