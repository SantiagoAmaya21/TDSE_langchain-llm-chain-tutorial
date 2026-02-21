import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert software engineering assistant."),
    ("user", "Explain the concept of {topic} in simple terms.")
])

# Output parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    response = chain.invoke({"topic": topic})
    print("\nResponse:\n")
    print(response)