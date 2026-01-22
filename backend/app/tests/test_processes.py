def test_create_process(client):
    payload = {
        "name": "Processo Teste",
        "description": "Descrição do processo",
        "type": "BUSINESS"
    }

    response = client.post("/api/v1/processes/", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]


def test_list_processes(client):
    response = client.get("/api/v1/processes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_analyze_process(client, monkeypatch):
    # cria processo primeiro
    payload = {
        "name": "Processo para análise",
        "description": "Teste",
        "type": "BUSINESS"
    }

    create = client.post("/api/v1/processes/", json=payload)
    process_id = create.json()["id"]

    # mock do LLM
    def fake_analyze(*args, **kwargs):
        return "Análise mockada com sucesso"

    monkeypatch.setattr(
        "backend.app.api.v1.processes.service.LLMClient.analyze_process",
        fake_analyze
    )

    response = client.post(f"/api/v1/processes/{process_id}/analyze")

    assert response.status_code == 200
    assert "analysis" in response.json()
