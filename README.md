# AI Ads Agent 🤖📊

## Visão Geral
Este projeto é um **agente inteligente para análise e otimização de campanhas de marketing digital**, desenvolvido com foco em aplicação prática de **Inteligência Artificial orientada a dados**. O sistema automatiza a leitura de métricas de campanhas, analisa o desempenho com apoio de um modelo de linguagem (LLM) e gera **recomendações estratégicas explicáveis**, como pausar, testar ou escalar campanhas.

O projeto simula um cenário real de negócio, integrando **backend, IA e visualização de dados**, permitindo que os resultados sejam consumidos por ferramentas de BI como o Power BI.

---

## Objetivo do Projeto
Demonstrar como a Inteligência Artificial pode ser utilizada para **auxiliar a tomada de decisão**, indo além de simples cálculos estatísticos. O agente:

- Interpreta métricas de marketing
- Aplica regras de negócio bem definidas
- Usa IA para contextualizar decisões
- Retorna resultados estruturados e prontos para visualização

---

## Inteligência Artificial Utilizada
A IA do projeto é baseada em um **Large Language Model (LLM)**, utilizado como um **motor de raciocínio e explicação**.

### Papel da IA no sistema
A IA é responsável por:
- Analisar campanhas com base em métricas fornecidas
- Aplicar regras de decisão previamente definidas
- Classificar campanhas em **pausar**, **testar** ou **escalar**
- Gerar **justificativas em linguagem natural**, tornando as decisões interpretáveis

### Observações importantes
- A IA **não cria regras novas**
- Todas as decisões seguem critérios objetivos
- O modelo atua como um **agente analítico**, não apenas como gerador de texto

Essa abordagem aproxima o projeto de cenários reais de uso de IA em empresas, onde **controle e explicabilidade** são fundamentais.

---

## Dados Utilizados
Os dados utilizados são **dados fictícios de campanhas de anúncios**, armazenados em um arquivo CSV.

### Principais métricas analisadas
- **ROAS (Return on Ad Spend)**
- **CPA (Custo por Aquisição)**
- **CTR (Click Through Rate)**

Essas métricas são amplamente utilizadas no mercado de marketing digital e permitem avaliar eficiência, custo e engajamento das campanhas.

---

## Regras de Decisão

### Pausar campanha
- ROAS < 1.2 **ou**
- CPA > 60 **ou**
- CTR < 1.5

### Escalar campanha
- ROAS ≥ 2.0 **e**
- CPA ≤ 40 **e**
- CTR ≥ 5

### Testar campanha
- Quando não se enquadra nos critérios de pausar ou escalar

Essas regras simulam decisões reais tomadas por gestores de tráfego e analistas de marketing.

---

## Arquitetura do Projeto
O projeto segue uma arquitetura modular e organizada:

- **Coleta de dados**: leitura e preparação dos dados de campanhas
- **Análise com IA**: envio das métricas ao modelo de linguagem para classificação e explicação
- **Persistência**: armazenamento das decisões geradas
- **API REST**: exposição dos resultados via endpoints
- **Visualização**: consumo dos dados pelo Power BI

Essa separação facilita manutenção, escalabilidade e reutilização do código.

---

## API REST
A aplicação é exposta como uma **API REST**, desenvolvida com FastAPI.

### Principais endpoints
- `POST /pipeline/run`
  - Executa todo o pipeline de análise
  - Processa os dados e gera as decisões

- `GET /pipeline/results`
  - Retorna os resultados já processados
  - Endpoint ideal para consumo por ferramentas de BI

Essa separação segue boas práticas de integração de sistemas.

---

## Integração com Power BI
Os resultados são disponibilizados em formato **JSON estruturado**, facilitando a integração direta com o Power BI via conector Web.

Isso permite:
- Atualização automática dos dados
- Criação de dashboards analíticos
- Visualização de campanhas por status
- Acompanhamento da tomada de decisão da IA

---

## Tecnologias Utilizadas
- Python
- FastAPI
- Pandas
- Large Language Model (LLM)
- Power BI
- CSV como fonte de dados

---

## Aprendizados e Diferenciais
Este projeto demonstra:
- Aplicação prática de IA em um problema real
- Uso de LLMs como agentes de decisão
- Integração entre backend, IA e BI
- Preocupação com explicabilidade das decisões
- Organização de pipeline analítico

Ele reflete uma abordagem moderna de uso de IA, focada em **impacto no negócio**, e não apenas em modelos isolados.

---

## Possíveis Evoluções
- Persistência em banco de dados (PostgreSQL)
- Histórico de decisões
- Autenticação na API
- Agendamento automático do pipeline
- Dashboards mais avançados no Power BI

---

## 📊 Dashboard no Power BI

O dashboard foi desenvolvido para visualizar as decisões geradas pela IA sobre campanhas de marketing digital.

### Principais indicadores exibidos:
- Quantidade de campanhas recomendadas para **escalar**
- Quantidade de campanhas recomendadas para **pausar**
- Campanhas em **observação/teste**
- Decisão da IA por campanha
- Análise visual clara para apoio à tomada de decisão

### Destaques do dashboard:
- Cores semânticas:
  - 🟢 Escalar (alto desempenho)
  - 🔴 Pausar (baixo desempenho)
  - 🟡 Testar (necessita mais dados)
- KPIs destacados no topo para leitura rápida
- Visual focado em gestores e analistas de marketing

### Prints do Dashboard
![Visão Geral](dashboard/screenshots/overview.png)


## Conclusão
O **AI Ads Agent** une **dados, inteligência artificial e engenharia de software**, mostrando como a IA pode ser utilizada como suporte real à tomada de decisão, de forma explicável, integrada e orientada a resultados.
