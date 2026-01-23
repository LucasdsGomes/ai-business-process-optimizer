import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# response = requests.get("http://localhost:8000/health")
# st.write(response.json())

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Process Analytics", layout="wide")

st.title("📊 Process Analytics Dashboard")
st.caption("Análises geradas por IA • Dados operacionais • Storytelling de dados")

@st.cache_data(ttl=30)
def fetch_processes():
    resp = requests.get(f"{API_URL}/api/v1/processes")
    resp.raise_for_status()
    return resp.json()

processes = fetch_processes()

if not processes:
    st.warning("Nenhum processo encontrado")
    st.stop()

df = pd.DataFrame(processes)

# ---------- KPIs ----------
col1, col2, col3 = st.columns(3)

col1.metric("Total de Processos", len(df))
col2.metric("Processos Analisados", (df['status'] == 'ANALYZED').sum())
col3.metric("Pendentes", (df['status'] != 'ANALYZED').sum())

st.divider()

# ---------- GRÁFICO 1: Status ----------
st.subheader("📌 Distribuição por Status")
status_counts = df['status'].value_counts()

fig1 = plt.figure(figsize=(4, 2.5))

status_counts.plot(kind='bar')
plt.title("Processos por Status")
plt.xlabel("Status")
plt.ylabel("Quantidade")
st.pyplot(fig1)

st.divider()

# ---------- GRÁFICO 2: Tamanho da Análise ----------
st.subheader("🧠 Complexidade das Análises (proxy)")

df['analysis_length'] = df['analysis_result'].fillna("").apply(len)


fig2 = plt.figure(figsize=(4, 2.5))

plt.hist(df['analysis_length'], bins=10)
plt.xlabel("Tamanho do texto da análise")
plt.ylabel("Quantidade de processos")
plt.title("Distribuição do tamanho das análises")
st.pyplot(fig2)

st.divider()

# ---------- TABELA ----------
st.subheader("📋 Processos Detalhados")

st.dataframe(
    df[['id', 'name', 'status', 'analysis_length']],
    use_container_width=True
)

# ---------- STORYTELLING ----------
st.subheader("📝 Análise Individual")

selected = st.selectbox(
    "Selecione um processo",
    df['name'].tolist()
)

process = df[df['name'] == selected].iloc[0]

st.markdown(f"### {process['name']}")
st.markdown(f"**Status:** {process['status']}")

if process['analysis_result']:
    st.markdown(process['analysis_result'])
else:
    st.info("Processo ainda não analisado pela IA")
