import streamlit as st
import requests
import websocket
import threading

API = "http://localhost:8000"

st.title("Full Stack FastAPI + Streamlit (Minimal Version)")

# --------------------------
# LOGIN
# --------------------------
st.header("Login")

username = st.text_input("Username", "admin")
password = st.text_input("Password", "admin123", type="password")

if st.button("Login"):
    res = requests.post(f"{API}/auth/login", json={"username": username, "password": password})
    st.write(res.json())

# --------------------------
# FILE UPLOAD
# --------------------------
st.header("CSV Upload")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    res = requests.post(f"{API}/upload/", files={"file": file})
    st.success(res.json())

    file_path = res.json()["path"]
    st.write("Uploaded path:", file_path)

    st.subheader("Run EDA")
    if st.button("Compute EDA"):
        eda_res = requests.post(f"{API}/eda/", json={"path": file_path})
        st.json(eda_res.json())

# --------------------------
# RAG QUERY
# --------------------------
st.header("Ask AI (RAG)")

query = st.text_input("Ask something")

if st.button("Ask AI"):
    res = requests.post(f"{API}/rag/ask", json={"query": query})
    #st.write("Answer:", res.json()["answer"])
    #st.write("Raw response:", res.text)
    #st.write("Context used:", res.json()["context"])

# --------------------------
# WEBSOCKET
# --------------------------
st.header("WebSocket Notifications")

def ws_listener():
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8000/ws")
    while True:
        msg = ws.recv()
        st.toast(msg)

threading.Thread(target=ws_listener, daemon=True).start()