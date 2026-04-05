# 🧠 Enhanced Q&A Chatbot with OpenAI

This project is an **Advanced Q&A Chatbot** built using **Streamlit**, **LangChain**, and **OpenAI’s GPT models**. It provides a clean, interactive interface for querying generative AI models with integrated tracing and debugging via LangSmith.

---

## ✨ Features
- 🤖 **Multiple GPT Models**: Supports `gpt-4o`, `gpt-4-turbo`, and `gpt-4` with easy model selection.
- 📜 **LangChain Integration**: Uses `ChatPromptTemplate` for structured and efficient prompt management.
- 🎛️ **Sidebar Settings**: Interactive sidebar for API key entry and model configuration.
- ⚡ **Real-time Interaction**: Instant responses through a sleek Streamlit interface.
- 📊 **Monitoring & Tracing**: Fully integrated with **LangSmith** for observability and debugging of LLM runs.
- 🔑 **Secure Config**: Environment variable management using `python-dotenv`.

---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) – UI framework for building web apps with Python
- [LangChain](https://www.langchain.com/) – Orchestration framework for LLM-based applications
- [OpenAI API](https://platform.openai.com/) – Powering AI responses with GPT models
- [LangSmith](https://www.langchain.com/langsmith) – Development platform for tracing and evaluation
- [Python Dotenv](https://pypi.org/project/python-dotenv/) – Managing environment variables

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/RohanJha2410/OpenAI-QnA-Chatbot.git
cd OpenAI-QnA-Chatbot
```

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables
Create a `.env` file in the project root to enable LangSmith tracing and set project names:
```bash
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=OpenAI-QA-Chatbot
```

---

## 🚀 Running the App
To start the chatbot, run:
```bash
streamlit run app.py
```

---

## 📖 Usage
- **API Key**: Enter your OpenAI API key in the sidebar (if not already set in `.env`).
- **Model Selection**: Choose your preferred GPT model from the dropdown menu in the sidebar.
- **Chatting**: Simply type your question in the main text box and get instant AI-generated answers.
- **Tracing**: All queries and responses will be logged to **LangSmith** if your API key is provided and tracing is enabled.

---

## 🌟 Future Improvements
- [ ] Add chat memory for persistent conversations.
- [ ] Support for document uploads and RAG (Retrieval-Augmented Generation).
- [ ] Custom prompt template configuration via UI.
- [ ] Deployment to Streamlit Cloud.

---

## 🤝 Contributing
Contributions are welcome! Please open an issue first to discuss any major changes you'd like to implement.

---

## 📜 License
This project is licensed under the MIT License.
