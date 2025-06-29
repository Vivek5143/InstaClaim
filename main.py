from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np
import urllib.request

# ✅ Set Tesseract OCR Path (For Windows users)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ✅ Streaming handler for LLM token output
class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

# ✅ Preprocess uploaded image (grayscale + threshold)
def preprocess_streamlit_image(uploaded_file):
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh

# ✅ OCR Text Extraction
def extract_text_from_image(uploaded_file):
    try:
        preprocessed_image = preprocess_streamlit_image(uploaded_file)
        text = pytesseract.image_to_string(preprocessed_image)
        return text
    except Exception as e:
        return f"Error reading image: {e}"

# ✅ Summarize long OCR text
def summarize_text(text):
    return text if len(text) <= 300 else f"Document Summary: {text[:300]}..."

# ✅ Ollama Health Check Function
def check_ollama_server(ollama_url="http://localhost:11434"):
    try:
        with urllib.request.urlopen(ollama_url) as response:
            if response.status == 200:
                return True
    except Exception as e:
        print(f"Ollama server check failed: {e}")
    return False

# ✅ App Title
st.title("Welcome to InstaClaim - Your Insurance Claim Assistant")

with st.sidebar:
    st.header("Ollama Model Used")
    ollama_model = "phi3:mini"  # Fixed model
    st.markdown(f"**Using Model:** `{ollama_model}`")

    if st.button("Clear Chat History", type="primary"):
        st.session_state["messages"] = [
            AIMessage(content="Hello! I’m here to assist you with any insurance claim-related queries. 😊")
        ]

# ✅ Initialize Chat History
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        AIMessage(content="Hello! I’m here to assist you with any insurance claim-related queries. 😊")
    ]

# ✅ Display Chat History (Black & Gold UI)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.markdown(f"<div style='padding:10px; border-radius:8px; text-align:right;'>🙂 {msg.content}</div>", unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f"<div style='color:#FFD700; padding:10px; border-radius:8px;'>🤖 {msg.content}</div>", unsafe_allow_html=True)

# ✅ File Upload & Backend OCR Context Injection (No UI text display)
with st.expander("📄 Upload Insurance Documents / Images (Optional)"):
    uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        extracted_text = extract_text_from_image(uploaded_file)
        if extracted_text.strip():
            summarized_text = summarize_text(extracted_text)

            # ✅ Remove old OCR system messages if any
            st.session_state.messages = [
                msg for msg in st.session_state.messages
                if not (isinstance(msg, SystemMessage) and "uploaded an insurance document" in msg.content)
            ]

            # ✅ Inject OCR as SystemMessage (backend-only, not shown to user)
            st.session_state.messages.insert(
                0,
                SystemMessage(content=f"The user has uploaded an insurance document containing the following details:\n{summarized_text}\nPlease use this information while answering any insurance-related queries.")
            )
            st.success("✅ Insurance document analyzed and context sent to AI.")
        else:
            st.warning("⚠️ No readable text found in the uploaded image.")

# ✅ Chat Input (English-only)
prompt = st.chat_input("Type your insurance-related query here...")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        # ✅ Ollama Server Health Check Before LLM Call
        ollama_server_url = "http://localhost:11434"
        if not check_ollama_server(ollama_server_url):
            fallback_message = "🚫 Hey there! It looks like our AI assistant is temporarily down due to a technical issue with Ollama. Please try again in a few minutes. 😊"
            st.warning(fallback_message)
            st.session_state.messages.append(AIMessage(content=fallback_message))
            st.stop()

        # ✅ Stream LLM Response (limiting history for speed)
        stream_handler = StreamHandler(st.empty())
        messages_for_llm = st.session_state.messages[-10:]
        llm = ChatOllama(model=ollama_model, streaming=True, callbacks=[stream_handler])
        response = llm(messages_for_llm)
        st.session_state.messages.append(AIMessage(content=response.content))
