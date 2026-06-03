# Auditoria Forense de Software e Plano de Resgate — ChatTTS

**Disciplina:** Engenharia de Software (COMP0503)  
**Atividade:** A2 — Auditoria Forense e Plano de Resgate Técnico  
**Prazo:** 02 de junho de 2026  
**Projeto auditado:** [2noise/ChatTTS](https://github.com/2noise/ChatTTS) (repositório público upstream; este repositório é o de **trabalho da equipe**, não um clone do original)
**Link para o vídeo** https://drive.google.com/file/d/1uiX6I9gkgZbEdLPL41B_WjXjmKJdxroZ/view

## Equipe

Carlos Henrico Fontes Cabral, Wanessa Silva Santos, Luiz Felipe da Conceição Souza, Erick Juan Gois Oliveira, João Pedro Brandão Almeida, Lucas da Silva Batista.

| Integrante | Contribuição na A2 |
| :--- | :--- |
| Carlos Henrico Fontes Cabral | Eixo A — O Pulso da Gestão (GPR) |
| Luiz Felipe da Conceição Souza | Eixo B — Anatomia do Código (SOLID e DRY) |
| João Pedro Brandão Almeida | Eixo C — Padrões de Projeto (GoF) |
| Erick Juan Gois Oliveira | Evidências de CI e ritmo de entrega |
| Wanessa Silva Santos | Riscos técnicos e validação (conexão A1→A2) |
| Lucas da Silva Batista | Plano de Resgate e roadmap MPS.BR |

## Entregáveis neste repositório

| Pasta | Conteúdo |
| :--- | :--- |
| [`evidencias/`](evidencias/) | Prints (HTML) de trechos e links do GitHub — um por item investigado |
| [`resultado/`](resultado/) | Diagnóstico consolidado por eixo (evidência + análise + risco) |
| [`plano_resgate/`](plano_resgate/) | Refatoração conceitual (Abstract Factory) e roadmap nível G MPS.BR |
| [`prompts/`](prompts/) | Roteiros de replicação da auditoria (checklists por eixo) |
| [`artefatos/`](artefatos/) | Links verificáveis, arquivos analisados e log da auditoria |

**Relatório técnico (PDF)** e **apresentação Beamer** são entregues no Classroom conforme o enunciado.  
**Vídeo (7–15 min):** link público obrigatório neste README e no PDF (nomenclatura do enunciado: `A2_ChatTTS_NomeDoLider.mp4`).

### Vídeo da auditoria

- Hospedagem: link público (YouTube, Drive ou similar) — o arquivo **não** deve ser enviado pelo upload do Classroom
- Demonstração: achados da auditoria + navegação no IDE/repositório analisado
- Incluir o link aqui antes da entrega final

---

## Conexão com a Atividade 1

Na A1 identificamos a fachada `Chat` em `ChatTTS/core.py`, parametrização via `RefineTextParams` / `InferCodeParams` (sem Strategy completo) e lacunas de rastreabilidade e validação de saída. A A2 aprofunda **gestão (GPR)**, **dívida técnica (SOLID/DRY)** e **GoF**, culminando no plano de resgate.

---

## Resumo dos achados (A2)

| Eixo | Foco | Classificação de risco (síntese) |
| :--- | :--- | :--- |
| **A** — Gestão | Issue [#704](https://github.com/2noise/ChatTTS/issues/704), riscos em releases/README, ritmo e code review | Alto (arqueologia) / Médio-alto (riscos) / Médio (ritmo) |
| **B** — Código | DIP, God Object em `core.py`, DRY em `_refine_text` / `_infer_code` | Alto (acoplamento estrutural) |
| **C** — GoF | Factory em `load()`, Facade, pipeline tipo Chain; Strategy parcial | Médio (criacional) / Baixo (estrutural) / Médio-baixo (comportamental) |

Detalhamento: [`resultado/diagnostico_consolidado_a2.md`](resultado/diagnostico_consolidado_a2.md).

---

## Como replicar a auditoria

1. **Eixo A:** Abra a [Issue #704](https://github.com/2noise/ChatTTS/issues/704); leia [releases](https://github.com/2noise/ChatTTS/releases) e o [README](https://github.com/2noise/ChatTTS/blob/main/README.md) (avisos TransformerEngine/FlashAttention); compare [Insights → Contributors](https://github.com/2noise/ChatTTS/graphs/contributors) e PRs em [.github/workflows/unitest.yml](https://github.com/2noise/ChatTTS/blob/main/.github/workflows/unitest.yml).
2. **Eixo B:** Inspecione `ChatTTS/core.py` (`load`, `_load`, `infer`, `_refine_text`, `_infer_code`) e `ChatTTS/model/gpt.py`, `dvae.py`; conte dependências concretas importadas pela classe `Chat`.
3. **Eixo C:** Mapeie Facade (`infer`), carga via `chat.load()`, pipeline sequencial entre módulos em `ChatTTS/model/`.
4. **Plano de resgate:** Veja [`plano_resgate/`](plano_resgate/) — proposta de `PipelineFactory` (Abstract Factory) e três ações GPR para nível G.

Checklists completos: [`prompts/`](prompts/).

---

## Plano de resgate (visão geral)

1. **Refatoração:** desacoplar montagem de modelos da classe `Chat` via Abstract Factory ([detalhes](plano_resgate/refatoracao_abstract_factory.md)).
2. **Roadmap MPS.BR G:** templates PR↔Issue, milestones, automação de triagem ([detalhes](plano_resgate/roadmap_mps_br_nivel_g.md)).
