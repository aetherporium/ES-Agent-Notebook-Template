import gradio as gr
import os
import re
from agent import process_user_message, save_to_notebook

conversation_history = []

def chat(message, history):
    response = process_user_message(message)
    history.append((message, response))
    return "", history

def save_section(section, name, content):
    save_to_notebook(section, name, content)
    return f"Saved"

with gr.Blocks(title="Expert Agent") as demo:
    gr.Markdown("# Expert Agent")
    
    with gr.Tab("Chat"):
        chatbot = gr.Chatbot(height=500)
        msg = gr.Textbox(label="Message", placeholder="Ask your Expert Agent...")
        submit_btn = gr.Button("Send", variant="primary")
        submit_btn.click(chat, [msg, chatbot], [msg, chatbot])
        msg.submit(chat, [msg, chatbot], [msg, chatbot])
    
    with gr.Tab("Profile"):
        gr.Markdown("## User Profile")
        goals = gr.Textbox(label="Goals", lines=5)
        gr.Button("Save").click(lambda x: save_section('profile', 'goals', x), inputs=[goals])
        preferences = gr.Textbox(label="Preferences", lines=5)
        gr.Button("Save").click(lambda x: save_section('profile', 'preferences', x), inputs=[preferences])
        constraints = gr.Textbox(label="Constraints", lines=5)
        gr.Button("Save").click(lambda x: save_section('profile', 'constraints', x), inputs=[constraints])
        context = gr.Textbox(label="Context", lines=5)
        gr.Button("Save").click(lambda x: save_section('profile', 'context', x), inputs=[context])
    
    with gr.Tab("Knowledge"):
        gr.Markdown("## Knowledge Base")
        concepts = gr.Textbox(label="Concepts", lines=5)
        gr.Button("Save").click(lambda x: save_section('knowledge', 'concepts', x), inputs=[concepts])
        frameworks = gr.Textbox(label="Frameworks", lines=5)
        gr.Button("Save").click(lambda x: save_section('knowledge', 'frameworks', x), inputs=[frameworks])
        evidence = gr.Textbox(label="Evidence", lines=5)
        gr.Button("Save").click(lambda x: save_section('knowledge', 'evidence', x), inputs=[evidence])
        glossary = gr.Textbox(label="Glossary", lines=5)
        gr.Button("Save").click(lambda x: save_section('knowledge', 'glossary', x), inputs=[glossary])
    
    with gr.Tab("Decisions"):
        gr.Markdown("## Active Decisions")
        active = gr.Textbox(label="Active", lines=8)
        gr.Button("Save").click(lambda x: save_section('decisions', 'active', x), inputs=[active])
        rationale = gr.Textbox(label="Rationale", lines=8)
        gr.Button("Save").click(lambda x: save_section('decisions', 'rationale', x), inputs=[rationale])
    
    with gr.Tab("Updates"):
        gr.Markdown("## Pending Updates")
        question = gr.Textbox(label="Add Question", placeholder="What don't you know?")
        gr.Button("Add").click(lambda x: save_section('questions', 'open', x), inputs=[question])
    
    with gr.Tab("Reviews"):
        gr.Markdown("## Notebook Reviews")
        log = gr.Textbox(label="Review Log", lines=10)
        gr.Button("Save").click(lambda x: save_section('reviews', 'review-log', x), inputs=[log])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
