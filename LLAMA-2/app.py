import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from llama 2 Model


def getLLamaResponse(input_text, no_words, blog_style):
    ##LLAMA2 Model

    llm = CTransformers(
        model="D:\LLAMA-2_Model\Models\llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        config={"max_new_tokens": 256, "temperature": 0.01},
    )

    ## Prompt Template

    template = """
     write an accurate blog for {blog_style} type of people for a topic {input_text}
     in no more than {no_words} words.
    """

    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"], template=template
    )

    # Generate response from LLAMA 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))

    return response


st.set_page_config(
    page_title="Generate Blogs",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed",
)


st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")


## Creating two more columns for two additional fields

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("Enter the Number of Words")

with col2:
    blog_style = st.selectbox(
        'Writing the blog for', ('Researchers','Data Scientist','Non-Tech'), index=0
    )

submit = st.button("Generate")


## final response
if submit:
    st.write(getLLamaResponse(input_text, no_words, blog_style))
