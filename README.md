# 📢 InstaClaim - Insurance Claim Support Chatbot 💬

A smart, **AI-powered insurance claim assistant chatbot** built using **LangChain**, **Streamlit**, **OCR (Tesseract)**, and **Ollama's Phi3 LLM**, designed to help users **understand**, **analyze**, and **process insurance claim queries and documents**.

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack Used](#-tech-stack-used)
- [Installation & Run Locally](#-installation--run-locally)
- [Usage Instructions](#-usage-instructions)
- [License and Reference Attribution](#-license-and-reference-attribution)
- [Important Notes for Judges / Panel Members](#-important-notes-for-judges--panel-members)

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
  Focused exclusively on **Phi-3:mini (via Ollama)** for **local LLM inferencing**.

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
| Local LLM         | Ollama (**Phi3:mini model only**)       |
| OCR               | Tesseract                         |
| Text Extraction   | pytesseract + PIL                |
| Backend Handling  | Python                           |

---

## 🧑‍💻 Installation & Run Locally


1. Clone the project repository
```
git clone https://github.com/Vivek5143/instaclaim-insurance-chatbot.git
cd InstaClaim
```
2. Create and activate a Virtual Environment (on Windows)
```
python -m venv .venv
.\.venv\Scripts\activate
```
3. Upgrade pip (optional but recommended)
```
python -m pip install --upgrade pip
```
4. Install all required Python dependencies
```
pip install -r requirements.txt
```
5. Download and Install Tesseract OCR (For Windows)
👉 [Download Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

6. After installing Tesseract, configure its path inside your project:
Edit your main.py file and set the path:
Example path (adjust if installed in different location):
```
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
7. Download Ollama and start the Ollama server:
👉 [Download Ollama for Windows](https://ollama.com/download)
Once installed, run the Ollama server (it will auto-start if installed properly):
```
ollama serve
```
8. Pull the required Ollama LLM model (Phi3 Mini in your case)
```
ollama pull phi3:mini
```
9. Finally, run your Streamlit app locally
```
streamlit run main.py
```
# 📝 Usage Instructions

✅ **Open Streamlit UI** (after running the above setup commands)


✅ **Upload insurance document image (optional)**  
*(Supported formats: PNG, JPG, JPEG)*

✅ **Ask your insurance-related query**  
*(Example: "How do I claim for hospitalization?" or "Is my policy covering theft?")*

✅ **Receive instant, context-aware, and insurance-specific AI assistance!**

---

## 🖥️ Screenshots

✅ **Chat Interface**

![Screenshot 2025-06-28 130239](https://github.com/user-attachments/assets/b6b9c722-1f2d-41d0-8fbd-a8d8c44eccac)

✅ **Bot Replying**

![Screenshot 2025-06-28 130454](https://github.com/user-attachments/assets/37c62121-42dd-4466-b9e5-7b722595a838)

✅ **OCR Uploaded**

![Screenshot 2025-06-28 163612](https://github.com/user-attachments/assets/c54f9107-1b7d-4730-a4d7-6c97e61461ac)

---

## 👨‍💻 Developer Contribution (By **Vivek Dalvi**)

- ✅ Integrated end-to-end **OCR → Text Summarization → AI Chat Context Injection**
- ✅ Designed and developed **Streamlit Black & Gold themed UI**
- ✅ Added **robust backend logic for handling image uploads, error handling, and user queries**
- ✅ Customized **LangChain with Ollama local LLM support**
- ✅ Ensured **no external APIs / cloud services dependency (Fully Offline AI Chatbot)**

---

## 📑 License and Reference Attribution:

This project is released under the **MIT License**.

**Reference Project (Inspiration & Learning Source):**  
[ai-chatbot-ollama by Karim Lalani (2023)](https://github.com/karim-lalani/ai-chatbot-ollama)

While this project draws **conceptual reference and learning inspiration** from the above open-source project,  
**InstaClaim has been independently customized and redesigned by Vivek Dalvi for the DSW Hackathon 2025**,  
focusing specifically on the **insurance claim support domain** with added OCR, UI theming, and Phi3 LLM integration.

## 🚀 Future Enhancements (Post Hackathon Plan)

- ✅ Add **Multi-language support** for regional insurance documents
- ✅ Integrate with **real insurance company APIs** for live claim status checking
- ✅ Deploy on **Cloud (AWS / GCP / Azure)** for broader user accessibility
- ✅ Add **voice input support** for better accessibility


## 📌 Important Notes for Judges / Panel Members

✅ **All LLM processing happens locally** using **Ollama Phi3 model**

✅ **No external API keys or cloud services used**

✅ Fully **customized for the insurance claim domain**

✅ Demonstrates **OCR → NLP → LLM pipeline integration**

✅ Ethically built on open-source foundations with proper author attributions

✅ Ready for **offline testing**, **local demo**, and **hackathon showcase**

---
