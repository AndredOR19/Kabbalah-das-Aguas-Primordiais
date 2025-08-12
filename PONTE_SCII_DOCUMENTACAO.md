# SCII-Core: Ponte Sismógrafo-Atlas

## Visão Geral

O arquivo `scii_database.json` agora funciona como o **SCII-Core** - o cérebro unificado que permite a integração perfeita entre o Sismógrafo Emocional e o Atlas Anatômico 3D.

## Estrutura da Ponte

### 1. Campos Essenciais Adicionados às Letras

Cada letra hebraica agora possui os campos necessários para a ponte:

```json
{
  "id": "KAPH_020",                    // Identificador único
  "letra_hebraica": "כ",               // Símbolo hebraico
  "nome_anatomico": "Fígado",          // Nome para o Atlas
  "id_mesh_3d": "Liver_Mesh",         // ID técnico para o modelo 3D
  "emocoes_associadas": [              // CAMPO-CHAVE: emoções detectáveis
    "frustração", 
    "raiva_reprimida", 
    "estagnação"
  ],
  "estados_chave": [                   // CAMPO-CHAVE: estados fisiológicos
    "foco_baixo", 
    "hrv_baixo", 
    "digestão_lenta"
  ],
  "funcao_espiritual": "...",          // Função no Corpo do Verbo
  "pratica_sugerida": "..."            // Prática terapêutica
}
```

### 2. Seção de Mapeamento Direto

A seção `ponte_sismografo_atlas` contém:

#### A. Mapeamento Emoções → Anatomia
```json
"mapeamento_emocoes_anatomia": {
  "frustração": {
    "sistema_anatomico": "Fígado",
    "letra_hebraica": "Kaph",
    "id_mesh_3d": "Liver_Mesh",
    "intensidade_base": 0.7,
    "cor_visualizacao": "#FF6B35"
  }
}
```

#### B. Estados Fisiológicos
```json
"estados_fisiologicos": {
  "hrv_baixo": {
    "sistemas_afetados": ["Liver_Mesh", "Respiratory_System_Mesh"],
    "intensidade_multiplicador": 1.2,
    "duracao_visualizacao": 3000
  }
}
```

#### C. Configuração da Ponte
```json
"configuracao_ponte": {
  "intervalo_atualizacao_ms": 1000,
  "threshold_emocional": 0.3,
  "fade_duration_ms": 2000,
  "max_intensidade": 1.0,
  "debug_mode": true
}
```

## Fluxo de Funcionamento

### 1. Detecção (Sismógrafo)
- Sismógrafo detecta palavra "frustração" em commit
- Consulta `mapeamento_emocoes_anatomia["frustração"]`
- Obtém: `id_mesh_3d: "Liver_Mesh"`

### 2. Visualização (Atlas)
- Atlas recebe comando: `iluminar("Liver_Mesh", intensidade: 0.7, cor: "#FF6B35")`
- Aplica efeito visual no modelo 3D do fígado
- Duração baseada em `configuracao_ponte`

### 3. Integração Espiritual
- Sistema consulta letra hebraica "Kaph"
- Exibe função espiritual: "Filtro emocional e energético"
- Sugere prática: "Desintoxicação emocional"

## Correspondências Principais Implementadas

| Emoção | Sistema Anatômico | Letra | Mesh 3D | Cor |
|--------|------------------|-------|---------|-----|
| Frustração | Fígado | Kaph (כ) | Liver_Mesh | #FF6B35 |
| Ansiedade | Sistema Respiratório | Aleph (א) | Respiratory_System_Mesh | #87CEEB |
| Indecisão | Sistema Muscular | Zayin (ז) | Muscular_System_Mesh | #FFD700 |
| Isolamento | Caixa Torácica | Cheth (ח) | Ribcage_Mesh | #696969 |
| Vergonha | Intestinos | Teth (ט) | Intestinal_System_Mesh | #8B0000 |

## Próximos Passos

1. **Completar todas as 22 letras** com os campos essenciais
2. **Expandir mapeamento emocional** com mais emoções
3. **Implementar API de comunicação** entre os sistemas
4. **Criar interface de configuração** para ajustes em tempo real
5. **Adicionar sistema de aprendizado** para refinamento automático

## Uso Técnico

### Para o Sismógrafo:
```javascript
// Consultar mapeamento
const emocao = "frustração";
const mapeamento = sciiCore.ponte_sismografo_atlas.mapeamento_emocoes_anatomia[emocao];
const meshId = mapeamento.id_mesh_3d; // "Liver_Mesh"
```

### Para o Atlas:
```javascript
// Receber comando de iluminação
function iluminarSistema(meshId, intensidade, cor, duracao) {
  const mesh = scene.getObjectByName(meshId);
  mesh.material.emissive.setHex(cor);
  mesh.material.emissiveIntensity = intensidade;
  // Aplicar fade após duracao
}
```

## Filosofia da Integração

Esta ponte não é apenas técnica - é uma manifestação do princípio hermético "Como acima, assim abaixo". Cada emoção detectada no plano digital (commits, código) encontra sua correspondência no plano físico (anatomia 3D) através da sabedoria ancestral das letras hebraicas.

O resultado é um sistema que não apenas visualiza, mas **ensina** - transformando cada momento de tensão emocional em uma oportunidade de autoconhecimento e cura.