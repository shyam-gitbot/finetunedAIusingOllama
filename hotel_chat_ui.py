import streamlit as st
from ollama_client import chat_with_ollama #, #SYSTEM_PROMPT

MODEL = "tinyllama:latest"  # change to your model name

st.title("🏨 Hotel Assistant Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []
    pass

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input := st.chat_input("Let me resolve your queries..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get model response
    reply = chat_with_ollama(MODEL, st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
