# Humanoid LLM Agent

A Python grid-world project where an AI agent uses the OpenAI API to navigate to a key, collect it, and open a door.

## Project Overview

This project simulates a simple 5x5 grid world. The agent starts from a fixed position and must complete the following goal:

1. Move to the key
2. Pick up the key
3. Move to the door
4. Open the door

The project uses a real LLM agent powered by the OpenAI API to decide the next move. A rule-based backup agent is also included so the game can continue if the LLM gives an invalid response or the API fails.

## Features

* 5x5 grid-world environment
* Agent, key, and door positions
* OpenAI API integration
* `.env` file for secure API key handling
* Rule-based fallback agent
* Valid action extraction from LLM responses
* Step-by-step terminal output

## Technologies Used

* Python
* OpenAI API
* python-dotenv
* VS Code
* Virtual Environment

## How It Works

The world provides the current observation, including:

* Agent position
* Key position
* Door position
* Whether the agent has the key
* Whether the door is open

The LLM receives this observation and returns one action:

```text
up
down
left
right
```

The action is then passed to the world, and the agent moves one step. The process repeats until the door is opened or the maximum number of steps is reached.

## Project Structure

```text
humanoid-llm-agent/
│
├── agent.py
├── llm_agent.py
├── main.py
├── world.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/zahirkhanBattani/humanoid-llm-agent.git
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

Create a `.env` file in the main project folder and add:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

Important: never upload your real `.env` file to GitHub.

### 6. Run the project

```bash
python main.py
```

## Example Output

```text
LLMAgent is active
LLM raw response: up
Final action: up
Agent choose: up

Key pick up

LLM raw response: right
Final action: right
Agent choose: right

Door opened! Goal complete.
Successful! Goal achieved
```

## What I Learned

Through this project, I learned how to:

* Build a simple grid-world simulation in Python
* Use classes to separate world logic and agent logic
* Connect a Python project to the OpenAI API
* Store API keys securely using `.env`
* Use a virtual environment for project dependencies
* Add fallback logic using `try/except`
* Validate and clean LLM responses before using them in code

## Future Improvements

* Add random world generation
* Add obstacles in the grid
* Add a graphical interface
* Track the full path taken by the agent
* Compare LLM decisions with rule-based decisions
* Add unit tests
