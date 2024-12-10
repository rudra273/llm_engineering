import os
from typing import List
import ollama
import gradio as gr
import sys

system_message = "You are a helpful assistant that responds in markdown"

def message_llama(prompt):
    llama_model = "llama3.2"
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    response = ollama.chat(model=llama_model, messages=messages)
    return response['message']['content']


def stream_llama(prompt): 
    llama_model = "llama3.2"
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    
    # Use the stream parameter in ollama.chat
    stream = ollama.chat(
        model=llama_model, 
        messages=messages, 
        stream=True
    )
    
    result = ""
    for chunk in stream:
        # Check if the chunk contains content
        if chunk['message']['content']:
            result += chunk['message']['content']
            yield result

# print(message_llama("what are you")) 

# view = gr.Interface(
#     fn=stream_llama,
#     inputs=[gr.Textbox(label="Your message:")],
#     outputs=[gr.Markdown(label="Response:")],
#     flagging_mode="never"
# )
# view.launch()


with gr.Interface(
    fn=stream_llama,
    inputs=[gr.Textbox(label="Your message:")],
    outputs=[gr.Markdown(label="Response:")],
    flagging_mode="never"
) as view:
    view.launch()

