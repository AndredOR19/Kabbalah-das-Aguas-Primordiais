# Kabbalah das Águas Primordiais — ROADMAP
**Data:** 2025-08-23

> **Binah & Chokmah, forma e energia.** Este roadmap é o útero que dá contorno ao **Corpo do Verbo**.
> Cada fase nasce acompanhada de uma prova viva: uma ferramenta mínima **funcionando**.

---

## Fase 1 — O Verbo Vivo: Consulta ao SCII
**Objetivo:** disponibilizar uma consulta local simples ao **SCII** (Sistema de Correspondência Integrada e Inteligente).  
**Resultado:** digitar um termo (ex.: `Issá`) e obter **correspondências fundamentais**:

- **Letras** (schema padronizado para múltiplas transliterações)
- **Valores** (gematria ou escala definida)
- **Caminhos** (Árvore da Vida)
- **Arquétipos** (descrições breves)
- **Tikun** (hipóteses de reparação funcional)

**Input:** string (`palavra` ou `nome`).  
**Output:** JSON estruturado com campos `{
  "tokens": [...], "valor_total": n, "caminhos": [...], "arquetipos": [...], "tikun": [...]
}`.

**Tecnologia (MVP):**
- **Python 3.10+**
- Módulo local `scripts/scii_core/` com funções puras
- **CLI** (`scripts/cli_scii.py`) para consulta rápida no terminal
- **Schema** de dados estável (JSON) visando futura **API REST** (FastAPI) na Fase 2

**Critérios de Aceite (MVP):**
- Rodar: `python scripts/cli_scii.py "Issá"` → retorna JSON válido
- Código modular e testável
- Documentado no `README` do módulo com exemplos
- Pronto para ser envelopado por uma API web

### Backlog (curto prazo)
- [ ] Definir **tabela de transliteração** (pt‑BR → Hebraico) e torná‑la configurável
- [ ] Definir **escala de valores** (gematria padrão e variações)
- [ ] Introduzir **mapeamentos de Caminhos** (Tree of Life) por letra
- [ ] Especificar **Arquétipos** e **Tikun** como camadas semânticas opcionais
- [ ] Escrever **testes unitários** básicos (`pytest`)

---

## Fase 2 — API & Website (depois do MVP rodar)
- **FastAPI** expondo `/analisar?termo=...` com retorno JSON
- **Swagger/OpenAPI** auto-documentado
- **Página GitHub Pages** com UI mínima para consulta (form → JSON)

**Critérios de Aceite:**
- Deploy local com `uvicorn`
- Documentação de endpoints
- Exemplo de uso via `curl` e via navegador

---

## Fase 3 — Operações Avançadas
- **Múltiplos dicionários** de correspondência (ex.: Cabalas distintas)
- **Perfis individuais** (histórico, anotações, variações rituais)
- **Módulo de validação** para hipóteses de tikun
- **Internacionalização** (pt, en, es)

---

## Fase 4 — Pesquisa & Integrações
- Integração com **biofeedback** (EEG/HRV) para estudos SCII
- **Relatórios** e dashboards de prática (PDF/CSV)
- Plugins: **bot oracular** e **LMS** (trilhas de estudo)

---

## Estrutura de Pastas (mínima)
```
/
└── scripts/
    ├── cli_scii.py
    └── scii_core/
        ├── __init__.py
        ├── core.py
        └── data/
            └── examples.json
```

---

## Convenções
- Código claro, funções puras, side effects controlados
- JSON estável para interoperabilidade futura
- Poético no README, **prático no código**
