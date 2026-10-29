import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def build_agent():
    return Agent(
        model=Groq(
            id="qwen/qwen3.8-27b",
            api_key=GROQ_API_KEY,
            request_params={"max_completion_tokens": 100}
        ),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )


agent = build_agent()

agent.print_response(
    "Is it safe to travel UAE today?"
)



