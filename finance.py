
import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Load environment variables
load_dotenv()

# Get Groq API key from .env
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Please check your .env file."
    )


def build_agent():
    agent = Agent(
        model=Groq(
            id="qwen/qwen3-32b",
            api_key=api_key,
            request_params={
                "max_completion_tokens": 100
            }
        ),
        tools=[
            YFinanceTools(),
            DuckDuckGoTools()
        ],
        markdown=True,
        add_datetime_to_context=True,
        description=(
            "You are an investment analyst who researches "
            "stock prices, analyst recommendations, "
            "and stock fundamentals."
        ),
        instructions=[
            "Use the provided tools whenever possible.",
            "Format responses using Markdown.",
            "Use tables to display financial data where possible.",
            "Provide concise, accurate, and useful analysis."
        ],
        debug_mode=True
    )

    return agent


if __name__ == "__main__":
    agent = build_agent()

    agent.print_response(
        "Share the MSFT stock price and analyst recommendations."
    )
