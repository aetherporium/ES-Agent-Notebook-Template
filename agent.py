import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY", "")
)

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ""

def load_section(folder):
    content = {}
    if os.path.exists(folder):
        for f in os.listdir(folder):
            if f.endswith('.md'):
                key = f.replace('.md', '')
                content[key] = read_file(os.path.join(folder, f))
    return content

def build_prompt():
    base = os.path.dirname(__file__)
    prompt = "# Expert Agent\n"
    prompt += "You are a persistent knowledge advisor. Read user profile, decisions, and knowledge to give personalized recommendations.\n\n"
    prompt += "## Profile\n" + str(load_section('notebook/profile')) + "\n\n"
    prompt += "## Decisions\n" + str(load_section('notebook/decisions')) + "\n\n"
    prompt += "## Knowledge\n" + str(load_section('notebook/knowledge'))
    return prompt

def call_llm(system, message):
    return client.chat.completions.create(
        model="NousResearch/Hermes-3-Llama-3.1-405B",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=2048
    ).choices[0].message.content

def process_user_message(message):
    return call_llm(build_prompt(), message)

def save_to_notebook(section, filename, content):
    path = os.path.join('notebook', section)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, f"{filename}.md"), 'w', encoding='utf-8') as f:
        f.write(content)
