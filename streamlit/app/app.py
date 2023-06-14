#!/home/streamlit/python/streamlit/.venv/bin/python3

from os import getenv

import streamlit as st
from dotenv import load_dotenv


load_dotenv()

def main():
    st.title("Minha Primeira Aplicação com Streamlit")
    st.subheader("Bem-vindo(a)!")
    
    name = st.text_input("Digite seu nome:")
    
    if st.button("Enviar"):
        st.success(f"Olá, {name}! Bem-vindo(a) à sua primeira aplicação com Streamlit. Variáveis Dotenv OK: {getenv('SQLSERVER_USUARIO')}")
        
if __name__ == '__main__':
    main()
