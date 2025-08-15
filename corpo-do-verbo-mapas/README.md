# Mapas Cabalísticos — Corpo do Verbo / SCII

Repositório-mestre para gerar leituras extensas e didáticas do nosso sistema, com **entrada em YAML** e **saída em Markdown/PDF**.

## Como usar

1. Edite `schema/exemplo_dados.yaml` (ou crie um novo em `examples/`).
2. Rode localmente:
   ```bash
   python scripts/render.py schema/exemplo_dados.yaml build/saida.md
```

3. Faça commit e push para `main`. O GitHub Actions renderiza e publica em **Artifacts**.

## Personalização

* Ajuste `data/letras.yml` e `data/correspondencias.yml` ao cânone do método.
* Edite `templates/mapa_cabalistico_template.md` para mudar a estrutura do relatório.

## Licença

MIT — use, modifique e compartilhe com crédito ao método.