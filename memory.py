import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb

load_dotenv()

db=SqliteDb(db_file="agno.db")
db.clear_memories()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def build_agent():
    return Agent(
        db=db,
        model=Groq(
            id="qwen/qwen3.8-27b",
            api_key=GROQ_API_KEY,
            request_params={"max_completion_tokens": 100}
        ),
        markdown=True,
        add_history_to_context=True, #The agent can use the previous message to answer your follow-up question.
        #enable_user_memories=True  #useful information about the user that can be retained 
        #and reused across conversations
        #enable_agentic_memory=True → let the 
        # agent decide when to save or update memories.
    )


agent = build_agent()

agent.print_response(
    "What is the capital of india?"
)

agent.print_response(
    "What is the best time to visit it?"
)



# Remember the difference:
# - add_history_to_context=True → use previous conversation messages.
# - enable_user_memories=True → automatically process messages for useful memories.
# - enable_agentic_memory=True → let the agent decide when to save or update memories.