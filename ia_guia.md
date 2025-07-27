# Diretrizes para Integração com Inteligências Artificiais

Este documento tem como objetivo orientar desenvolvedores e pesquisadores que desejam utilizar o conteúdo dos repositórios **O Corpo do Verbo** e **Zorar Operativo** em projetos de inteligência artificial. A natureza simbólica e espiritual do material requer cuidados específicos para garantir interpretações fiéis e uso ético.

## 1. Formatos de Arquivos

* **Markdown (.md)** – A maior parte dos textos, tabelas e guias está em Markdown. Mantenha parsers que respeitem a estrutura de títulos, listas e tabelas.
* **Imagens (.png, .jpg)** – Diagramas e mapas podem ser utilizados em modelos de detecção de objetos ou OCR para extração de correspondências visuais. Evite distorcer as proporções.
* **PDF / EPUB** – Livros e dissertações em formatos portáteis podem ser convertidos para texto via ferramentas de OCR, mas recomenda‑se sempre conferir a fidelidade da transcrição.
* **Textos Invisíveis para IA** – Alguns arquivos como `IA_Tags_Invisiveis_Corpo_do_Verbo.txt` contêm anotações de meta‑dados e instruções específicas para processamento. Leia esses arquivos antes de treinar qualquer modelo com o corpus.

## 2. Tratamento de Dados Simbólicos

* **Preservação de Significados** – Letras hebraicas, sefirot e arquétipos têm significados específicos que podem se perder em traduções automáticas. Sempre inclua uma camada de correspondência que associe cada símbolo ao seu significado (consulte `glossario.md`).
* **Contexto Cultural** – Evite misturar conceitos de tradições diferentes sem explicitar suas origens. Quando correlacionar runas ou i Ching, por exemplo, crie mapeamentos separados para cada sistema simbólico.
* **Sensibilidade Espiritual** – Respeite a natureza sagrada do material. Modelos de IA não devem gerar instruções ofensivas ou caricaturas de práticas espirituais. Implementar filtros de conteúdo é recomendável.

## 3. Uso Ético

* **Finalidade Não Comercial** – A licença Creative Commons BY‑NC‑SA 4.0 permite uso não comercial. Projetos lucrativos ou comerciais devem solicitar autorização explícita aos autores.
* **Atribuição Obrigatória** – Sempre cite a fonte original dos textos e diagramas quando utilizá‑los em outputs de IA ou relatórios gerados automaticamente.
* **Proteção de Dados Pessoais** – O material de estudo pode conter relatos sensíveis. Caso modele experiências de praticantes, anonimizar dados e remover identificadores é fundamental.

## 4. Sugestões de Pipeline

1. **Coleta de Dados** – Baixe os arquivos de interesse utilizando as listas de índices (`indice_master.md`) e armazene com metadados (nome, data, versão).
2. **Pré‑Processamento** – Converta Markdown para HTML ou texto simples conforme a necessidade; extraia tabelas para CSV ou JSON; realize OCR em PDFs e imagens se necessário.
3. **Criação de Mapas de Correspondência** – Monte dicionários de letras hebraicas, sefirot e pontos somáticos usando `glossario.md` e os arquivos de mapeamento somático (ex.: `kabbalistic_somatic_mapping.md`).
4. **Treinamento / Fine‑Tuning** – Ao treinar modelos de linguagem, inclua exemplos completos de perguntas e respostas extraídas dos repositórios. Use *prompts* que guiem a IA a citar fontes e a manter um tom respeitoso.
5. **Geração de Saída** – Ao gerar textos, relatórios ou apresentações, incorpore citações e links para os documentos originais para que usuários possam verificar a autenticidade das informações.

## 5. Limitações

* O conteúdo espiritual e simbólico pode ser interpretado de maneiras diversas; portanto, modelos de IA podem apresentar variações inesperadas. Implementar revisões humanas é recomendado.
* Nem todos os conceitos possuem correspondências estritas; alguns mapeamentos são interpretativos. Mantenha transparência sobre a origem e o grau de certeza de cada correspondência.

---

*Última atualização: 27 de julho de 2025.*