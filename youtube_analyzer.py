
from textwrap import dedent
import os

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file."
    )


def build_youtube_agent():
    return Agent(
        name="YouTube Agent",

        model=Groq(
            id="qwen/qwen3.8-27b",
            api_key=GROQ_API_KEY,
            request_params={
                "max_completion_tokens": 500
            },
        ),

        tools=[
            YouTubeTools(
                enable_get_video_captions=True,
                enable_get_video_data=True,
                enable_get_video_timestamps=False,
                languages=["en"],
            )
        ],

        instructions=dedent("""\
            You are a YouTube video analysis expert.

            Analyze the video using available captions and metadata.

            1. OVERVIEW
            - Explain the video topic and type.
            - Give a brief overview of its content.

            2. KEY TOPICS
            - Identify 5-8 important topics.
            - Include timestamps when available.
            - Summarize each topic in 1-2 sentences.
            - Never invent timestamps.

            3. LEARNING POINTS
            - Highlight important concepts and demonstrations.
            - Use relevant emojis for educational or technical content.

            4. ACCURACY
            - Use only information supported by the available data.
            - Mention when captions or metadata are unavailable.
            - Keep the final report concise.
        """),

        markdown=True,
        add_datetime_to_context=True,
    )


if __name__ == "__main__":
    youtube_agent = build_youtube_agent()

    youtube_agent.print_response(
        "Analyze this YouTube video: "
        "https://www.youtube.com/watch?v=BOiDLE3oKe4. "
        "Give an overview, key topics with timestamps, "
        "and the main learning points.",
        stream=True,
    )
