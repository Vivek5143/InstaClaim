📢 InstaClaim - Insurance Claim Support Chatbot 💬
An AI-powered Insurance Support Chatbot built using Streamlit, LangChain, and Ollama LLMs, with OCR (Image-to-Text) support for reading insurance documents and images.

✨ Features:
✅ Insurance-specific chatbot conversations
✅ Supports multiple Ollama models (like Mistral, Llama3, Gemma, etc.)
✅ Upload insurance documents/images and extract text using Tesseract OCR
✅ Clean Streamlit Web UI
✅ Maintains chat history
✅ Dynamic model selection
✅ Image preview + extracted text display

🛠️ Tech Stack:
Python 🐍
Streamlit 📲
LangChain 🧠
Ollama (Local LLM Server) 🤖
pytesseract (OCR) 🖼️
Pillow (Image processing)
Import / Library	Why it is used in your chatbot project
from langchain.callbacks.base import BaseCallbackHandler	✅ This handles streaming of LLM (Large Language Model) responses in real-time inside the Streamlit UI. This lets you see the AI's answer building word by word (streamed).
from langchain.chat_models import ChatOllama	✅ This connects LangChain with Ollama models (like Mistral, Phi3) running locally on your machine. It sends your prompt to Ollama and gets AI replies.
from langchain.schema import HumanMessage, AIMessage	✅ Helps store and structure chat history in a chat-like format (separating Human and AI messages). This is needed by LangChain to understand multi-turn conversations.
import urllib.request, json	✅ Used for API communication with the Ollama server to get the list of installed models (via Ollama /api/tags endpoint).
import streamlit as st	✅ This is for creating the Streamlit web-based User Interface. Used for building buttons, inputs, sidebar, chat layout, etc.
from PIL import Image	✅ PIL (Python Imaging Library) helps to open, read and display uploaded images (insurance documents, forms, etc.).
import pytesseract	✅ This is the OCR engine (Optical Character Recognition). It reads text content from uploaded images (scanned documents).
🚀 Quick Start:
✅ 1. Clone the Repository:
git clone https://github.com/Vivek5143/instaclaim-insurance-chatbot.git
cd instaclaim-insurance-chatbot
✅ 2. Set up Virtual Environment (Recommended):

python -m venv .venv
.venv\Scripts\activate   # On Windows
✅ 3. Install Python Dependencies:

pip install -r requirements.txt
✅ 4. Install Tesseract OCR (For Image-to-Text Extraction): Download from: https://github.com/tesseract-ocr/tesseract

After installation, update this line in your main.py file:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
(Change the path if your installation location is different.)
✅ 5. Start Ollama Server & Pull Required LLM Models:

ollama pull mistral
ollama pull llama3
ollama pull gemma
Make sure Ollama is running on:
http://localhost:11434
✅ 6. Run the Chatbot Locally:

streamlit run main.py
After running, open your browser and go to:


Current Project Customization & Deployment: Vivek5143

✅ Possible Future Improvements: Deploy on Streamlit Cloud or Hugging Face Spaces

Add PDF document reading

Add voice-to-text support

Style improvements and advanced UI

Persistent conversation history (database or file)

Screenshot 2025-06-27 224127 Screenshot 2025-06-27 224319 Screenshot 2025-06-27 224456 Screenshot 2025-06-27 224624

✅ License: This project is intended for learning and demonstration purposes only.

Made with ❤️ for Insurance Support Chatbot Development 🚀