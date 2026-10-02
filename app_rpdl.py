import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página para modo amplo (layout profissional de BI)
st.set_page_config(
    page_title="RPDL - Rastreador de Pautas Locais",
    page_icon="📰",
    layout="wide"
)

# 1. Carregamento dos dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv("noticias_goias.csv")
    return df

df = carregar_dados()

# 2. Cabeçalho e Identificação Institucional
st.title("📰 RPDL: Rastreador de Pautas e Debates Locais")
st.caption("Projeto Integrador V-A • Parceria: Bernadete Coelho Serviços Educacionais & PUC Goiás")
st.markdown("---")

# 3. Barra Lateral: Filtros Interativos
st.sidebar.header("🔍 Filtros de Apuração")

municipios_disponiveis = ["Todos"] + sorted(df["municipio"].unique().tolist())
municipio_selecionado = st.sidebar.selectbox("Município:", municipios_disponiveis)

eixos_disponiveis = ["Todos"] + sorted(df["eixo"].unique().tolist())
eixo_selecionado = st.sidebar.selectbox("Eixo Temático:", eixos_disponiveis)

# Aplicando os filtros no DataFrame
df_filtrado = df.copy()
if municipio_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["municipio"] == municipio_selecionado]
if eixo_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["eixo"] == eixo_selecionado]

# 4. Linha de KPIs (Indicadores-Chave de Desempenho)
total_pautas = len(df_filtrado)
total_mencoes = df_filtrado["mencoes_pop"].sum() if total_pautas > 0 else 0
eixo_top = df_filtrado["eixo"].mode()[0] if total_pautas > 0 else "N/A"
pct_criticas = (len(df_filtrado[df_filtrado["polaridade"] == "Crítico"]) / total_pautas * 100) if total_pautas > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Pautas Mapeadas", f"{total_pautas}")
col2.metric("Volume de Clamor Popular", f"{total_mencoes:,}".replace(",", "."))
col3.metric("Eixo em Destaque", eixo_top)
col4.metric("Índice de Tom Crítico", f"{pct_criticas:.1f}%")

st.markdown("---")

# 5. Painel Gráfico (Visualizações de BI)
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("📊 Distribuição de Pautas por Eixo Temático")
    contagem_eixo = df_filtrado["eixo"].value_counts().reset_index()
    contagem_eixo.columns = ["Eixo", "Total"]
    fig_eixo = px.bar(
        contagem_eixo,
        x="Eixo",
        y="Total",
        color="Eixo",
        text_auto=True,
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    fig_eixo.update_layout(showlegend=False, xaxis_title="", yaxis_title="Quantidade de Notícias")
    st.plotly_chart(fig_eixo, use_container_width=True)

with col_graf2:
    st.subheader("🎯 Enquadramento Editorial (Polaridade)")
    contagem_polaridade = df_filtrado["polaridade"].value_counts().reset_index()
    contagem_polaridade.columns = ["Polaridade", "Quantidade"]
    fig_polaridade = px.pie(
        contagem_polaridade,
        names="Polaridade",
        values="Quantidade",
        color="Polaridade",
        color_discrete_map={"Crítico": "#E53E3E", "Neutro": "#CBD5E0", "Positivo": "#38A169"},
        hole=0.4
    )
    st.plotly_chart(fig_polaridade, use_container_width=True)

# 6. Módulo Didático e Tomada de Decisão: Análise de Lacuna (Gap)
st.subheader("💡 Estudo de Caso Didático: Índice de Lacuna Editorial")
st.write(
    "Cruza o volume de reclamações/debates populares com o enquadramento da matéria para indicar pautas de apuração prioritárias."
)

fig_gap = px.scatter(
    df_filtrado,
    x="mencoes_pop",
    y="veiculo",
    color="polaridade",
    size="mencoes_pop",
    hover_data=["titulo", "municipio", "eixo"],
    color_discrete_map={"Crítico": "#E53E3E", "Neutro": "#4A5568", "Positivo": "#38A169"},
    labels={"mencoes_pop": "Menções da População (Fóruns/Redes)", "veiculo": "Veículo Noticioso"}
)
st.plotly_chart(fig_gap, use_container_width=True)

# 7. Tabela de Pautas para Exercícios Pedagógicos
with st.expander("📋 Visualizar Base de Pautas Filtradas (Exportação Didática)"):
    st.dataframe(df_filtrado, use_container_width=True)
    csv_bytes = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Baixar Dados Filtrados (CSV)",
        data=csv_bytes,
        file_name="pautas_filtradas_rpdl.csv",
        mime="text/csv"
    )