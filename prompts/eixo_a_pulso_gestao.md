# Eixo A — O Pulso da Gestão (MPS.BR GPR)

## 1. Arqueologia de Issues

**Caso obrigatório da equipe:** [Issue #704](https://github.com/2noise/ChatTTS/issues/704)

| Pergunta | Onde verificar |
| :--- | :--- |
| Quem abriu? | Autor na issue (LivinLuo1993, 20/08/2024) |
| Discussão e mudança de escopo? | Comentários: de falha de `chat.load()` para pipeline de embeddings de voz |
| Documentação? | Descrição, logs, código na issue; labels `documentation`, `stale` |
| Vínculo com PR? | Aba "Development" / busca `Fixes #704` nos PRs |

**Evidência:** print em `evidencias/eixo_a_issue_704.html` + link direto.

**Risco registrado pela equipe:** Alto.

---

## 2. Gestão de Riscos Ocultos

| Fonte | O que buscar |
| :--- | :--- |
| [README.md](https://github.com/2noise/ChatTTS/blob/main/README.md) | Avisos sobre TransformerEngine / FlashAttention-2 em produção |
| [Releases](https://github.com/2noise/ChatTTS/releases) | Correções de inferência, Transformers, streaming |
| Raiz do repo | Ausência de `SECURITY.md` |
| Código | Poucos `TODO`/`FIXME` públicos; dívida em avisos e releases |

**Evidência:** `evidencias/eixo_a_readme_riscos_dependencias.html`

**Risco:** Médio-alto.

---

## 3. Ritmo de Entrega e Code Review

| Fonte | O que buscar |
| :--- | :--- |
| [Contributors graph](https://github.com/2noise/ChatTTS/graphs/contributors) | Picos vs. cadência constante |
| Pull Requests | Comentários de revisão vs. merge rápido |
| [.github/workflows/unitest.yml](https://github.com/2noise/ChatTTS/blob/main/.github/workflows/unitest.yml) | Verificação automatizada no CI |

**Evidência:** `evidencias/eixo_a_ci_unitest.html`

**Risco:** Médio.
