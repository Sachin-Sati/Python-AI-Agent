# import libraries
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime

# web search
search = DuckDuckGoSearchRun()
@tool
def web_search(query: str) -> str:
    """"Search the web for current information
    Args:
        query (str): search query / question to answer
        
    Returns:
        str: relevant search results"""
    return search.run(query)

# wikipedia search
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# save to file
@tool
def save_to_file(content: str, filename:str = 'research_output.txt') -> str:
    """Save final output/summary to a timestamped file

    IMPORTANT: Unless the user explicitly asks for a different filename,
    ALWAYS use filename = 'research_output.txt'
    Do NOT invent creative names like summary.md, output_final.txt, etc.

    Args:
        content (str): research output/summary to save
        filename (str): name of the file (default: 'research_output.txt')
        
    Returns:
        str: confirmation message"""
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    formatted_txt = f"--- Research Output --- \nTimestamp: {timestamp} \n\n{content}\n\n"
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(formatted_txt)
    return f"Content saved successfully to {filename}"