# Log da auditoria de testes — A3

| Data | Atividade | Saída |
| :--- | :--- | :--- |
| 2026-06-15 | Revisão achados A1/A2 (core.py, validação de áudio) | Seção conexão no relatório |
| 2026-06-18 | Inventário pasta `tests/` e `testall.sh` | `evidencias/eixo_a_estrutura_tests.html` |
| 2026-06-20 | Análise CI `unitest.yml` | `evidencias/eixo_a_ci_unitest.html` |
| 2026-06-22 | Qualidade técnica (#511.py, #655.py, mocks) | `evidencias/eixo_b_*.html` |
| 2026-06-25 | Mapeamento lacunas e módulos críticos | `evidencias/eixo_c_*.html` |
| 2026-06-28 | Plano de evolução e snippets pytest | `plano_evolucao/`, `snippets/` |
| 2026-06-30 | Reorganização repositório para A3 | README, remoção artefatos A2 |

## Checklist de entrega (enunciado)

- [x] Repositório GitHub com artefatos de replicação
- [x] README com tutorial de replicação
- [x] Prompts/checklists por eixo
- [x] Snippets de testes propostos
- [ ] Link do vídeo de apresentação no README e no PDF
- [ ] Relatório técnico PDF no Classroom
- [ ] Post da URL do repositório na thread do Classroom

## Comandos de verificação local

```bash
pip install pytest numpy
pytest snippets/ -v
```
