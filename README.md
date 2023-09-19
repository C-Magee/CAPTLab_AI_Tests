This repository is a space for Corin Magee (and future collaborators) to test the use of an independent knowledge base for the CAPTLab's PAT project. 

Running Instructions:
1) Create a keys.py file in the parent folder with:  openai_key = "[YOUR OPEN AI KEY]" OR place your openAI key directly in line 14 of app.py (os.environ["OPENAI_API_KEY"] = YOUR OPEN AI KEY)
From commandline: 
2) Install all required libraries (pip install -r requirements.txt)
3) Run the app.py file (py app.py)
4) When prompted for "User:" enter your user questions, the ai-generated refined prompt will print first followed by a visual seperator and then the actual response. 
5) Repeat step 4 as long as you wish
6) When you want to exit, type "stop" in the user prompt.

9/18/2023 Updates: There is no longer a basic UI, because it was too odd with chat history. You must run this entirely in command line

Changes that need to be made: 
- Create a UI that is outside of command prompt
- Turn off displaying the "Query with:" information
- Devise tests to see if the information being pulled by the knowledge base is adequate or if it needs to be broken up further to be useful.
- Expand knowledge base
- Refine prompt (specifics tbd after mroe testing)
