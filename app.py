import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Impostos VS Faturamento",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Impostos VS Faturamento")
st.header("Impostos")
impostos_arquivo = st.file_uploader("Impostos",  type=["xlsx", "xls"])
if impostos_arquivo is not None:
    df_impostos = pd.read_excel(impostos_arquivo)
    df_impostos

st.header("Faturamento")
faturamento_arquivo = st.file_uploader("Faturamento", type=["xlsx", "xls"])
if faturamento_arquivo is not None:
    df_faturamento = pd.read_excel(faturamento_arquivo)
    df_faturamento