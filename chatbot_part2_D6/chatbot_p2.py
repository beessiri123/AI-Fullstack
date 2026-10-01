from ollama import chat
import streamlit as st
st.set_page_config(page_title="LlamaBot",page_icon="𐙚")
st.title("LlamaBot - Here to talk!")

personality = "You are a friendly and patient tutor named Llama.Answer warmly.keep the answers within one senetence."
personality2 = "You are a friendly and patient tutor named Llama.Answer warmly.keep the answers within one senetence."

if "history" not in st.session_state:
    st.session_state.history=[{"role": "system","content": personality}]

if "toast_msg" not in st.session_state:
    st.session_state.toast_msg = None

if st.session_state.toast_msg:
    st.toast(st.session_state.toast_msg[0], st.session_state.toast_msg[1])
    st.session_state.toast_msg = None

with st.sidebar:
    st.header("chat controls")
    if st.button("clear chat" , type = "primary"):
        st.session_state.history=[{"role": "system","content": personality}]
        st.rerun()
    if st.button("change personality"):
        st.session_state.history=[{"role": "system","content": personality2}]
        st.rerun()


with st.chat_message("assistant"):
    st.write("Hello I'm Llama.Ask something to get started.")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Type something...")
if question:
    st.session_state.history.append({"role":"user","content": question})

    with st.chat_message("user"):
        st.write(question)

    try:
        with st.spinner("Thinking..."):
            response = chat(
                    model="llama3.2",
                    messages=st.session_state.history
            )
            reply = response["message"]["content"]
            st.session_state.history.append({"role":"assistant","content": reply})
                
            with st.chat_message("assistant"):
                st.write(reply)
    except Exception as e:
        st.write("Ollama is not working. Try again")