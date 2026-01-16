from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from src.config.index import appConfig

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_ollama import ChatOllama, OllamaEmbeddings
from src.config.index import appConfig
import os

POLOAPI_BASE_URL = "https://poloai.top/v1"
OLLAMA_BASE_URL = "https://ollama.com/v1"
LOCAL_OLLAMA_BASE_URL = "http://localhost:11434"

openAI = {
#     "embeddings_llm": ChatOllama(
#         model="qwen2.5", base_url=LOCAL_OLLAMA_BASE_URL, temperature=0
#     ),
    "embeddings_llm": ChatOpenAI(
         model="qwen3-coder:480b-cloud", base_url=OLLAMA_BASE_URL, api_key=appConfig["ollama_api_key"], temperature=0
    ),
    "embeddings": OllamaEmbeddings(
        model="nomic-embed-text",
        base_url=LOCAL_OLLAMA_BASE_URL,
        # api_key=appConfig["OLLAMA_API_KEY"],
        # dimensions=768,  # This ollama model only support 768.  1536 Do not changes this value. It is used in the document_chunks embedding vector.
    ),
    "chat_llm": ChatOpenAI(
         model="qwen3-coder:480b-cloud", base_url=OLLAMA_BASE_URL, api_key=appConfig["ollama_api_key"], temperature=0
    ),
    "mini_llm": ChatOllama(
         model="qwen2.5", base_url=LOCAL_OLLAMA_BASE_URL, temperature=0
    ),
}


# # PoloAPI model
# openAI = {
#     "embeddings_llm": ChatOpenAI(
#         model="gpt-4-turbo", base_url=POLOAPI_BASE_URL, api_key=appConfig["openai_api_key"], temperature=0
#     ),
#     "embeddings": OpenAIEmbeddings(
#         model="text-embedding-3-large",
#         base_url=POLOAPI_BASE_URL,
#         api_key=appConfig["openai_api_key"],
#         dimensions=1536,  # ! Do not changes this value. It is used in the document_chunks embedding vector.
#     ),
#     "chat_llm": ChatOpenAI(
#         model="gpt-4o", base_url=POLOAPI_BASE_URL, api_key=appConfig["openai_api_key"], temperature=0
#     ),
#     "mini_llm": ChatOpenAI(
#         model="gpt-4o-mini", base_url=POLOAPI_BASE_URL, api_key=appConfig["openai_api_key"], temperature=0
#     ),
# }

# llm = ChatOpenAI(
#         model="qwen3-coder-plus",
#         temperature=0,
#         base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#         api_key=os.getenv("DASHSCOPE_API_KEY")
# )  

 # llm = ChatOllama(
        #     model="qwen2.5",
        #     temperature=0,
        #     base_url="http://localhost:11434",
        #     # api_key=os.getenv("OLLAMA_API_KEY")
        # )

#  embedding_model =OllamaEmbeddings(
#         model="mxbai-embed-large",
#         base_url="http://localhost:11434",
#         # api_key=os.getenv("OLLAMA_API_KEY")
#     )   

# openAI = {
#     "embeddings_llm": ChatOpenAI(
#         model="gpt-4-turbo", api_key=appConfig["openai_api_key"], temperature=0
#     ),
#     "embeddings": OpenAIEmbeddings(
#         model="text-embedding-3-large",
#         api_key=appConfig["openai_api_key"],
#         dimensions=1536,  # ! Do not changes this value. It is used in the document_chunks embedding vector.
#     ),
#     "chat_llm": ChatOpenAI(
#         model="gpt-4o", api_key=appConfig["openai_api_key"], temperature=0
#     ),
#     "mini_llm": ChatOpenAI(
#         model="gpt-4o-mini", api_key=appConfig["openai_api_key"], temperature=0
#     ),
# }
