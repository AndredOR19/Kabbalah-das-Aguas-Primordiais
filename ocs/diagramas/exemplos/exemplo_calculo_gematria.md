---
title: Exemplo de Uso do Script de Gematria
summary: |-
  Este exemplo demonstra como utilizar o script `calculate_gematria.py` para
  calcular o valor gemátrico de palavras ou frases hebraicas.  
  O arquivo deve ser colocado em `ocs/scripts/exemplos`.

## Pré‑requisitos

Certifique‑se de ter o Python 3 instalado em seu sistema.  
Para verificar, rode:

```bash
python3 --version
```

Caso não esteja instalado, consulte a documentação da sua distribuição para
procedimentos de instalação.

## Passo a passo

1. Abra um terminal e navegue até o diretório onde se encontra o script `calculate_gematria.py`.
2. Execute o script passando uma palavra ou frase hebraica como argumento.  
   Por exemplo, para calcular o valor de שלום (*shalom*):

   ```bash
   python3 calculate_gematria.py "שלום"
   ```

   A saída será algo semelhante a:

   ```
   Valor gemátrico de 'שלום': 376
   ```

3. Você pode calcular frases inteiras; o script somará o valor de cada letra conhecida e ignorará espaços ou sinais diacríticos (niqqud).  
   Exemplo:

   ```bash
   python3 calculate_gematria.py "בראשית ברא"
   ```

   **Saída:**

   ```
   Valor gemátrico de 'בראשית ברא': 914
   ```

## Integração futura

Este script é um ponto de partida. Ele pode ser integrado a módulos maiores do SCII para:  
- Analisar nomes completos.  
- Relacionar valores gemátricos com sefirot da Árvore da Vida.  
- Gerar relatórios automáticos durante consultas oraculares.

Sinta‑se à vontade para modificar e expandir conforme as necessidades de suas práticas.
