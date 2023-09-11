This repository is a space for Corin Magee (and future collaborators) to test the use of an independent knowledge base for the CAPTLab's PAT project. 

9/11/2023 Updates: In the current iteration, running app.py after installing all of the requirements (pip install -r requirements.txt ) creates a  local site with which to ask questions based on the pdfs in the docs folder. The user must also have their openAI Key saved in a keys.py file in the parent folder (not shown in github for privacy) using the following variable assignment: openai_key = "[YOUR OPEN AI KEY]"

Changes that need to be made: 
- Comment current code more and personalize it from its current basic functionality as taken from this tutorial (https://beebom.com/how-train-ai-chatbot-custom-knowledge-base-chatgpt-api/) 
- Display/store chat history to make questions a conversation.
- Devise tests to see if the information being pulled by the knowledge base is adequate or if it needs to be broken up further to be useful.
- Create a new UI to promote more chat-like functions, including prompt-scripting
- Expand knowledge base
