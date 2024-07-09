import ollama
import streamlit as st
import asyncio
import time
from openai import AsyncOpenAI
from token_count import TokenCount


title = "Some Bank Chatbot"
st.set_page_config(page_title=title, layout="wide")
st.title(title)

generate = st.button("Generate", type="primary")

model = "llama3"
prompt = "Can a python eat a lion?"

col = st.columns(1)
col.append(f"# :blue[{model}]")

meta = None

body = col[0].empty()
client = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ignore-me")

async def run_prompt(placeholder, meta, prompt, model):
    stream = await client.chat.completions.create( 
        model=model,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt},],
        stream=True
    )
    streamed_text = ""
    async for chunk in stream:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content is not None:
            streamed_text = streamed_text + chunk_content 
            placeholder.write(streamed_text) 

async def main():
    await asyncio.gather(
        run_prompt(body, meta, prompt=prompt, model=model)
    )

if generate:
    if prompt == "":
        st.warning("Please enter a prompt")
    else:
        asyncio.run(main())