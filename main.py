import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Initialize OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert software engineering assistant."),
    ("user", "Explain the concept of {topic} in simple terms.")
])

# Create output parser
output_parser = StrOutputParser()

# Create chain
chain = prompt | llm | output_parser

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    response = chain.invoke({"topic": topic})
    print("\nResponse:\n")
    print(response)