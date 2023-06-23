#!/home/streamlit/python/streamlit/.venv/bin/python3

from dados import dados

import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv


load_dotenv()


#@st.cache_data
def load_data() -> pd.DataFrame:
    return dados()


def build_visualizations(dataframe: pd.DataFrame):
    st.header(
        ":bar_chart: Dash Board - "
        "Analise de Crédito em tempo 'quase' real"
    )

    st.markdown("#")

    total_analise = (
        dataframe[dataframe.columns[0]].count()
    )

    total_analise = (
        f"{total_analise:_.0f}".replace("_", ".")
    )

    total_analise_aprovada = (
        len(dataframe.query("resultado=='APROVADO'"))
    )

    total_analise_aprovada = (
        f"{total_analise_aprovada:_.0f}".replace("_", ".")
    )

    total_analise_reprovada = (
        len(dataframe.query("resultado=='REPROVADO'"))
    )

    total_analise_reprovada = (
        f"{total_analise_reprovada:_.0f}".replace("_", ".")
    )

    uf = (
        dataframe
        .groupby(by="uf")
        .count()[["id_solicitacao"]]
        .sort_values("uf")
        .rename(columns={"id_solicitacao": "quantidade"})
    )

    uf = (
        uf.sort_values("quantidade", ascending=False)
    )

    regiao = (
        dataframe
        .groupby(by="regiao")
        .count()[["id_solicitacao"]]
        .sort_values("regiao")
        .rename(columns={"id_solicitacao": "quantidade"})
    )

    tempo_medio = (
        dataframe.groupby("uf")["tempo_analise_segundos"].mean()
    )

    fig_uf = px.bar(
        uf,
        title="<b>Volume do solicitações por UF</b>",
        x=uf.index,
        y="quantidade",
        orientation="v",
        text="quantidade",
        color_discrete_sequence=["#FF4B4B"] * len(uf)
    )

    fig_regiao = px.pie(
            regiao,
            title="<b>Volume do solicitações por região</b>",
            names=regiao.index,
            values="quantidade",
            width=450,
            color_discrete_sequence=["#FF4B4B"]
    )

    fig_tempo = px.area(
            tempo_medio,
            title="<b>Tempo médio (em segundos) da análise</b>",
            width=1200,
            height=400,
            color_discrete_sequence=["#FF4B4B"] * len(tempo_medio)
    )

    left_column, middle_column, right_column = st.columns(3)

    with left_column:
        st.markdown('> **Total De Análises:**')
        st.subheader(f":orange[{total_analise}]")

    with middle_column:
        st.markdown("> **Analises Aprovadas:**")
        st.subheader(f":orange[{total_analise_aprovada}]")

    with right_column:
        st.markdown("> **Analises Reprovadas:**")
        st.subheader(f":orange[{total_analise_reprovada}]")

    st.markdown("---")

    chart_column1_left, chart_column1_right = st.columns([0.6, 0.3])
    chart_column1_left.plotly_chart(fig_uf)
    chart_column1_right.plotly_chart(fig_regiao)

    st.plotly_chart(fig_tempo)
    st.markdown("##")
    st.dataframe(dataframe)


def hide_syle() -> None:
    style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def main(dataframe) -> None:
    build_visualizations(dataframe=dataframe)
    hide_syle()


if __name__ == "__main__":
    st.set_page_config(
        page_title="Analise de crédito",
        page_icon=":bar_chart:",
        initial_sidebar_state="collapsed",
        layout="wide"
    )
    dataframe = load_data()
    main(dataframe=dataframe)
