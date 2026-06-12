from langchain.agents import AgentExecutor
from langchain.agents import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from config import GOOGLE_API_KEY
from tools.movie_search import movie_tool


def build_prompt():

    template = """
You are an Interactive Movie Recommendation Agent.

When a decade is mentioned,
convert it into a release year range before using the tool.

Examples:

90s -> 1990-1999
80s -> 1980-1989
2000s -> 2000-2009

Available tools:

{tools}

Tool names:

{tool_names}

Use this format:

Question:
Thought:
Action:
Action Input:
Observation:
Thought:
Final Answer:

For Final Answer use:

Best Match Found

Title:
Year:
TMDB Score:
Reason:
Overview:

Question: {input}

{agent_scratchpad}
"""

    return PromptTemplate.from_template(template)


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0,
)

agent = create_react_agent(
    llm=llm,
    tools=[movie_tool],
    prompt=build_prompt(),
)

executor = AgentExecutor(
    agent=agent,
    tools=[movie_tool],
    verbose=True,
    handle_parsing_errors=True,
)

query = input("Enter request: ")

result = executor.invoke(
    {"input": query}
)

print("\n")
print(result["output"])