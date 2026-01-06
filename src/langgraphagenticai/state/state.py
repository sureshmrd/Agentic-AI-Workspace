from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    represents the structure of the State of the graph
    """
    messages : Annotated[List,add_messages]
