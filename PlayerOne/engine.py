import yaml
from transformers import pipeline

def load_flow(folder):
    with open(f"{folder}/flow.yaml") as f:
        return yaml.safe_load(f)

def run_interactive(flow_data):
    model_name = flow_data['flow']['model']
    chatbot = pipeline("text-generation", model=model_name)

    print("\n[Interactive Mode: Type 'exit' to quit]\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chatbot(
            f"User: {user_input}\nAI:",
            max_new_tokens=100,
            do_sample=True,
            temperature=0.9,
            top_k=50,
            top_p=0.95,
            pad_token_id=50256
        )[0]['generated_text']

        reply = response.split("AI:")[-1].strip()
        print("Bot:", reply if reply else "[No reply]")
