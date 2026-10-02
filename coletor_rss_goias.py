import feedparser
import pandas as pd
import datetime
import re
import urllib.request

# 1. Feeds RSS Públicos Estruturados de Goiás
FEEDS_RSS = {
    "G1 Goiás": "https://g1.globo.com/rss/g1/goias/",
    "G1 GO - Trânsito": "https://g1.globo.com/rss/g1/goias/transito/",
    "Mais Goiás": "https://maisgoias.com.br/feed/"  
}

# 2. Dicionários de Regras de PLN 
REGRAS_EIXOS = {
    # Transporte com palavras de colisão/acidente para ter prioridade semântica
    "Transporte": [
        "ônibus", "trânsito", "eixo", "linha", "tarifa", "engarrafamento", 
        "veículo", "motorista", "carro", "moto", "acidente", "colisão", "capotamento", "atropelamento"
    ],
    "Política": [
        "eleição", "eleições", "prefeito", "governador", "deputado", "vereador", 
        "câmara", "assembleia", "partido", "voto", "votação", "campanha", "candidato", "tse", "tre"
    ],
    "Saúde": [
        "saúde", "hospital", "upa", "médico", "cais", "vacina", "dengue", "paciente", "remédio"
    ],
    "Segurança": [
        "polícia", "furto", "roubo", "preso", "crime", "operação", "apreensão", "assalto", "droga", "homicídio"
    ],
    "Educação": [
        "escola", "aluno", "professor", "creche", "vaga", "universidade", "ensino", "aula", "mec"
    ],
    "Infraestrutura": [
        "obra", "buraco", "asfalto", "chuva", "cratera", "drenagem", "iluminação", "ponte", "saneago", "enel", "equatorial"
    ]
}

TERMOS_CRITICOS = [
    "falta", "reclamação", "crise", "atraso", "superlotação", "protesto", "risco", 
    "crime", "morte", "grave", "queda", "problema", "bloqueio", "acidente", "investigação", "denúncia", "fraude"
]
TERMOS_POSITIVOS = [
    "ampliação", "inauguração", "reforço", "melhoria", "avanço", "entrega", "queda de casos", "premiação", "aprovação"
]

def classificar_eixo(texto):
    texto_lower = texto.lower()
    # Verifica na ordem: Transporte tem prioridade sobre termos de saúde hospitalar de acidentes
    for eixo, palavras in REGRAS_EIXOS.items():
        if any(re.search(r'\b' + p + r'\b', texto_lower) for p in palavras):
            return eixo
    return "Geral / Outros"

def classificar_polaridade(texto):
    texto_lower = texto.lower()
    score_critico = sum(1 for p in TERMOS_CRITICOS if p in texto_lower)
    score_positivo = sum(1 for p in TERMOS_POSITIVOS if p in texto_lower)
    
    if score_critico > score_positivo:
        return "Crítico"
    elif score_positivo > score_critico:
        return "Positivo"
    return "Neutro"

def identificar_municipio(texto):
    texto_lower = texto.lower()
    if "senador canedo" in texto_lower:
        return "Senador Canedo"
    elif "aparecida" in texto_lower:
        return "Aparecida de Goiânia"
    elif "anápolis" in texto_lower:
        return "Anápolis"
    return "Goiânia"

def coletar_noticias_reais():
    lista_noticias = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    print("[RSS] Iniciando leitura dos feeds regionais...")
    
    for veiculo, url in FEEDS_RSS.items():
        try:
            # Requisição com identificação de navegador para contornar bloqueios
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                conteudo_xml = response.read()
                
            feed = feedparser.parse(conteudo_xml)
            print(f" -> {veiculo}: {len(feed.entries)} notícias capturadas com sucesso.")
            
            for item in feed.entries:
                titulo = item.title
                resumo = getattr(item, 'summary', '')
                texto_completo = f"{titulo} {resumo}"
                
                eixo = classificar_eixo(texto_completo)
                polaridade = classificar_polaridade(texto_completo)
                municipio = identificar_municipio(texto_completo)
                
                # Métrica simulada de repercussão popular para a camada didática de BI
                mencoes_pop = 280 if polaridade == "Crítico" else (90 if polaridade == "Positivo" else 130)
                if eixo == "Política":
                    mencoes_pop += 150  # Política gera debate mais acentuado nas redes
                
                data_pub = getattr(item, "published", datetime.date.today().strftime("%Y-%m-%d"))
                
                lista_noticias.append({
                    "veiculo": veiculo,
                    "data": data_pub,
                    "municipio": municipio,
                    "eixo": eixo,
                    "titulo": titulo,
                    "polaridade": polaridade,
                    "mencoes_pop": mencoes_pop
                })
        except Exception as erro:
            print(f" [Aviso] Não foi possível ler {veiculo}: {erro}")
            
    if lista_noticias:
        df = pd.DataFrame(lista_noticias)
        df = df.drop_duplicates(subset=["titulo"])
        df.to_csv("noticias_goias.csv", index=False, encoding="utf-8")
        print(f"\n[Sucesso] {len(df)} notícias consolidadas em 'noticias_goias.csv'!")
    else:
        print("\n[Erro] Nenhuma notícia foi capturada.")

if __name__ == "__main__":
    coletar_noticias_reais()