import pandas as pd
import numpy as np

# Definindo dados controlados com foco no jornalismo regional de Goiás
dados = [
    # Saúde
    {"veiculo": "O Popular", "data": "2026-09-20", "municipio": "Goiânia", "eixo": "Saúde", 
     "titulo": "Falta de pediatras em CAIS gera filas e protestos de mães", "polaridade": "Crítico", "mencoes_pop": 420},
    {"veiculo": "G1 Goiás", "data": "2026-09-21", "municipio": "Goiânia", "eixo": "Saúde", 
     "titulo": "Prefeitura anuncia ampliação do horário de vacinação", "polaridade": "Positivo", "mencoes_pop": 180},
    {"veiculo": "Mais Goiás", "data": "2026-09-23", "municipio": "Senador Canedo", "eixo": "Saúde", 
     "titulo": "UPA de Senador Canedo registra superlotação no início da semana", "polaridade": "Crítico", "mencoes_pop": 310},
    
    # Transporte e Mobilidade
    {"veiculo": "Jornal Opção", "data": "2026-09-22", "municipio": "Goiânia", "eixo": "Transporte", 
     "titulo": "Usuários do Eixo Anhanguera relatam atrasos em horários de pico", "polaridade": "Crítico", "mencoes_pop": 550},
    {"veiculo": "Mais Goiás", "data": "2026-09-24", "municipio": "Aparecida de Goiânia", "eixo": "Transporte", 
     "titulo": "Novas linhas de ônibus são integradas na região metropolitana", "polaridade": "Neutro", "mencoes_pop": 130},
    {"veiculo": "O Popular", "data": "2026-09-25", "municipio": "Senador Canedo", "eixo": "Transporte", 
     "titulo": "Reclamações sobre intervalos de viagens entre Canedo e Goiânia crescem", "polaridade": "Crítico", "mencoes_pop": 480},

    # Infraestrutura e Obras
    {"veiculo": "G1 Goiás", "data": "2026-09-21", "municipio": "Goiânia", "eixo": "Infraestrutura", 
     "titulo": "Obras de drenagem no Setor Pedro Ludovico avançam para nova fase", "polaridade": "Neutro", "mencoes_pop": 90},
    {"veiculo": "Mais Goiás", "data": "2026-09-24", "municipio": "Goiânia", "eixo": "Infraestrutura", 
     "titulo": "Crateras na Marginal Botafogo trazem risco a motoristas após chuva", "polaridade": "Crítico", "mencoes_pop": 610},

    # Educação
    {"veiculo": "Jornal Opção", "data": "2026-09-22", "municipio": "Goiânia", "eixo": "Educação", 
     "titulo": "Escolas municipais recebem novos equipamentos de informática", "polaridade": "Positivo", "mencoes_pop": 75},
    {"veiculo": "O Popular", "data": "2026-09-25", "municipio": "Senador Canedo", "eixo": "Educação", 
     "titulo": "Déficit de vagas em creches municipais mobiliza comunidade local", "polaridade": "Crítico", "mencoes_pop": 390},

    # Segurança
    {"veiculo": "G1 Goiás", "data": "2026-09-23", "municipio": "Aparecida de Goiânia", "eixo": "Segurança", 
     "titulo": "Operação integrada reforça patrulhamento em polos comerciais", "polaridade": "Neutro", "mencoes_pop": 110},
    {"veiculo": "Mais Goiás", "data": "2026-09-26", "municipio": "Goiânia", "eixo": "Segurança", 
     "titulo": "Moradores do Setor Central cobram reforço na iluminação pública contra furtos", "polaridade": "Crítico", "mencoes_pop": 340}
]

df = pd.DataFrame(dados)
df.to_csv("noticias_goias.csv", index=False, encoding="utf-8")
print("Dataset 'noticias_goias.csv' gerado com sucesso!")