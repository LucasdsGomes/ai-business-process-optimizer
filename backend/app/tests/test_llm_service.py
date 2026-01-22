from backend.app.clients import llm_client

def test_llm_client_prompt_generation(monkeypatch):
    class FakeResponse:
        class Choice:
            class Message:
                content = "Resposta simulada"

            message = Message()

        choices = [Choice()]

    class FakeClient:
        def chat(self):
            pass

        class chat:
            class completions:
                @staticmethod
                def create(*args, **kwargs):
                    return FakeResponse()

    # Monkeypatch direto no objeto importado
    monkeypatch.setattr(llm_client, "OpenAI", lambda **kwargs: FakeClient())
