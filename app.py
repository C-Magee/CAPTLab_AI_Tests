from gpt_index import SimpleDirectoryReader,  GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import gradio as gr
import os
import streamlit as st
#You will need to create a file called keys.py to hold your personal open AI Key using the following variable declaration
# openai_key = "[YOUR OPENAI API KEY]"
from keys import openai_key

#Or you can directly input your Key it into the enviornmental variable declaration below 
# in place of openai_key if you aren't intending to make your code public.
os.environ["OPENAI_API_KEY"] = openai_key

#create a json file holding the chat history including the prompts, knowledge, base and responses. 
def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')

    return index

#cosntructs the chatbot response by querying the prompt formulated by the user and the json modifications
def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

#Creates a basic user interface using gradio
iface = gr.Interface(fn=chatbot,
                     inputs=gr.components.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="Custom-trained AI Chatbot")

#Pulls the knowledge base from the docs folder
index = construct_index("docs")
#launches the AI on a local server. 
iface.launch(share=True)