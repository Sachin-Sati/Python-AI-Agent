# supress warning about pydantic v1 and python 3.14
import warnings
warnings.filterwarnings(
    "ignore",
    message="Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater",
    category=UserWarning,
    module="langchain_core._api.deprecation"
)

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.messages import SystemMessage, HumanMessage
from tools import web_search, wiki_tool, save_to_file

# load env variable file
load_dotenv() 

# response schema
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# llm models (not free anymore)
# llm = ChatOpenAI(model="gpt-4o-mini")
# llm = ChatAnthropic(model="claude-3-5-sonnet-20241002")

# initialize Groq LLM
llm = ChatGroq(model='llama-3.3-70b-versatile')

# prompt template
system_prompt = """
        You are a concise, factual research assistant.
        Use tools when necessary to get accurate, up-to-date information.
        Think step-by-step, but be brief.
        After gathering information (if needed), provide a final answer using **only** the structured JSON format — no extra text, no markdown, no explanations outside the JSON.
    """

# create agent
agent = create_agent(
    model=llm,
    tools=[web_search, wiki_tool, save_to_file],
    system_prompt=system_prompt,
    response_format=ResearchResponse
)

# invoke agent with user query
query = input("What can help you research today?: ")
if not query:
    print("No query provided.")
else:
    # invoke agent and get response
    response = agent.invoke({"messages":[HumanMessage(content=query)]})

    # parse response into structured format
    structured: ResearchResponse | None = response.get('structured_response')

    if structured:
        # print structured response
        print("Topic:", structured.topic)
        print("Summary:", structured.summary)
        print("Sources:", structured.sources)
        print("Tools Used:", structured.tools_used)
    else:
        # print fallback message
        last_msg = response["messages"][-1]
        print("\nNo structured response found. Last message:", last_msg)