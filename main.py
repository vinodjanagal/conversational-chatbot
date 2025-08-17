import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate

# 1. setup and load API key.

def setup_environment():
    """loads environment variables and check the API key."""

    load_dotenv()
    if "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
        print("Error: HUGGINGFACEHUB_API_TOKEN not found in .env file. ")
        print("Please create a .env file and add your Hugging Face API Token.")

        exit()



# --- TEMPORARY TEST BLOCK ---
# We will use this to test our functions as we build them.
if __name__ == "__main__":
    print("--- Running setup check ---")
    setup_environment()
    print("--- Setup successful! API key is loaded. ---")





