
import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")


# Common model configuration
def get_model():
    return Groq(
        id="qwen/qwen3.8-27b",
        api_key=api_key,
        request_params={
            "max_completion_tokens": 150
        }
    )


# Agent 1: English
eng_agent = Agent(
    name="English Agent",
    role="You answer questions in English.",
    model=get_model(),
    instructions=[
        "Always answer in English."
    ]
)


# Agent 2: Chinese
chi_agent = Agent(
    name="Chinese Agent",
    role="You answer questions in Chinese.",
    model=get_model(),
    instructions=[
        "Always answer in Chinese."
    ]
)


# Agent 3: Hindi
hindi_agent = Agent(
    name="Hindi Agent",
    role="You answer questions in Hindi.",
    model=get_model(),
    instructions=[
        "Always answer in Hindi."
    ]
)


# Create the team
language_team = Team(
    name="Language Team",
    model=get_model(),
    members=[
        eng_agent,
        chi_agent,
        hindi_agent
    ],
    instructions=
       """ All member agents must respond to answer the query in their specific language. 
                        Do not route to just one agent.
                        Output the response of all agents.
                """,
    markdown=True,
    debug_mode=True
)


# Run the team
if __name__ == "__main__":
    language_team.print_response(
        "what is the capital of india?.",
        stream=True
    )
