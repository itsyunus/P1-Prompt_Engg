# 🧠 PlayerOne

A minimal, OpenAI-free LLM flow engine to create and test chatbots using open-source models like `gpt2` or `phi-2`. Inspired by Azure's Prompt Flow but works **fully offline** and locally.

---

## 🚀 Features

- 🧱 Flow-based design using simple YAML
- 🤖 Local LLMs with `transformers` (e.g., GPT2, Phi-2)
- 💬 Interactive CLI-based chatbot
- 🔓 No API keys or cloud access needed
- 🪶 Lightweight and beginner-friendly

---

## 📁 Directory Structure

```
PlayerOne/
├── cli.py                   # CLI commands (init, test)
├── engine.py                # Flow loader + chatbot runner
├── flow_templates/
│   └── chatbot.yaml         # Default flow template
├── main.py                  # Entry point
├── requirements.txt
```

---

## 🔧 Installation

1. Clone the repo:

```bash
git clone https://github.com/itsyunus/P1-Prompt_Engg.git
cd P1-Prompt_Engg
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚡ Quick Start

### 1. Initialize a chatbot flow

```bash
python -m PlayerOne.main init my_chatbot
```

This creates a folder `my_chatbot/flow.yaml` based on the default template.

### 2. Run the chatbot interactively

```bash
python -m PlayerOne.main test my_chatbot
```

Type messages in the terminal. Type `exit` to quit.

---

## 🧠 Use a Better Model

To switch to a smarter open model like `microsoft/phi-2`, edit `my_chatbot/flow.yaml`:

```yaml
flow:
  name: simple_chat
  model: microsoft/phi-2
```

---

## 🛠 Requirements

- Python 3.9 to 3.11
- `transformers`, `torch`, `typer`, `PyYAML`

Install via:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Make sure your code is clean and tested.

---

## 📄 License

MIT License © 2025 Shaik Mohammad Yunus
