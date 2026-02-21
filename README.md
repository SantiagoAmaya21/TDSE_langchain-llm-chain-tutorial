# LangChain LLM Chain Tutorial

## Project Overview

This repository contains the implementation of a basic **LangChain LLM Chain** using OpenAI as the language model provider.

The objective of this project is to understand:

* How LangChain structures prompts
* How LLM chains are built
* How prompt → model → output parser pipelines work
* How to integrate OpenAI into LangChain

---

## Architecture

The architecture is simple and linear:

User Input
↓
ChatPromptTemplate
↓
ChatOpenAI (LLM)
↓
Output Parser
↓
Final Response

### Components

* **ChatPromptTemplate** → Structures system and user messages.
* **ChatOpenAI** → Connects to OpenAI's GPT model.
* **StrOutputParser** → Parses raw model output into clean text.
* **Chain Operator (|)** → Connects components in sequence.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/langchain-llm-chain-tutorial.git
cd langchain-llm-chain-tutorial
```

### Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_real_key_here
```

---

## Running the Project

```bash
python main.py
```

You will be prompted to enter a topic.

Example:

```
Enter a topic: Retrieval-Augmented Generation
```

The model will generate an explanation.

---

## What Was Learned

* How LangChain builds modular pipelines
* Prompt engineering basics
* How LLM chaining works internally
* How to connect OpenAI models to LangChain

---

## Technologies Used

* Python
* LangChain
* OpenAI API
* dotenv

