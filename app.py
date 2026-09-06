import os
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# =========================================================
# ENVIRONMENT
# =========================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="IKEA GenAI Assistant",
    page_icon="🛋️",
    layout="wide"
)


# =========================================================
# PROFESSIONAL DARK UI
# =========================================================

st.markdown("""
<style>

    /* Main application */
    .stApp {
        background-color: #111111;
        color: #ffffff;
    }

    /* Main content */
    .main {
        background-color: #111111;
    }

    /* Headings */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    /* Normal text */
    p, label, .stMarkdown {
        color: #eeeeee !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #181818;
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Text input */
    .stTextInput input {
        background-color: #222222 !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
        border-radius: 8px !important;
    }

    /* Text area */
    .stTextArea textarea {
        background-color: #222222 !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
        border-radius: 8px !important;
    }

    /* Select box */
    div[data-baseweb="select"] > div {
        background-color: #222222 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #555555 !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: #0058a3 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: 600 !important;
    }

    .stButton > button:hover {
        background-color: #0075d1 !important;
        color: #ffffff !important;
    }

    /* Alerts */
    .stAlert {
        border-radius: 10px !important;
    }

    /* Horizontal line */
    hr {
        border-color: #444444 !important;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LLM
# =========================================================

@st.cache_resource
def load_llm():

    return ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=GOOGLE_API_KEY
    )


# =========================================================
# VECTOR STORE
# =========================================================

@st.cache_resource
def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "vectorstore/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


# =========================================================
# HEADER
# =========================================================

st.title("🛋️ IKEA GenAI Assistant")

st.markdown(
    "### AI-Powered Home Decor Assistant"
)

st.write(
    "Explore IKEA products, generate product descriptions, "
    "create AI room designs, and analyze customer reviews."
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🛋️ IKEA GenAI")

st.sidebar.markdown(
    "### Choose a Module"
)

module = st.sidebar.selectbox(
    "Select Module",
    [
        "RAG Chatbot",
        "Description Generator",
        "Image Generator",
        "Review Analyzer"
    ],
    key="main_module_selector"
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    "### 🚀 Available Features"
)

st.sidebar.write("💬 Product Search")
st.sidebar.write("✍️ Description Generation")
st.sidebar.write("🎨 AI Room Design")
st.sidebar.write("⭐ Review Analysis")

st.sidebar.markdown("---")

st.sidebar.info(
    "Powered by Generative AI, "
    "FAISS and Stable Diffusion."
)


# =========================================================
# 1. RAG CHATBOT
# =========================================================

if module == "RAG Chatbot":

    st.header("💬 IKEA RAG Chatbot")

    st.write(
        "Ask questions about IKEA products and "
        "get answers from the product knowledge base."
    )

    question = st.text_input(
        "Ask something about IKEA products:",
        placeholder=(
            "Example: Which products are suitable "
            "for a modern living room?"
        )
    )

    if st.button(
        "🔍 Search",
        key="rag_button"
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Searching IKEA products..."
            ):

                try:

                    vectorstore = load_vectorstore()

                    docs = vectorstore.similarity_search(
                        question,
                        k=4
                    )

                    context = "\n\n".join(
                        [
                            doc.page_content
                            for doc in docs
                        ]
                    )

                    prompt = f"""
You are an IKEA product assistant.

Answer the user's question using ONLY the
information provided in the context.

Context:
{context}

User Question:
{question}

Give a clear and useful answer.

Mention product names and prices when available.

If the answer is not available in the context,
say that the information is not available.
"""

                    llm = load_llm()

                    response = llm.invoke(
                        prompt
                    )

                    st.success(
                        "Answer generated successfully! 🎉"
                    )

                    content = response.content

                    if isinstance(content, list):

                        text = "".join(
                            item.get("text", "")
                            for item in content
                            if isinstance(item, dict)
                        )

                    else:

                        text = str(content)

                    st.markdown(text)

                except Exception as e:

                    st.error(
                        f"RAG Error: {e}"
                    )


# =========================================================
# 2. DESCRIPTION GENERATOR
# =========================================================

elif module == "Description Generator":

    st.header(
        "✍️ Product Description Generator"
    )

    st.write(
        "Generate professional marketing descriptions "
        "for IKEA-style products."
    )

    product_name = st.text_input(
        "Product Name",
        placeholder="Example: BILLY Bookcase"
    )

    category = st.text_input(
        "Category",
        placeholder="Example: Furniture"
    )

    features = st.text_area(
        "Product Features",
        placeholder=(
            "Example: Wooden bookcase, 5 shelves, "
            "modern design, spacious storage"
        )
    )

    style = st.selectbox(
        "Writing Style",
        [
            "Modern",
            "Professional",
            "Minimalist",
            "Luxury",
            "Friendly"
        ]
    )

    if st.button(
        "✨ Generate Description",
        key="description_button"
    ):

        if not product_name or not features:

            st.warning(
                "Please enter product name and features."
            )

        else:

            with st.spinner(
                "Generating product description..."
            ):

                try:

                    llm = load_llm()

                    prompt = f"""
Create a professional IKEA-style
product description.

Product Name:
{product_name}

Category:
{category}

Features:
{features}

Writing Style:
{style}

Create:

1. Short product description
2. Key features
3. Main benefits
4. Suitable room/use
5. Attractive marketing description

Keep it clear, professional and
customer-friendly.
"""

                    response = llm.invoke(
                        prompt
                    )

                    st.success(
                        "Description generated successfully! 🎉"
                    )

                    content = response.content

                    if isinstance(content, list):

                        text = "".join(
                            item.get("text", "")
                            for item in content
                            if isinstance(item, dict)
                        )

                    else:

                        text = str(content)

                    st.markdown(text)

                except Exception as e:

                    st.error(
                        f"Description Generator Error: {e}"
                    )


# =========================================================
# 3. IMAGE GENERATOR
# =========================================================

elif module == "Image Generator":

    st.header(
        "🎨 AI Room Image Generator"
    )

    st.write(
        "Create an AI-generated interior room design "
        "using your local Stable Diffusion model."
    )

    st.info(
        "💡 Image generation runs locally on your CPU. "
        "The first generation may take several minutes."
    )

    furniture = st.text_input(
        "Furniture",
        placeholder=(
            "Example: Sofa, coffee table, bookshelf, TV unit"
        )
    )

    interior_style = st.selectbox(
        "Interior Style",
        [
            "Scandinavian",
            "Modern",
            "Minimalist",
            "Contemporary",
            "Cozy"
        ]
    )

    requirements = st.text_area(
        "Room Requirements",
        placeholder=(
            "Example: Bright living room, natural sunlight, "
            "indoor plants, wooden floor, large window"
        )
    )

    if st.button(
        "🎨 Generate AI Room",
        key="image_button"
    ):

        if not furniture:

            st.warning(
                "Please enter furniture details."
            )

        else:

            with st.spinner(
                "🎨 AI realistic room image "
                "generate ho rahi hai..."
            ):

                try:

                    from modules.image_gen import (
                        generate_room_image
                    )

                    image = generate_room_image(
                        furniture,
                        interior_style,
                        requirements
                    )

                    if image is not None:

                        st.success(
                            "AI Image Generated Successfully! 🎉"
                        )

                        st.image(
                            image,
                            caption="AI Generated IKEA Room",
                            use_container_width=True
                        )

                except Exception as e:

                    st.error(
                        f"Image Generator Error: {e}"
                    )


# =========================================================
# 4. REVIEW ANALYZER
# =========================================================

elif module == "Review Analyzer":

    st.header(
        "⭐ IKEA Review Analyzer"
    )

    st.write(
        "Analyze customer reviews using Generative AI."
    )

    reviews = st.text_area(
        "Paste customer reviews",
        height=250,
        placeholder="""Example:

The sofa is very comfortable and looks great.

The quality is good but assembly was difficult.

Excellent product for the price.
"""
    )

    if st.button(
        "📊 Analyze Reviews",
        key="review_button"
    ):

        if not reviews.strip():

            st.warning(
                "Please enter some reviews."
            )

        else:

            with st.spinner(
                "Analyzing customer reviews..."
            ):

                try:

                    llm = load_llm()

                    prompt = f"""
Analyze the following customer reviews.

Reviews:
{reviews}

Provide:

1. Overall sentiment
2. Positive points
3. Negative points
4. Common complaints
5. Customer satisfaction level
6. Final summary

Use clear headings and bullet points.
"""

                    response = llm.invoke(
                        prompt
                    )

                    st.success(
                        "Review analysis completed! 🎉"
                    )

                    content = response.content

                    if isinstance(content, list):

                        text = "".join(
                            item.get("text", "")
                            for item in content
                            if isinstance(item, dict)
                        )

                    else:

                        text = str(content)

                    st.markdown(text)

                except Exception as e:

                    st.error(
                        f"Review Analyzer Error: {e}"
                    )