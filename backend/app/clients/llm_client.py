from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )

    def analyze_process(self, name: str, description: str) -> str:
        prompt = f"""
Você é um especialista em otimização de processos empresariais.

Analise o processo abaixo e retorne:
1. Principais gargalos
2. Riscos operacionais
3. Sugestões de melhoria
4. Próximos passos recomendados

Nome do processo:
{name}

Descrição do processo:
{description}
"""

        response = self.client.chat.completions.create(
    model="deepseek/deepseek-r1-0528:free",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.4,
)


        return response.choices[0].message.content
