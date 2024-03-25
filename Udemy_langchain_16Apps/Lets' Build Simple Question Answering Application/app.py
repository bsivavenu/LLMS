#Hello! It seems like you want to import the Streamlit library in Python. Streamlit is a powerful open-source framework used for building web applications with interactive data visualizations and machine learning models. To import Streamlit, you'll need to ensure that you have it installed in your Python environment.
#Once you have Streamlit installed, you can import it into your Python script using the import statement,

# import streamlit as st

#As Langchain team has been working aggresively on improving the tool, we can see a lot of changes happening every weeek,
#As a part of it, the below import has been depreciated
#from langchain.llms import OpenAI

#New import from langchain, which replaces the above
# from langchain_openai import OpenAI

#When deployed on huggingface spaces, this values has to be passed using Variables & Secrets setting, as shown in the video :)
# import os
# os.environ["OPENAI_API_KEY"] = "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"


# from langchain.llms import HuggingFaceEndpoint
from langchain_community.llms import HuggingFaceEndpoint

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

#Function to return the response
def load_answer(question):
    # "text-davinci-003" model is depreciated, so using the latest one https://platform.openai.com/docs/deprecations
    # llm = OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0)
    llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2") # Model link : https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

    #Last week langchain has recommended to use invoke function for the below please :)
    answer=llm.invoke(question)
    return answer


#App UI starts here
# st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
# st.header("LangChain Demo")

#Gets the user input
def get_text(q):
    # input_text = st.text_input("You: ", key="input")
    return q

# print('etxt')
while True:
    q = input('\n ask question:\n ')
    user_input=get_text(q)
    print(user_input)
    print('\n')
    response = load_answer(user_input)
    print(response)    
# submit = st.button('Generate')  

# #If generate button is clicked
# if submit:

#     st.subheader("Answer:")

#     st.write(response)

