from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_core.messages import HumanMessage

model = OllamaFunctions(
    model="dolphin-llama3:8b-256k",
    keep_alive=-1,
    format="json"
)

model = model.bind_tools(
    tools=[
        {

                "name": "searchMemory",
                "description": "Searches memories based on a given query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "index": {
                            "type": "string",
                            "description": "The index to be searched.",
                            "example": "default",
                        },
                        "query": {
                            "type": "string",
                            "description": "The search query based from user request. get concept or noun",
                            "example": "concept",
                        },
                        "minRelevance": {
                            "type": "number",
                            "description": "The minimum relevance score for results.",
                            "minimum": 0,
                            "maximum": 1,
                            "default": 0.8,
                            "example": 0.8,
                        },
                        "limit": {
                            "type": "integer",
                            "description": "The limit on the number of results.",
                            "example": 5,
                        },
                    },
                    "required": ["index", "query", "limit"],
                },
            

        }, 
        {

                "name": "upsertMemory",
                "description": "Inserts or updates a memory document.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "index": {
                            "type": "string",
                            "description": "The index where the document will be upserted.",
                            "example": "default",
                        },
                        "documentId": {
                            "type": "string",
                            "description": "The unique ID of the document.",
                            "example": "synth_memory_MMDDYYYYHHMMSS_feeling",
                        },
                        "text": {
                            "type": "string",
                            "description": "The content of the memory.",
                            "example": "I seem to remember that I must try to use the API whenever I need to recall something",
                        },
                        "tags": {
                            "type": "object",
                            "additionalProperties": {
                                "type": "array",
                                "items": {
                                    "type": "string",
                                },
                            },
                            "example": {
                                "reminder": ["completed"],
                                "payment": ["Globe internet", "February 3, 2024"],
                            },
                        },
                    },
                    "required": ["index", "documentId", "text"],
                },
            
        }, 
    ],


)


response = model.invoke(" recall that memory then remember it. The events today May 19")

print(response)
