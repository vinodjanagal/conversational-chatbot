import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate

# 1. setup and load API key.
def setup_environment():
    """Loads environment variables and checks for the GROQ_API_KEY."""
    load_dotenv()
    if "GROQ_API_KEY" not in os.environ:
        print("Error: GROQ_API_KEY not found in .env file.")
        print("Please create a .env file and add your Groq API Key.")
        exit()

# 2. the prompt template.

# for controlling AI behaviour.

def create_prompt_template():
    """Creates the prompt template for the conversation."""
    template = """
You are a friendly and helpful AI travel assistant. Your goal is to have a natural conversation
with a user to help them plan their trip. Keep your responses concise and conversational.
If the user's input is unclear, ask a clarifying question instead of assuming it's a correction.


Current conversation:
{history}

Human: {input}
AI Assistant:"""

    return PromptTemplate(input_variables=["history", "input"], template=template)


#  3.The Chatbot Class ---
class TravelChatbot:
    def __init__(self, prompt):
        """Initializes the chatbot's components using the Groq LLM."""

        # We are using Mixtral, a high-quality model available on Groq.
        self.llm = ChatGroq(model_name="llama3-8b-8192", temperature=0.7)

        self.memory = ConversationBufferMemory(human_prefix="Human", ai_prefix="AI Assistant")
        
        self.conversation_chain = ConversationChain(
            prompt=prompt,
            llm=self.llm,
            verbose=False,
            memory=self.memory
        )

    def chat(self, user_input):
        """
        Handles a single turn of the conversation.
        Gets the full response and post-processes it to prevent runaway generation.
        """
        full_response = self.conversation_chain.predict(input=user_input)

        clean_response = full_response.split("Human:")[0].strip()
        return clean_response


# 4. THE INTERFACE: Running the Chatbot ---

if __name__ == "__main__":
    # First, run the setup to load the API key and validate it.
    setup_environment()
    
    # Second, create the prompt template blueprint.
    prompt_template = create_prompt_template()
    
    # Third, use the class blueprint and the prompt blueprint to create a live chatbot instance.
    bot = TravelChatbot(prompt=prompt_template)
    
    # Finally, start the interactive conversation loop.
    print("Groq Travel Chatbot is ready!")
    print("   Type 'exit' to end the conversation.")
    
    while True:
        # Wait for the user to type something and press Enter.
        user_query = input("User: ")
        
        # Check if the user wants to quit.
        if user_query.lower() == 'exit':
            print("AI: Goodbye! Hope you have a great trip!")
            break # This exits the 'while' loop and the program ends.
        
        # If the user didn't type 'exit', pass their query to the bot's chat method.
        ai_response = bot.chat(user_query)
        
        # Print the bot's response.
        print(f" bot: \n{ai_response}\n")





