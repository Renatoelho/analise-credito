#!/home/streamlit/python/streamlit/.venv/bin/python3

import streamlit as st

def main():
    st.title("Minha Primeira Aplicação com Streamlit")
    st.subheader("Bem-vindo(a)!")
    
    name = st.text_input("Digite seu nome:")
    
    if st.button("Enviar"):
        st.success(f"Olá, {name}! Bem-vindo(a) à sua primeira aplicação com Streamlit.")
        
if __name__ == '__main__':
    main()
