# 🎬 GenAI Playground & MovieSage AI

Welcome to the **GenAI Playground & MovieSage AI** repository! This project serves as a comprehensive collection of learning experiments, chat implementations, embedding models, and interactive user interfaces built using **LangChain**, **Streamlit**, and various state-of-the-art LLM APIs (Gemini, Mistral, Groq, OpenAI, and Hugging Face).

---

## 🌟 Key Features

### 1. 🍿 MovieSage AI (`./MovieSageAI/`)
An intelligent movie information extraction assistant. Given a raw textual description of a movie, MovieSage AI parses it, extracts structured metadata, generates a concise summary, and returns the result in clean JSON format.
* **Core Logic (`./MovieSageAI/core.py`)**: Console-based JSON extraction using Mistral AI (`mistral-small-2603`).
* **Interactive UI (`./MovieSageAI/UIMovieSageBot.py`)**: A premium, highly styled Streamlit dashboard with a cinematic interface, custom dark mode styling, and dynamic scanning overlays.

### 2. 🎭 Personality Chatbot (`./chatmodel/`)
An interactive chatbot that allows users to chat with a variety of personalities, including Funny, Angry, Sarcastic, Sad, and Romantic.
* **Console Chatbot (`./chatmodel/Chatbot.py`)**: Command-line based chatbot.
* **Streamlit Chatbot (`./chatmodel/UIchatbot.py`)**: A premium Streamlit application with custom animations, message bubble styles tailored to each personality, and reactive glows.

### 3. 🧪 Embedding & Endpoint Demos (`./embeddingmodel/` & Root)
* **OpenAI Embeddings (`./embeddingmodel/embedding.py`)**: Demonstrates query embedding generation using OpenAI's `text-embedding-3-small`.
* **Hugging Face Embeddings (`./embeddingmodel/huggingface.embeddings.py`)**: Computes sentence embeddings using Hugging Face's `sentence-transformers/all-MiniLM-L6-v2`.
* **Multi-LLM Playground (`./Chat.py`)**: Shows side-by-side LangChain integrations with **Gemini** (`gemini-2.5-flash`), **Groq** (`openai/gpt-oss-120b`), and **Mistral AI** (`mistral-small-2603`).
* **Hugging Face Endpoint (`./Huggingface.py`)**: Directly integrates Hugging Face's hosted endpoint for `deepseek-ai/DeepSeek-V4-Flash`.

---

## 📁 Repository Structure

```text
├── MovieSageAI/
│   ├── core.py               # Core MovieSage AI prompt and extraction script
│   └── UIMovieSageBot.py     # Streamlit web application for MovieSage AI
├── chatmodel/
│   ├── Chatbot.py            # Console chatbot with selectable personalities
│   └── UIchatbot.py          # Custom styled Streamlit chatbot with personalities
├── embeddingmodel/
│   ├── embedding.py          # OpenAI text embeddings demo
│   └── huggingface.embeddings.py # Hugging Face sentence embeddings demo
├── Chat.py                   # Multi-LLM integration (Gemini, Groq, Mistral)
├── Huggingface.py            # DeepSeek LLM via Hugging Face Endpoint
├── requirements.txt          # Python dependencies
├── .env.example              # Template for API credentials
└── test.py                   # Verification script
```

---

## 🛠️ Setup & Installation

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/SandhyaBharti/Gen_AI.git
cd Gen_AI
```

### 3. Create a Virtual Environment
Initialize a virtual environment to manage project-specific dependencies:

**On Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
Install all required libraries specified in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the root directory and add your API credentials. You can use the template below:
```env
# Google Gemini API
GOOGLE_API_KEY=your_google_api_key_here

# Groq API
GROQ_API_KEY=your_groq_api_key_here

# Mistral AI API
MISTRAL_API_KEY=your_mistral_api_key_here

# OpenAI API (for embeddings)
OPENAI_API_KEY=your_openai_api_key_here

# Hugging Face Hub Token
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

---

## 🚀 Running the Applications

### Launch Streamlit Apps
To run the interactive web applications, launch them using streamlit from your terminal:

* **To run MovieSage AI UI:**
  ```bash
  streamlit run MovieSageAI/UIMovieSageBot.py
  ```
* **To run the Personality Chatbot UI:**
  ```bash
  streamlit run chatmodel/UIchatbot.py
  ```

### Run CLI/Console Apps
To run any of the terminal-based utility scripts:

* **Personality Chatbot CLI:**
  ```bash
  python chatmodel/Chatbot.py
  ```
* **Multi-LLM Playground:**
  ```bash
  python Chat.py
  ```
* **Hugging Face Endpoint Demo:**
  ```bash
  python Huggingface.py
  ```

---

## 🛠️ Tech Stack
* **Framework**: [LangChain](https://www.langchain.com/) (LangChain Core, Community, OpenAI, Google GenAI, Groq, Mistral, HuggingFace)
* **Frontend**: [Streamlit](https://streamlit.io/) with custom HTML/CSS injections for modern styling
* **LLM APIs**: Google Gemini, Groq, Mistral AI, Hugging Face, OpenAI
