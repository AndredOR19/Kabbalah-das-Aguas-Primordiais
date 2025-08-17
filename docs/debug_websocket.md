# Guia de Debug WebSocket (Socket.IO)

## Objetivo
Passo a passo para diagnosticar e corrigir erros de WebSocket (ex.: "Could not establish websocket connection") em ambientes com proxy (Nginx/Cloudflare/Apache) e front HTTPS.

---

## 1) Testes de Handshake com CURL (Precisão Máxima)

```bash
# Socket.IO v4 (Engine.IO = 4)
curl --http1.1 -i -N \
  -H "Connection: Upgrade" \
  -H "Upgrade: websocket" \
  -H "Sec-WebSocket-Version: 13" \
  -H "Sec-WebSocket-Key: $(openssl rand -base64 16)" \
  "https://teu-dominio.com/socket.io/?EIO=4&transport=websocket"

# Socket.IO v2 (Engine.IO = 3)
curl --http1.1 -i -N \
  -H "Connection: Upgrade" \
  -H "Upgrade: websocket" \
  -H "Sec-WebSocket-Version: 13" \
  -H "Sec-WebSocket-Key: $(openssl rand -base64 16)" \
  "https://teu-dominio.com/socket.io/?EIO=3&transport=websocket"
```

- Sucesso: resposta contém `HTTP/1.1 101 Switching Protocols` + `Upgrade: websocket`.
- Falha: 400/502/timeout → proxy/servidor não aceitou upgrade.

---

## 2) Validação fim-a-fim com socket.io-client

```bash
npm install socket.io-client
```

```javascript
// scripts/teste-ws.js
const { io } = require('socket.io-client');
const socket = io('wss://teu-dominio.com', {
  path: '/socket.io',
  transports: ['websocket'],
  reconnectionAttempts: 3,
});

socket.on('connect', () => console.log('✅ Conectado | ID:', socket.id));
socket.on('connect_error', (err) => console.error('❌ Falha:', err.message));
socket.on('disconnect', () => console.log('🚫 Desconectado'));
```

```bash
node scripts/teste-ws.js
```

---

## 3) Configuração robusta de Nginx

Considere usar este exemplo (arquivo: `docs/nginx_websocket_example.conf`):

```nginx
map $http_upgrade $connection_upgrade { default upgrade; '' close; }

server {
  # ... demais configurações ...
  location /socket.io/ {
    proxy_pass http://127.0.0.1:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_set_header Host $host;
    proxy_buffering off;
    proxy_read_timeout 600s;
    proxy_send_timeout 600s;
    proxy_no_cache 1;
    proxy_cache_bypass 1;
  }
}
```

- Se não forçar `transports: ['websocket']` no cliente, garanta também polling em `/socket.io/?transport=polling`.

---

## 4) Apache (habilitar módulos + configuração)

```bash
sudo a2enmod proxy proxy_http proxy_wstunnel && sudo systemctl reload apache2
```

```apache
ProxyPass        "/socket.io/"  "ws://127.0.0.1:3000/socket.io/"
ProxyPassReverse "/socket.io/"  "ws://127.0.0.1:3000/socket.io/"
ProxyPassMatch   "^/socket.io/(.*)$" "http://127.0.0.1:3000/socket.io/$1"
```

---

## 5) Cloudflare

- Habilitar WebSockets no painel.
- Page Rule para `teu-dominio.com/socket.io/*` com Cache Level: Bypass.
- SSL: Full (Strict) se houver certificado válido no origin.
- Evitar Rocket Loader/Mirage para essa rota.
- Manter heartbeats no servidor/cliente se desconectar após ociosidade.

---

## 6) Servidor Socket.IO (CORS, ping/pong)

```javascript
const { Server } = require('socket.io');
const http = require('http');
const httpServer = http.createServer();
const io = new Server(httpServer, {
  cors: {
    origin: 'https://teu-dominio.com',
    methods: ['GET', 'POST'],
    credentials: true,
  },
  transports: ['websocket', 'polling'],
  pingInterval: 25000,
  pingTimeout: 5000,
  connectionStateRecovery: {
    maxDisconnectionDuration: 2 * 60 * 1000,
  },
});

// Handler essencial para teste de latência (ping/ack)
io.on('connection', (socket) => {
  socket.on('ping', (timestamp, callback) => {
    callback(Date.now()); // responde com timestamp atual
  });
});

setInterval(() => io.emit('heartbeat', Date.now()), 20000);
```

---

## 7) Checklist Rápido

- [ ] `curl --http1.1` retorna `101 Switching Protocols`
- [ ] `node scripts/teste-ws.js` conecta com sucesso
- [ ] Nginx com `map $http_upgrade` e timeouts adequados
- [ ] Cloudflare com WebSockets habilitado e cache bypass
- [ ] Servidor com CORS e ping/pong configurados

---

## 8) Diagnóstico rápido

- `wscat` conecta? → servidor OK, falha é front/CORS.
- `curl` mostra 101? → handshake OK, investigue timeout no app.
- `curl` 400/502? → proxy/servidor mal configurado.
- Nada conecta nem no 4G? → bloqueio de rede/ISP.