# 🔬 SCII - Módulo de Medição e Análise de HRV

> *"O que não se mede, não se melhora. O que não se melhora, se degrada sempre."*

Este diretório contém o ciclo completo de **Calibração Automática de HRV (Variabilidade da Frequência Cardíaca)**, uma das ferramentas centrais do Sistema de Correspondência Integrada e Inteligente (SCII).

O objetivo deste módulo é fornecer um feedback quantitativo e qualitativo sobre o alinhamento do praticante com a assinatura vibracional de uma determinada prática cabalística.

## 🔄 O Ciclo de Calibração

O sistema opera em um ciclo de 3+1 etapas:

1.  **Medição**: Captura os dados de HRV durante a prática.
2.  **Análise**: Compara os dados com a assinatura arquetípica ideal.
3.  **Feedback**: Fornece instruções claras para a próxima calibração.
4.  **Visualização**: Gera um gráfico para análise visual dos dados.

## 📂 Estrutura do Módulo

- **`medicao_hrv.py`**: O ponto de partida. Simula a coleta de dados de um sensor de HRV.
- **`analise_hrv.py`**: O cérebro. Analisa os dados coletados e gera um relatório.
- **`feedback_pratico.py`**: O guia. Traduz a análise em instruções práticas.
- **`visualizacao_hrv.py`**: O olho. Transforma os dados brutos em um gráfico visual.

## 🚀 Como Utilizar o Módulo

Os scripts foram projetados para serem usados de forma modular e interativa através da linha de comando.

### 1. Medição

Inicie uma medição especificando a duração e o nome da prática.

```bash
python3 scii_medicao_hrv/medicao_hrv.py --duracao 30 --pratica "Contemplacao_Binah"
```

Isso irá gerar um arquivo de dados, como `scii_medicao_hrv/Contemplacao_Binah_2025-08-12_00-30-00.json`.

### 2. Análise

Analise o arquivo gerado, fornecendo o nome da prática para que o sistema possa usar a assinatura arquetípica correta.

```bash
python3 scii_medicao_hrv/analise_hrv.py scii_medicao_hrv/Contemplacao_Binah_2025-08-12_00-30-00.json --pratica "Contemplacao_Binah"
```

Isso irá imprimir um relatório de análise detalhado no terminal.

### 3. Feedback (Usando Pipe)

Para obter um feedback direto, você pode "encanar" (pipe) a saída da análise para o script de feedback.

```bash
python3 scii_medicao_hrv/analise_hrv.py scii_medicao_hrv/Contemplacao_Binah_2025-08-12_00-30-00.json --pratica "Contemplacao_Binah" | python3 scii_medicao_hrv/feedback_pratico.py --pratica "Contemplacao_Binah"
```

Isso irá gerar uma instrução clara e direcionada para sua próxima prática.

### 4. Visualização

A qualquer momento, você pode gerar um gráfico a partir de um arquivo de medição.

```bash
python3 scii_medicao_hrv/visualizacao_hrv.py scii_medicao_hrv/Contemplacao_Binah_2025-08-12_00-30-00.json
```

Isso criará um arquivo de imagem, como `Contemplacao_Binah_2025-08-12_00-30-00_grafico.png`.

## 🧠 Banco de Assinaturas Arquetípicas

O coração do módulo de análise é o banco de dados de assinaturas encontrado em `analise_hrv.py`. Ele contém os valores ideais de HRV para diferentes práticas.

```python
ASSINATURAS = {
    "Ativacao_Aleph": {
        "hrv_media_ideal": 60.0,
        "desvio_padrao_ideal": 15.0
    },
    "Meditacao_Tiferet": {
        "hrv_media_ideal": 75.0,
        "desvio_padrao_ideal": 12.0
    },
    # ... e outras assinaturas
}
```

Para adicionar novas práticas, basta expandir este dicionário.

## 🛠️ Dependências

Para usar este módulo, você precisa das seguintes bibliotecas Python:

- `numpy`
- `matplotlib`
- `pytest` (para executar os testes)

Você pode instalá-las com:

```bash
pip install numpy matplotlib pytest
```

## 🧪 Testes

Para garantir a confiabilidade do módulo, testes unitários foram criados na pasta `tests/`. Para executá-los, use o comando:

```bash
pytest tests/
```

---

*Este módulo representa um passo fundamental na fusão da sabedoria cabalística com a tecnologia de biossensores, criando um sistema de feedback em tempo real para a jornada espiritual.*
