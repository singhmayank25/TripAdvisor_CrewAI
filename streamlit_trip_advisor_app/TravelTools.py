from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def search_web_tool(query: str) -> str:
    """
    Search the web using DuckDuckGo and return the top 5 results.
    """
    search = DuckDuckGoSearchResults(num_results=5)
    return search.run(query)

result = search_web_tool.run("Latest advancements in generative AI")
print(result)
