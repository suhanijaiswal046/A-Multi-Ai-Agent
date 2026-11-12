# 🤖 AI Agent Hub – Multi-Agent AI Application

An interactive **Multi-Agent AI Application** built using **Agno, Groq, and Streamlit**. The project brings multiple specialized AI agents together into a single interface to perform different tasks, including web research, financial analysis, multilingual responses, conversational memory, and YouTube video analysis.

Each agent has its own role, instructions, tools, and capabilities.

## ✨ Features

### 1. 🤖 General AI Agent
- Answers general questions.
- Performs web searches using DuckDuckGo.
- Uses real-time date and time context.
- Generates structured Markdown responses.

### 2. 💰 Finance Agent
- Retrieves stock market information using YFinance.
- Researches financial information using DuckDuckGo.
- Provides stock prices and analyst recommendations.
- Presents financial information in structured tables.

### 3. 👥 Multi-Agent Language Team
A team of three specialized AI agents:
- English Agent – Responds in English.
- Hindi Agent – Responds in Hindi.
- Chinese Agent – Responds in Chinese.

All three agents collaborate to answer the same query in their respective languages.

### 4. 🧠 Memory Agent
- Maintains conversational history.
- Uses SQLite for persistent database storage.
- Supports contextual follow-up questions.
- Uses previous messages to generate more relevant responses.

### 5. ▶️ YouTube Video Analyzer
- Analyzes YouTube videos using available captions and metadata.
- Extracts important topics.
- Generates video summaries.
- Identifies key learning points.
- Provides timestamps when available.

## 🏗️ Project Architecture

```text
                  User
                    |
                    v
             Streamlit UI
                    |
                    v
              Agent Selection
                    |
       +------------+------------+
       |            |            |
       v            v            v
   AI Agent    Finance Agent  Language Team
       |            |            |
       v            v            v
  DuckDuckGo    YFinance      English Agent
                DuckDuckGo    Hindi Agent
                              Chinese Agent

       +------------+------------+
       |                         |
       v                         v
  Memory Agent             YouTube Agent
       |                         |
       v                         v
  SQLite Database          YouTube Tools
       |                         |
       +------------+------------+
                    |
                    v
              Groq LLM
                    |
                    v
             AI Response
                    |
                    v
             Streamlit UI
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Agno | AI agent and multi-agent framework |
| Groq | LLM inference |
| Qwen | Language model |
| Streamlit | Interactive web interface |
| DuckDuckGo | Web search |
| YFinance | Financial data retrieval |
| YouTube Tools | Video captions and metadata |
| SQLite | Persistent database storage |
| Python-dotenv | Environment variable management |

## 📂 Project Structure

```text
A-Multi-Ai-Agent/
│
├── agent.py              # General AI agent
├── finance.py            # Finance research agent
├── team.py               # Multi-agent language team
├── memory.py             # Memory-enabled AI agent
├── youtube_analyzer.py   # YouTube video analyzer
│
├── ui.py                 # Streamlit application
├── requirements.txt      # Project dependencies
├── .env                  # API keys (not committed)
├── .gitignore             # Ignored files
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/suhanijaiswal046/A-Multi-Ai-Agent.git

cd A-Multi-Ai-Agent
```

### 2. Create a virtual environment

```bash
python -m venv myenv
```

Activate it on Windows:

```bash
myenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

**Important:** Never upload your `.env` file or expose your API keys on GitHub.

### 5. Run the application

```bash
streamlit run ui.py
```

The application will open in your browser.

## 🔄 How It Works

1. The user opens the Streamlit application.
2. The user selects an AI agent from the sidebar.
3. The selected agent is initialized using Agno.
4. The agent receives the user's query.
5. The Groq-powered language model processes the request.
6. When required, the agent calls its assigned tools.
7. The agent generates a response.
8. Streamlit displays the response in the chat interface.

## 🧠 Key Concepts Implemented

- AI Agents and Agent Configuration
- Tool Integration and Tool Calling
- Multi-Agent Collaboration
- Role-Based Agent Instructions
- Conversational Memory
- SQLite Database Integration
- LLM Inference using Groq
- Session State Management in Streamlit
- Real-Time Information Retrieval
- YouTube Content Analysis

## 🚀 Future Enhancements

- Add an intelligent supervisor agent for automatic task routing.
- Implement agent-to-agent communication.
- Add Human-in-the-Loop (HITL) functionality.
- Introduce advanced long-term memory.
- Add conversation export functionality.
- Improve the UI with agent-specific dashboards.
- Add authentication and user-specific conversations.

## 👩‍💻 Author

**Suhani Jaiswal**

B.Tech – Computer Science and Engineering

[GitHub Profile](https://github.com/suhanijaiswal046)

---

⭐ If you find this project interesting, consider giving it a star!
