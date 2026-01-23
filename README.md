# 🤖 AI Business Process Optimizer

Este projeto nasceu de uma inquietação simples:

> **Como conectar IA, automação e análise de dados de forma prática e próxima da realidade de um negócio?**

Em vez de estudar cada tecnologia de forma isolada, a ideia aqui foi **integrar tudo em um único fluxo**, simulando um cenário real de otimização de processos empresariais.

Nada de projeto de tutorial. Este repositório representa **estudo aplicado**, com erros, refatorações e decisões técnicas pensadas para escalar.

<img width="1024" height="687" alt="image" src="https://github.com/user-attachments/assets/323c3780-bb5b-4a81-8792-6197cf834a32" />

## Ativação do N8N para intermédio de API e Notion
<img width="737" height="627" alt="image" src="https://github.com/user-attachments/assets/04f6d8d7-54d0-4a9f-950d-ba9c8a75c7b0" />

## Registro dos processos solicitados e pendentes via API/Swagger - Python

<img width="1523" height="273" alt="image" src="https://github.com/user-attachments/assets/0dc35841-7d8c-46c3-a5c4-2451e7e560b7" />

## Visualização de dados via Streamlit com Dashboard - PowerBI (Análise de Dados)

https://github.com/user-attachments/assets/ef782ee1-12eb-489a-9e76-5ceb83a63977

---

## 🧠 Visão Geral do Fluxo

O sistema funciona como uma esteira inteligente de processos:

1. **API em Python (FastAPI)** recebe e gerencia os processos
2. **n8n** automatiza eventos e orquestra fluxos
3. **IA via OpenRouter (LLMs)** analisa processos e sugere melhorias
4. **Notion** atua como camada visual e organizacional do negócio
5. **Streamlit** apresenta dashboards e análises interativas
6. **Análise de dados** transforma eventos em insights acionáveis

📌 Tudo isso conectado de forma assíncrona, automatizada e auditável.

---

## 🏗️ Arquitetura (alto nível)

```
Usuário / Sistema
        ↓
 FastAPI (Python)
        ↓
      n8n (Automação)
        ↓
 OpenRouter (IA / LLMs)
        ↓
     Notion (Gestão)
        ↓
 Streamlit / Dashboards
```

---

## ⚙️ Tecnologias Utilizadas

### Backend & Automação

* **Python**
* **FastAPI**
* **n8n**
* **PostgreSQL**

### IA

* **OpenRouter** (integração com LLMs)
* Análise de processos e sugestões inteligentes

### Dados & Visualização

* **Streamlit**
* Conceitos de **Power BI & Storytelling de Dados**
* Pandas

### Organização

* **Notion API**

---

## 🚀 Funcionalidades

* 📥 Criação e versionamento de processos
* 🔄 Automação de eventos via webhook
* 🧠 Análise inteligente com IA
* 📊 Visualização de métricas e status
* 🗂️ Organização centralizada no Notion
* 📈 Base preparada para análises históricas

---

## 📦 Estrutura do Projeto

```
backend/
 ├── app/
 │   ├── api/
 │   ├── core/
 │   ├── services/
 │   ├── models/
 │   └── tests/

n8n/
 └── workflows/

streamlit/
 └── dashboard.py

notion/
 └── integration.py
```

---

## ▶️ Como Executar (resumido)

```bash
# Backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Streamlit
streamlit run dashboard.py
```

> ⚠️ É necessário configurar variáveis de ambiente para:
>
> * OpenRouter
> * Notion API
> * Banco de dados

---

## 🎯 Objetivo do Projeto

Este projeto tem como foco:

* Aprender **IA aplicada a processos reais**
* Explorar **automação de ponta a ponta**
* Unir **backend, dados e negócio**
* Construir algo que faria sentido em um ambiente corporativo

Não é um produto final. É um **laboratório vivo**.

---

## 📌 Próximos Passos

* [ ] Autenticação de usuários
* [ ] Controle de permissões
* [ ] Métricas avançadas de performance
* [ ] Logs inteligentes com IA
* [ ] Deploy em cloud

E correção de bugs!
---

## 🤝 Contribuições

Sugestões, ideias e feedbacks são muito bem-vindos.
Se quiser trocar ideia sobre IA, automação ou dados, fica à vontade para abrir uma issue.

---

## 📫 Contato

**Lucas de Souza Gomes**
Back-End Developer & Analista de Dados

* LinkedIn: https://www.linkedin.com/in/lucasdsgomes/

---

> 💡 *Estudar é importante. Construir conecta tudo.*
