# Kabbalah das Águas Primordiais - Roadmap

## Fase 1: O Verbo Vivo - A Consulta ao SCII

- **Objetivo**: Criar a primeira ferramenta do sistema — a consulta básica ao SCII (Sistema de Correspondências Interdimensionais Integradas).
- **Input**: Uma palavra ou nome (ex: "Issá").
- **Output**: As correspondências fundamentais: letras, valores, caminhos, arquétipos, tikun.
- **Tecnologia**: Script Python inicial, com futura API REST como alvo.

---

## Fase 2: Primeira Boca do Oráculo - CLI SCII

- **Objetivo**: Criar uma interface de linha de comando que permita consultas ao SCII diretamente do terminal.
- **Comando**: `python scii_cli.py "Issá"`
- **Resultado**: Impressão formatada das correspondências fundamentais e da gematria total.

---

## Fase 2.5: A Boca do Oráculo na Rede - API SCII

- **Objetivo**: Criar uma API com FastAPI que exponha o SCII como serviço web.
- **Rota**: `GET /scii/{palavra}`
- **Resultado**: JSON com letras, valores, arquétipos, caminhos, tikun e soma gemátrica.
- **Futuro**: Evoluir para interface web interativa e aplicativo mobile.
