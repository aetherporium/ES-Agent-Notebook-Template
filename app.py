import gradio as gr
import os
from agent import process_user_message, save_to_notebook

def chat(message, history):
    response = process_user_message(message)
    history.append((message, response))
    return "", history

def save(section, name, content):
    save_to_notebook(section, name, content)

with gr.Blocks(title="Expert Agent") as demo:
    gr.Markdown("# Expert Agent")
    
    with gr.Tab("Chat"):
        chatbot = gr.Chatbot(height=500)
        msg = gr.Textbox(label="Message", placeholder="Ask anything...")
        gr.Button("Send", variant="primary").click(chat, [msg, chatbot], [msg, chatbot])
        msg.submit(chat, [msg, chatbot], [msg, chatbot])
    
    with gr.Tab("Profile"):
        gr.Markdown("## User Profile")
        goals = gr.Textbox(label="Goals", lines=5)
        gr.Button("Save").click(lambda x: save('profile', 'goals', x), inputs=[goals])
        prefs = gr.Textbox(label="Preferences", lines=5)
        gr.Button("Save").click(lambda x: save('profile', 'preferences', x), inputs=[prefs])
        constraints = gr.Textbox(label="Constraints", lines=5)
        gr.Button("Save").click(lambda x: save('profile', 'constraints', x), inputs=[constraints])
        context = gr.Textbox(label="Context", lines=5)
        gr.Button("Save").click(lambda x: save('profile', 'context', x), inputs=[context])
    
    with gr.Tab("Knowledge"):
        gr.Markdown("## Knowledge Base")
        concepts = gr.Textbox(label="Concepts", lines=5)
        gr.Button("Save").click(lambda x: save('knowledge', 'concepts', x), inputs=[concepts])
        frameworks = gr.Textbox(label="Frameworks", lines=5)
        gr.Button("Save").click(lambda x: save('knowledge', 'frameworks', x), inputs=[frameworks])
        evidence = gr.Textbox(label="Evidence", lines=5)
        gr.Button("Save").click(lambda x: save('knowledge', 'evidence', x), inputs=[evidence])
        glossary = gr.Textbox(label="Glossary", lines=5)
        gr.Button("Save").click(lambda x: save('knowledge', 'glossary', x), inputs=[glossary])
    
    with gr.Tab("Decisions"):
        gr.Markdown("## Active Decisions")
        active = gr.Textbox(label="Active", lines=8)
        gr.Button("Save").click(lambda x: save('decisions', 'active', x), inputs=[active])
        rationale = gr.Textbox(label="Rationale", lines=8)
        gr.Button("Save").click(lambda x: save('decisions', 'rationale', x), inputs=[rationale])
    
    with gr.Tab("Updates"):
        question = gr.Textbox(label="Add Question")
        gr.Button("Add").click(lambda x: save('questions', 'open', x), inputs=[question])
    
    with gr.Tab("Reviews"):
        log = gr.Textbox(label="Review Log", lines=10)
        gr.Button("Save").click(lambda x: save('reviews', 'review-log', x), inputs=[log])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
