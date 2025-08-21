# Protocolo Vivaldi + SCII: WebSocket ping/ack, Guia de Debug, CLI de diagnóstico, README e Makefile

## Resumo
Este PR consolida melhorias no subsistema de WebSocket (diagnóstico e robustez) e introduz um núcleo inicial do SCII (consulta por emoção/sintoma via CLI), além de documentação e utilitários para uso.

## Mudanças Principais
- Docs/WebSocket
  - Atualizado `docs/debug_websocket.md` com exemplo de handler `ping/ack` (servidor Socket.IO), checklists e cenários de diagnóstico.
  - Navegação do MkDocs inclui “Guia de Debug WS” (`mkdocs.yml`).
- SCII (Sistema de Correspondências Integradas de Inteligência)
  - `src/scii_core.py`: Loader para a base existente `scii_database.js/data/scii_database.json` + consulta por emoção/sintoma.
  - `src/scii_cli.py`: CLI com filtros por órgão/arquétipo e opção de saída JSON.
- README
  - Nova seção “SCII: Diagnóstico por Emoção (CLI)” com exemplos e saída JSON.
- Makefile
  - Alvos para facilitar uso do CLI: `scii`, `scii-json`, `scii-org`, `scii-arq`.
- Organização/Misc
  - Sincronização de arquivos e ajustes menores (inclusão de CHANGELOG, organização de backups, dashboard_principal.py etc.).

## Como Testar
1) Handshake WebSocket (Engine.IO v4)
```bash
curl --http1.1 -i -N \
  -H "Connection: Upgrade" \
  -H "Upgrade: websocket" \
  -H "Sec-WebSocket-Version: 13" \
  -H "Sec-WebSocket-Key: $(openssl rand -base64 16)" \
  "https://seu-dominio.com/socket.io/?EIO=4&transport=websocket"
```
- Esperado: `HTTP/1.1 101 Switching Protocols` + `Upgrade: websocket`

2) Cliente Socket.IO (fim-a-fim)
```bash
node scripts/teste-ws.js
```

3) SCII CLI
```bash
python src/scii_cli.py --emocao "ansiedade"
python src/scii_cli.py --emocao "ansiedade" --filtro-orgao "Respiratório"
python src/scii_cli.py --emocao "ansiedade" --json
# via Makefile
make scii EMOCAO="ansiedade"
make scii-json EMOCAO="ansiedade"
```

## Checklist
- [ ] WebSocket: handshake retorna `101 Switching Protocols`
- [ ] `scripts/teste-ws.js` conecta com sucesso e reporta status
- [ ] Servidor Socket.IO tem handler `ping/ack` implementado
- [ ] `python src/scii_cli.py --emocao "ansiedade"` retorna correspondências
- [ ] Opções de filtro e `--json` funcionam como esperado

## Notas
- O SCII utiliza a base existente em `scii_database.js/data/scii_database.json` (estrutura “letras”).
- Próximos passos: ampliar consultas (por órgão/arquétipo diretamente), adicionar testes automatizados e mapear Bet/Gimel com casos de uso.