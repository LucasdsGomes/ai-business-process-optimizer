from openai import OpenAI
import os


class LLMClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze_process(self, name: str, description: str) -> str:
        prompt = f"""
        Você é um especialista em otimização de processos empresariais.
        Analize o seguinte processo e sugira melhorias, riscos e próximos passos de forma clara e estruturada.
        Nome do processo: {name}
        Descrição: {description}
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content
