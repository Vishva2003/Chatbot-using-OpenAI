import openai
import gradio as gr
import gradio.components as components

openai.api_key = "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"

messages = [
{"role": "system", "content": "You are an AI specialized in Flirting and Pickup lines"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = components.Textbox(lines=30, label="Chat with AI")
outputs = components.Textbox(lines=30,label="Reply") 

iface = gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI ChatBot <—", description="What you want to know?")
iface.launch(share=True)