# Conversational AI Travel Chatbot

A fast, conversational AI chatbot for travel planning, built with LangChain and powered by the Llama3 model via the Groq API.

## Problem
Planning a trip involves a series of related questions, not just a single search. A user needs an assistant that can maintain context and have a natural, multi-turn conversation.

## Solution
This chatbot is built to have a seamless, back-and-forth conversation. The key features are:

*   **High-Performance LLM:** It leverages the `llama3-8b-8192` model via the Groq API, providing near-instantaneous responses for a smooth user experience.
*   **Conversational Memory:** It uses LangChain's `ConversationBufferMemory` to remember the context of the dialogue, allowing for intelligent follow-up questions.
*   **Robust Output Parsing:** The final output from the LLM is post-processed to prevent "runaway generation," ensuring the bot only provides its own response and waits for the next user input.

## Tech Stack
*   **Languages & Libraries:** Python, LangChain, LangChain-Groq, Groq
*   **Models:** Llama3 8B
*   **Platform:** Groq API
*   **Developer Tools:** VS Code, Git, GitHub, Virtual Environments

## How to Run
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file and add your `GROQ_API_KEY`.
5. Run the chatbot: `python main.py`