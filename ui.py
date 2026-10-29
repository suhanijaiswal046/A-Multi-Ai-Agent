# import streamlit as st
# from youtube_analyzer import build_youtube_agent

# st.set_page_config(
#     page_title="Youtube Video Analyzer",
#     layout="centered"
# )

# st.title("🎥 AI Youtube Video Analyzer")

# @st.cache_resource
# def get_agent():
#     return build_youtube_agent()


# agent = get_agent()

# # input box
# video_url = st.text_input("Enter Youtube Video Link") # str
# button = st.button("Analyze Video") # True/False

# if video_url and button:
#     with st.spinner("Analyzing video...."):
#         response = agent.run(
#             f"Analyze this video: {video_url}"
#         )

#     st.markdown("Analysis Report of Video:")
#     st.markdown(response.content)

import streamlit as st

from agent import build_agent as build_general_agent
from finance import build_agent as build_agent
from team import language_team
from memory import build_agent
from youtube_analyzer import build_youtube_agent


st.set_page_config(
    page_title="My AI Agent Hub",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 My AI Agent Hub")
st.caption("One interface for all your AI agents")

# Agent selection
agent_options = {
    "🤖 AI Agent": "ai",
    "💰 Finance Agent": "finance",
    "👥 Agent Team": "team",
    "🧠 Memory Agent": "memory",
    "▶️ YouTube Analyzer": "youtube",
}

selected_label = st.sidebar.radio(
    "Choose your agent",
    list(agent_options.keys()),
)

selected_agent = agent_options[selected_label]

# Create the selected agent only
@st.cache_resource
def load_agent(agent_name):
    if agent_name == "ai":
        return build_general_agent()

    if agent_name == "finance":
        return build_agent()

    if agent_name == "team":
        return language_team

    if agent_name == "memory":
        return build_agent()

    if agent_name == "youtube":
        return build_youtube_agent()

    raise ValueError("Unknown agent selected")


try:
    agent = load_agent(selected_agent)
except Exception as exc:
    st.error(f"Could not initialize this agent: {exc}")
    st.stop()

# Keep a separate conversation for each agent
if "conversations" not in st.session_state:
    st.session_state.conversations = {}

if selected_agent not in st.session_state.conversations:
    st.session_state.conversations[selected_agent] = []

messages = st.session_state.conversations[selected_agent]

# Display previous messages
for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
prompt = st.chat_input(
    "Ask a question or enter a YouTube URL..."
)

if prompt:
    messages.append({
        "role": "user",
        "content": prompt,
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner(f"{selected_label} is working..."):
            try:
                response = agent.run(prompt)
                answer = response.content

                if not isinstance(answer, str):
                    answer = str(answer)

                st.markdown(answer)

                messages.append({
                    "role": "assistant",
                    "content": answer,
                })

            except Exception as exc:
                st.error(f"Agent error: {exc}")
