from llama_index import SimpleDirectoryReader, GPTListIndex
from llama_index.node_parser import SimpleNodeParser
from llama_index.prompts  import PromptTemplate
from llama_index.llms import ChatMessage, MessageRole
from llama_index.chat_engine import CondenseQuestionChatEngine
import os

#You will need to create a file called keys.py to hold your personal open AI Key using the following variable declaration
# openai_key = "[YOUR OPENAI API KEY]"
from keys import openai_key

#Or you can directly input your Key it into the enviornmental variable declaration below 
# in place of openai_key if you aren't intending to make your code public.
os.environ["OPENAI_API_KEY"] = openai_key
 

#Define what documents are to go into the KB
docs= SimpleDirectoryReader("docs").load_data()
#Parse the documents into smaller nodes for indexing and searching
parser = SimpleNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents(docs)

#Using a list index, as our KB is fairly small and we want summarization of multiple texts
#if the kb changes in size drastically, can look into different more embedding-heavy indexing
index = GPTListIndex.from_documents(docs)

#Prompt given to LLM to synthesize the chat history and user question into a single cohesive openai prompt
custom_prompt = PromptTemplate("""\
Given a conversation (between Parent and Assistant), \
rewrite the Parent's Question to be a standalone prompt that captures all relevant context \
from the Chat History. The standalone prompt should always take the form of "In 50 words or less...", the Parent's Question, (Context: all relevant context from the Chat History),  \
and end with the phrase 'ask follow up question for user reflection. Say you don't know if the Parent's Question is outside of PATbot's purpose' 

<Chat History> 
{chat_history}               

<Parent's Question>
{question}

<Standalone prompt>

""")

# list of `ChatMessage` objects to start the conversation, Pulled from the PATbot script
custom_chat_history = [
    ChatMessage(
        role=MessageRole.ASSISTANT, 
        content="I am PATbot! I am a parent assistant tool for mental wellbeing. I am not a therapist \
            but I have been trained by experts to help explain behavior to parents of children with behavioral problems"
    ),
]

#assigns the ai query_engine (run by the chat_engine) to sort through index and openai
query_engine = index.as_query_engine()

#Creates the chat engine which uses the prompt to condense user question and chat_history context
#This will then be passed through to the query_engine assigned
chat_engine = CondenseQuestionChatEngine.from_defaults(
    query_engine=query_engine, 
    condense_question_prompt=custom_prompt,
    chat_history=custom_chat_history,
    verbose=True
)

#Obtain the user_question by asking the user directly. 
user_question = input("User Question: ")
#while the user has a question instead of typing "stop", ask the chatbot
#To exit the loop, the user types "stop"
while user_question.lower() != "stop":
    #Transform the user_question into a condensed prompt, and query database with the prompt
    response = chat_engine.chat(user_question)
    #visually seperate and print the response
    print("-------------")
    print (response)
    print("------------")
    #Ask for the next question/user input
    user_question = input("User Question: ")

#clear chat history at the end of a conversation. 
chat_engine.reset()

