#pip install streamlit langchain openai wikipedia chromadb tiktoken
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY']=apikey

st.title('Test GPT')
prompt=st.text_input('Plug in your prompt here')

#prompt template
title_template=PromptTemplate(
    input_variables=['topic'],
    template='write me a youtube video title about {topic}'
)


#llmS 
llm=OpenAI(temperature=0.9)
title_chain=LLMChain(llm=llm,prompt=title_template)

if prompt:
    resposne=title_chain.run(topic=prompt)
    st.write(resposne)