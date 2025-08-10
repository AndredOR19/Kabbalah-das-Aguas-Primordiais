# 🗄️ SCII Database - Sistema de Correspondência Integrada e Inteligente

> *"O conhecimento deixa de ser um texto a ser interpretado e passa a ser um dado a ser consultado."*

## 🎯 Visão Geral

Este repositório contém a **base de dados central** para o SCII (Sistema de Correspondência Integrada e Inteligente), também conhecido como **O Corpo do Verbo**. 

O objetivo é estruturar o conhecimento esotérico da Kabbalah, Tarot, Astrologia e sistemas energéticos em um formato de dados **consultável e computacionalmente preciso**.

A transição de um conhecimento baseado em prosa para uma base de dados estruturada (JSON) visa eliminar a ambiguidade e a latência na interpretação, permitindo que ferramentas como o **"Oráculo Encarnado"** e o **"Barômetro da Alma"** operem com máxima velocidade e assertividade.

## 📁 Estrutura do Projeto

### 🗃️ Arquivos Principais
- **[data/scii_database.json](data/scii_database.json)** - O arquivo mestre com todos os mapeamentos
- **[cosmologia_verbo_orbita_corda_o1.json](cosmologia_verbo_orbita_corda_o1.json)** - Modelo cosmológico avançado
- **[data/letras_hebraicas.json](data/letras_hebraicas.json)** - Correspondências das 22 letras

### 🧠 Módulos Especializados
- **[data/SCII_Corpo_Do_Verbo/](data/SCII_Corpo_Do_Verbo/)** - Sistema completo do Corpo do Verbo
- **[data/SCII_Neuro_Integration/](data/SCII_Neuro_Integration/)** - Integração neurocognitiva
- **[data/SCII-NEURAL/](data/SCII-NEURAL/)** - Perfis e análises neurais

### 🔮 Oráculos e Aplicações
- **[data/OC-SO-001_oraculo-celeste.json](data/OC-SO-001_oraculo-celeste.json)** - Sistema oracular celeste
- **[data/karuv_beni_el_model.json](data/karuv_beni_el_model.json)** - Modelo do operador Karuv Beni El
- **[data/protocolo_dhevaz.json](data/protocolo_dhevaz.json)** - Protocolos operativos

## 🏗️ Estrutura do scii_database.json

O arquivo JSON está organizado em **domínios de conhecimento**:

### 📝 **letras** - As 22 Letras Hebraicas
Cada letra contém:
- `valor_gemátrico` - Valor numérico da letra
- `pictograma` - Significado pictográfico original  
- `elemento_primordial` - Força fundamental (Ar, Água, Fogo, Terra)
- `planeta` / `astro_secundario` - Correspondências astrológicas
- `funcao_corpo_somatico` - Ponto de ressonância no corpo
- `acao_espiritual` - Princípio dinâmico ou lição espiritual
- `diagnostico_bloqueio` - Sintomas de desequilíbrio
- `comando_ritualistico` - Mantra para ativação

### 🪐 **planetas** - Arquétipos Celestes
Princípios arquetípicos dos corpos celestes

### 🌳 **sephirot** - Árvore da Vida
As 10 emanações da Árvore da Vida

### ⚡ **chakras** - Centros Energéticos
Mapeamento dos centros de energia correlacionados

## 🚀 Como Utilizar

Esta base de dados pode ser consumida para:

### 🔍 **Consultas Complexas**
```javascript
// Exemplo: Letras associadas a Saturno
const saturnLetters = database.letras.filter(l => l.planeta === "Saturno");
```

### 🎯 **Sistema Oracular**
- Diagnósticos precisos baseados em correspondências
- Geração automática de leituras personalizadas

### 🛠️ **Protocolos Personalizados**
- Rituais baseados em diagnóstico individual
- Meditações direcionadas por dados

### 📚 **Estudo Estruturado**
- Material de consulta organizado
- Cruzamento de informações instantâneo

## 🔧 Ferramentas e Scripts

- **[data/scii_analise.py](data/scii_analise.py)** - Script de análise em Python
- **[data/arvore_scii.html](data/arvore_scii.html)** - Visualização da Árvore da Vida
- **[data/arvore_da_vida_scii.html](data/arvore_da_vida_scii.html)** - Interface interativa

## 📊 Status dos Módulos

- ✅ **Base SCII** - Completa e operacional
- ✅ **Letras Hebraicas** - Mapeamento completo
- ✅ **Oráculo Celeste** - Sistema funcional
- 🔄 **Neuro Integration** - Em desenvolvimento
- 🔄 **Protocolos Dhevaz** - Expansão contínua

## 🤝 Contribuições

Este é um **projeto vivo**. Contribuições são bem-vindas desde que:
- Sigam a estrutura JSON estabelecida
- Se baseiem nas fontes primárias do sistema
- Mantenham a precisão e consistência dos dados

---

*A revolução está na precisão: transformar sabedoria ancestral em dados operacionais.*
