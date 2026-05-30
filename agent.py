import os
import re
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

def load_section(path):
    content = {}
    if os.path.exists(path):
        for filename in os.listdir(path):
            if filename.endswith('.md'):
                key = filename.replace('.md', '')
                content[key] = read_file(os.path.join(path, filename))
    return content

def build_system_prompt():
    base = os.path.dirname(__file__)
    prompt = read_file(os.path.join(base, 'notebook', 'prompts', 'expert-agent.md')) + "\n\n"
    prompt += read_file(os.path.join(base, 'notebook', 'prompts', 'notebook-rules.md')) + "\n\n"
    prompt += "## User Profile\n" + str(load_section(os.path.join(base, 'notebook', 'profile'))) + "\n\n"
    prompt += "## Active Decisions\n" + str(load_section(os.path.join(base, 'notebook', 'decisions'))) + "\n\n"
    prompt += "## Knowledge\n" + str(load_section(os.path.join(base, 'notebook', 'knowledge')))
    return prompt

def generate_response(system_prompt, user_message):
    return client.chat.completions.create(
        model="NousResearch/Hermes-3-Llama-3.1-405B",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=2048
    ).choices[0].message.content

def process_user_message(message):
    return generate_response(build_system_prompt(), message)

def save_to_notebook(section, filename, content):
    base = os.path.dirname(__file__)
    path = os.path.join(base, 'notebook', section)
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, f"{filename}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
