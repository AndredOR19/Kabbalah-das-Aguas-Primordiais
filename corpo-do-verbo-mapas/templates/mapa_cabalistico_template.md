# {{ identidade.nome }} — Mapa Cabalístico (Corpo do Verbo / SCII)

**Autor:** {{ meta.autor_analise }}  
**Versão do Template:** {{ meta.versao_template }}

---

## Capa — Identidade Vibracional

- Nome civil: **{{ identidade.nome }}**  
- Pseudônimo espiritual: **{{ identidade.pseudonimo | default('—') }}**  
- Nascimento: **{{ identidade.data_nascimento }} {{ identidade.hora_nascimento }} — {{ identidade.local_nascimento }}**

### Assinatura Operativa (resumo)
- Eixos: {{ assinaturas.eixos | join(', ') }}  
- Letras-chave: {{ assinaturas.letras_chave | join(', ') }}  
- Portais: {{ assinaturas.portais_operativos | join('; ') }}

---

## Sumário
1. Camada 1 — História Simples
2. Camada 2 — Tradução Técnica (Corpo do Verbo)
3. Camada 3 — Operatividade Vibracional (SCII)
4. Diagrama de Fluxo Cabalístico
5. Roteiro Operativo (Rituais & Práticas)
6. Anexos (Aspectos e Tabelas)

---

## 1) Camada 1 — História Simples

{{ bloco_historia_simples }}

---

## 2) Camada 2 — Tradução Técnica (Corpo do Verbo)

### 2.1 Sol
- Signo/Casa: **{{ posicoes.Sol.signo }} / Casa {{ posicoes.Sol.casa }}**
- Letra / Caminho / Arcano: **{{ sol.letra }} / {{ sol.caminho }} / {{ sol.arcano }}**
- Função: {{ sol.funcao }}

### 2.2 Lua
- Signo/Casa: **{{ posicoes.Lua.signo }} / Casa {{ posicoes.Lua.casa }}**
- Letra / Caminho / Arcano: **{{ lua.letra }} / {{ lua.caminho }} / {{ lua.arcano }}**
- Função: {{ lua.funcao }}

<!-- Repita para Mercúrio, Vênus, Marte, Júpiter, Saturno, Urano, Netuno, Plutão, Asc/MC/IC/DC -->

{{ bloco_traducao_tecnica }}

---

## 3) Camada 3 — Operatividade Vibracional (SCII)

### 3.1 Gatilhos e Portais
- **Porta do Espelho (Casa 7):** {{ scii.porta_espelho }}
- **Caminho Nun (24):** {{ scii.nun_efeito }}
- **Loops Alquímicos:** {{ scii.loops_alquimicos | join('; ') }}

### 3.2 Padrão de Travessia (Eixo)
- **{{ assinaturas.eixos[0] }}** → {{ scii.descricao_eixo_principal }}

{{ bloco_operatividade }}

---

## 4) Diagrama de Fluxo Cabalístico

```mermaid
flowchart LR
  A[Netzach] -- Caminho 24 / Nun --> B[Tiphareth]
  B --> C[Expressão no Mundo]
```

---

## 5) Roteiro Operativo (Rituais & Práticas)

Ver Camada 3 para exercícios de travessia, ancoragem e visão.

---

## 6) Anexos

### 6.1 Aspectos (orbes)

{% for asp in posicoes.Sol.aspectos %}

* Sol {{ asp.tipo }} {{ asp.com }} (orbe {{ asp.orbe }})
  {% endfor %}

### 6.2 Tabelas de Correspondência

|                            Letra |     Caminho     |     Arcano     | Função         |
| -------------------------------: | :-------------: | :------------: | :------------- |
| {% for k, v in letras.items() %} |                 |                |                |
|                          {{ k }} | {{ v.caminho }} | {{ v.arcano }} | {{ v.funcao }} |
|                     {% endfor %} |                 |                |                |