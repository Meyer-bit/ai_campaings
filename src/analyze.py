import os
import json
import pandas as pd
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  

client = Groq(api_key=os.getenv("GROQ_API_KEY"))



def dataframe_to_text(df):
    text = ""
    for _, row in df.iterrows():
        text += (
            f"Campanha: {row['campaign']} | "
            f"ROAS: {row['roas']} | "
            f"CPA: {row['cpa']} | "
            f"CTR: {row['ctr']}\n"
        )
    return text

def analyze_campaigns(df):
    campaigns_text = dataframe_to_text(df)

    prompt = f"""
Você é um gestor de tráfego profissional.

Analise as campanhas abaixo respeitando ESTRITAMENTE as regras:

REGRAS DE DECISÃO:
- Pausar campanhas se ROAS < 1.2 OU CPA > 60 OU CTR < 1.5
- Escalar campanhas se ROAS >= 2.0 E CPA <= 40 E CTR >= 5
- Caso contrário, marcar como teste

RESTRIÇÕES:
- Use apenas os dados fornecidos
- Não crie novas regras

FORMATO OBRIGATÓRIO DO MOTIVO:
- Linguagem natural
- Métricas relevantes com valores entre parênteses
- Sem símbolos matemáticos

Exemplos:
- "Escalar porque o ROAS (6.8) está alto e o CTR (6.2) está bom"
- "Pausar porque o CPA (120.0) esta muito alto e o CTR (2.0) está fraco"
- "Testar porque o ROAS (3.2) é bom, mas o CTR (3.5) é mediano"

Campanhas:
{campaigns_text}

Responda SOMENTE em JSON no formato:
{{
  "pausar": [{{ "campanha": "", "motivo": "" }}],
  "escalar": [{{ "campanha": "", "motivo": "" }}],
  "testar": [{{ "campanha": "", "motivo": "" }}]
}}
"""



    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content
    return json.loads(content)

