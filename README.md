# 🛋️ IKEA GenAI Assistant

An AI-powered IKEA Home Decor Assistant built using **Python, Streamlit, LangChain, FAISS, Hugging Face and Google Gemini**.

The application helps users search IKEA-style products, generate product descriptions, create realistic room images, and analyze customer reviews using Generative AI.

---

## 🚀 Features

### 1. 🔎 RAG Chatbot

The RAG (Retrieval-Augmented Generation) chatbot allows users to ask questions about IKEA products.

It uses:

- FAISS Vector Database
- Hugging Face Embeddings
- LangChain
- Google Gemini
- Semantic Search

Users can ask questions such as:

- Which products are suitable for a bedroom?
- Show me affordable storage furniture.
- What is the price of a particular product?
- Which furniture is suitable for a modern room?

---

### 2. ✍️ Product Description Generator

Generate professional product descriptions using Google Gemini.

Users can provide:

- Product name
- Product category
- Material
- Features
- Price
- Style

The AI generates a polished product description suitable for an e-commerce website.

---

### 3. 🖼️ AI Image Generator

Generate realistic interior room images based on user requirements.

Users can specify:

- Furniture
- Interior style
- Room requirements

The application uses **Stable Diffusion** locally to generate the room image.

Example:

> Modern Scandinavian bedroom with IKEA-style furniture, wooden flooring, indoor plants and natural daylight.

---

### 4. 📊 Review Analyzer

The Review Analyzer processes customer reviews and performs sentiment analysis.

It can identify:

- Positive reviews
- Negative reviews
- Neutral reviews
- Customer feedback patterns

TextBlob is used for sentiment analysis.

---

## 🧠 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Streamlit | Web application UI |
| LangChain | LLM & RAG workflow |
| Google Gemini | Generative AI |
| FAISS | Vector database |
| Hugging Face | Embeddings & AI models |
| Sentence Transformers | Text embeddings |
| Stable Diffusion | AI image generation |
| TextBlob | Sentiment analysis |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Plotly | Data visualization |
| Pillow | Image processing |

---

## 📁 Project Structure

```text
ikea-genai-capstone/
│
├── data/
│   ├── ikea.csv
│   ├── cleaned_ikea.csv
│   ├── reviews.csv
│   └── analyzed_reviews.csv
│
├── vectorstore/
│   └── faiss_index/
│       ├── index.faiss
│       └── index.pkl
│
├── modules/
│   ├── __init__.py
│   ├── rag_chatbot.py
│   ├── description_gen.py
│   ├── image_gen.py
│   └── review_analyzer.py
│
├── notebooks/
│   ├── 01_data_prep.ipynb
│   ├── 02_build_vectorstore.ipynb
│   ├── 03_test_rag.ipynb
│   ├── 04_test_image_gen.ipynb
│   └── ...
│
├── generated_room.png
├── app.py
├── generate_dataset.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── report.pdf