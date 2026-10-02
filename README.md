# 📰 RPDL — Rastreador de Pautas e Debates Locais

> **Projeto Integrador V-A (Caráter Extensionista)**  
> Curso: Big Data e Inteligência Artificial  
> Disciplina: Técnicas de Visualização de Dados & Business Intelligence  

---

## 📌 Visão Geral do Projeto

O **RPDL (Rastreador de Pautas e Debates Locais)** é uma aplicação analítica voltada ao monitoramento e categorização inteligente de notícias regionais e pautas comunitárias no estado de Goiás. 

Desenvolvido no âmbito de atividade extensionista em parceria com organização do setor educacional em Jornalismo, o sistema automatiza a ingestão de notícias abertas e disponibiliza um painel interativo de **Business Intelligence (BI)** para:
1. Apoiar a identificação ágil de pautas de interesse público e furos jornalísticos.
2. Servir como ambiente laboratorial para o ensino de **Jornalismo de Dados (*Data-Driven Journalism*)** e análise de escuta social.

---

## 🚀 Arquitetura e Pipeline da Solução

O sistema opera no formato de **Produto Mínimo Viável (MVP)** dividido em três camadas:

1. **Ingestão de Dados (Feeds RSS/XML):**
   * Coleta automatizada de manchetes e resumos via biblioteca `feedparser`.
   * Monitoramento de portais regionais abertos (*G1 Goiás*, *G1 Trânsito*, *Mais Goiás*).
   * Tratamento de cabeçalhos de requisição e persistência estruturada em formato tabular (`noticias_goias.csv`).

2. **Inteligência e Processamento de Linguagem Natural (PLN):**
   * **Classificação Temática Heurística:** Categorização automática em eixos prioritários (*Saúde*, *Transporte*, *Segurança*, *Educação*, *Infraestrutura* e *Política*).
   * **Hierarquia Semântica:** Calibragem de regras para desambiguação de termos (ex.: priorização do eixo *Transporte* em eventos viários com impactos hospitalares).
   * **Análise de Enquadramento Editorial:** Classificação de polaridade (*Crítico*, *Neutro* ou *Positivo*) via detecção léxica.

3. **Camada de Visualização & Business Intelligence:**
   * Aplicação web interativa desenvolvida com **Streamlit**.
   * Gráficos analíticos construídos com **Plotly**.
   * Filtros dinâmicos por município e eixo temático.
   * Exportação de recortes de dados para estudos de caso pedagógicos.

---

## 📊 Indicadores e Visualizações de BI (KPIs)

* **Pautas Mapeadas:** Volume total de matérias rastreadas no período.
* **Eixo em Destaque:** Identificação da categoria temática com maior saturação na imprensa regional.
* **Índice de Tom Crítico:** Porcentagem de publicações voltadas a denúncias ou demandas comunitárias.
* **Índice de Lacuna Editorial (*Bubble Chart*):** Gráfico de dispersão que cruza veículos noticiosos, repercussão popular estimada e polaridade, destacando pautas críticas com alta demanda social.

---

## 🛠️️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Manipulação de Dados:** Pandas
* **Coleta de Dados:** Feedparser, Urllib
* **Visualização & Dashboard:** Streamlit, Plotly Express

---

## 📂 Estrutura do Repositório

```text
├── coletor_rss_goias.py    # Script de ingestão RSS e classificação PLN
├── app_rpdl.py             # Aplicação do Dashboard interativo (Streamlit)
├── noticias_goias.csv      # Base de dados estruturada gerada pelo coletor
└── README.md               # Documentação técnica do projeto
