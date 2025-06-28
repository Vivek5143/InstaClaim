# 📢 InstaClaim - Insurance Claim Support Chatbot 💬

A smart, **AI-powered insurance claim assistant chatbot** built using **LangChain**, **Streamlit**, **OCR (Tesseract)**, and **Ollama's Phi3 LLM**, designed to help users **understand**, **analyze**, and **process insurance claim queries and documents**.

---

## 🚀 About the Project

Filing an insurance claim is often **confusing**, **slow**, and **document-heavy**.  
**InstaClaim solves this by:**

- ✅ Allowing users to **upload images of insurance documents (JPG/PNG)**
- ✅ **Extracting important text** using **OCR (Tesseract)**
- ✅ **Analyzing the extracted text** and giving **insurance-specific guidance**
- ✅ Answering user queries in a **conversational AI chat format**
- ✅ Running **locally** using **Ollama's Phi3 model** (No external API keys needed)

---

## ✨ Features 


- ✅ **Model Support:**  
  Focused exclusively on **Phi-3 (via Ollama)** for **local LLM inferencing**.

- ✅ **Streamlit UI:**  
   **sleek Black and Gold theme** for **presentation appeal**.

- ✅ **OCR + Context-aware AI:**  
  - Automatically **extracts text** from uploaded **insurance images** using **Tesseract OCR**.  
  - **Injects the extracted content into the AI chat** for **smarter, context-based responses**.

---

## 🏗️ Tech Stack Used

| Feature           | Technology                        |
|-------------------|-----------------------------------|
| Chatbot UI        | Streamlit + LangChain             |
| Local LLM         | Ollama (**Phi3 model only**)       |
| OCR               | Tesseract                         |
| Text Extraction   | pytesseract + PIL                |
| Backend Handling  | Python                           |

---

## 🧑‍💻 Installation & Run Locally

```bash
# Clone the repo
git clone https://github.com/Vivek5143/instaclaim-insurance-chatbot.git
cd instaclaim-insurance-chatbot

# Setup virtual environment (For Windows users)
python -m venv .venv
.\.venv\Scripts\activate

# Install required libraries
pip install -r requirements.txt

# Run Ollama Server (Ensure Phi3 model is pulled)
ollama serve

# Run Streamlit App
streamlit run main.py
```
# 📝 Usage Instructions

✅ **Open Streamlit UI** (after running the above setup commands)

✅ **Choose Phi3 model** from the sidebar  
*(Model selector already filtered to Phi3 for simplicity)*

✅ **Upload insurance document image (optional)**  
*(Supported formats: PNG, JPG, JPEG)*

✅ **Ask your insurance-related query**  
*(Example: "How do I claim for hospitalization?" or "Is my policy covering theft?")*

✅ **Get instant, context-aware, insurance-specific AI guidance!**

---

## 📑 License and Reference Attribution:

This project is released under the **MIT License**.

**Reference Project (Inspiration & Learning Source):**  
[ai-chatbot-ollama by Karim Lalani (2023)](https://github.com/karim-lalani/ai-chatbot-ollama)

While this project draws **conceptual reference and learning inspiration** from the above open-source project,  
**InstaClaim has been independently customized and redesigned by Vivek Dalvi for the DSW Hackathon 2025**,  
focusing specifically on the **insurance claim support domain** with added OCR, UI theming, and Phi3 LLM integration.


## 📌 Important Notes for Judges / Panel Members

✅ **All LLM processing happens locally** using **Ollama Phi3 model**

✅ **No external API keys or cloud services used**

✅ Fully **customized for the insurance claim domain**

✅ Demonstrates **OCR → NLP → LLM pipeline integration**

✅ **Ethical open-source usage** with **proper attribution**

✅ Ready for **offline testing**, **local demo**, and **hackathon showcase**

---
