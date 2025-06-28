from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage, AIMessage
import urllib.request, json
import streamlit as st
from PIL import Image
import pytesseract

# ✅ For Windows users - Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ✅ Fetch Ollama models (Optional: Here, only 'mistral' and 'phi3' for sidebar dropdown)
@st.cache_resource
def get_ollama_models(ollama_server_url):
    api_tags = "/api/tags"
    models = []
    try:
        with urllib.request.urlopen(ollama_server_url + api_tags) as tags:
            response = json.load(tags)
            models = [model['name'].replace(":latest", "") for model in response['models']]
    except Exception as e:
        st.error(f"Failed to connect to Ollama server. Error: {e}")
    return tuple(models)

# ✅ Custom Streamlit callback handler for token streaming
class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

# ✅ OCR image text extraction
def extract_text_from_image(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error reading image: {e}"

# ✅ Streamlit UI
st.title("Welcome to the InstaClaim")

with st.sidebar:
    st.header("Ollama Model Selection")
    # ollama_server = st.text_input("Ollama API Server", value="http://localhost:11434")
    allowed_models = ["phi3"]
    ollama_model = st.selectbox("Choose Ollama Model", allowed_models, index=0)

    st.markdown("""
    Changing model won't clear chat history.  
    Click below to clear chat history manually.
    """)
    if st.button("Clear Chat History", type="primary"):
        st.session_state["messages"] = [
            AIMessage(content="Hello! I’m here to assist you with any insurance claim-related queries. 😊")
        ]

# ✅ Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        AIMessage(content="Hello! I’m here to assist you with any insurance claim-related queries. 😊")
    ]

# ✅ Display Chat History with colored message bubbles
for msg in st.session_state.messages:
    if msg.type == "human":
        st.markdown(f"<div style='padding:10px; border-radius:8px; text-align:right;'>🙂 {msg.content}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color:#FFD700; padding:10px; border-radius:8px;'>🤖 {msg.content}</div>", unsafe_allow_html=True)

# ✅ File Upload Section
with st.expander("📄 Upload Insurance Documents / Images (Optional)"):
    uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, use_column_width=True, caption="Uploaded Image Preview")
        extracted_text = extract_text_from_image(uploaded_file)
        if extracted_text.strip():
            st.success("✅ Text extracted from image:")
            st.text_area("Extracted Text:", value=extracted_text, height=150)
            
            # ✅ NEW: Append extracted text as Human Message for LLM context
            st.session_state.messages.append(
                HumanMessage(content=f"The user uploaded an insurance document with the following content:\n{extracted_text}")
            )
        else:
            st.warning("⚠️ No readable text found in the image.")

# ✅ Chat input box (Must stay outside expander/columns)
prompt = st.chat_input("Type your insurance-related query here...")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    if not ollama_model:
        st.warning("Please select a model in the sidebar.")
        st.stop()

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatOllama(model=ollama_model, streaming=True, callbacks=[stream_handler])
        response = llm(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
