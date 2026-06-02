# Roadmap de maturidade — nível G (MPS.BR GPR)

Três ações imediatas se a equipe assumisse a manutenção do ecossistema ChatTTS.

## Ação 1 — Rastreabilidade (GRE → GPR → GCO)

| Item | Detalhe |
| :--- | :--- |
| **O quê** | Templates de Issue e Pull Request exigindo referência cruzada (`Relates to #N` / `Fixes #N`) |
| **Por quê** | Issue #704 exemplifica documentação rica sem fechamento rastreável até PR |
| **Evidência esperada** | PRs com links clicáveis para issues; GRE 1, 2, 4 |
| **Prazo sugerido** | Mês 1 |

## Ação 2 — Controle de ritmo via Milestones

| Item | Detalhe |
| :--- | :--- |
| **O quê** | Milestones trimestrais alinhados ao roadmap público (streaming, emoções, backends) |
| **Por quê** | Gráfico de contribuições com picos (“crunch”) sem marcos formais |
| **Evidência esperada** | Aba Milestones ativa no GitHub com datas |
| **Prazo sugerido** | Mês 2 |

## Ação 3 — Automação da triagem de riscos

| Item | Detalhe |
| :--- | :--- |
| **O quê** | Workflow em `.github/workflows/` para rotular PRs com arquivos em `ChatTTS/core.py` ou dependências críticas; checklist de dívida técnica |
| **Por quê** | Complementar `unitest.yml` (verificação) com governança visível |
| **Evidência esperada** | Novo YAML em `.github/workflows/`; GPR 4, 7 |
| **Prazo sugerido** | Mês 3 |

## Linha do tempo

| Período | Foco |
| :--- | :--- |
| Mês 1 | Governança — templates e regras de rastreabilidade |
| Mês 2 | Monitoramento — milestones e registro de riscos técnicos |
| Mês 3 | Consolidação — automações CI/CD e homologação práticas nível G |

## Conexão com validação de IA (A1 → A2)

Formalizar critérios de aceite para saída de áudio (mesmo que proxy: duração, energia, WER opcional) como extensão da Ação 3, reduzindo risco de “alucinação” acústica sem camada GQA isolada.
